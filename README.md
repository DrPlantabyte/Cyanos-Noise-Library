# Cyanos-Noise-Library
A simple java library for 2D and 3D fractal noise generation (aka "Perlin Noise").

### Sample Code
The following code creates a buffered image, fills it with a greyscale perlin noise pattern, and then displays the image in a JDialog window.
```java
        int size = 400;
        java.awt.image.BufferedImage bimg 
                = new java.awt.image.BufferedImage(size,size,
                        java.awt.image.BufferedImage.TYPE_INT_ARGB
                );
        FractalNoiseGenerator2D prng 
                = new DefaultFractalNoiseGenerator2D(
                        System.currentTimeMillis()
                );
        final double precision = 1.0/size;
        final double pixelSize = 1.0/size*4;
        for(int x = 0; x < size; x++){
            for(int y = 0; y < size; y++){
                float v = (float)prng.valueAt(
                            precision,
                            x*pixelSize-0.5, 
                            y*pixelSize-0.5
                );
                v += 1;
                v *= 0.5f;
                if(v < 0) v = 0f;//0.5f;
                if(v > 1) v = 1f;//0.5f;
                bimg.setRGB(x, y, java.awt.Color.HSBtoRGB(0f, 0f, v));
            }
        }
        javax.swing.JOptionPane.showMessageDialog(
                null, 
                new javax.swing.JLabel(new javax.swing.ImageIcon(bimg))
        );
```
