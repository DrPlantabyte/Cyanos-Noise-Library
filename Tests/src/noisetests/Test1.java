package noisetests;

import cchall.noise.SphericalSurfaceFractalNoiseGenerator;
import cchall.noise.math.AbstractNumberGenerator;
import cchall.noise.math.random.DefaultRandomNumberGenerator;

import javax.swing.*;
import java.awt.image.BufferedImage;

public class Test1 {
	
	public static void main(String[] args){
		double radius = 1000;
		double initialNoiseScale = 1000;
		double initialNoiseMagnitude = 1;
		double octaveScaleMultiplier = 0.5;
		double octaveMagnitudeMultiplier = 0.5;
		AbstractNumberGenerator seeder = new DefaultRandomNumberGenerator(12345);
		
		SphericalSurfaceFractalNoiseGenerator gen = new SphericalSurfaceFractalNoiseGenerator(
				radius ,
				initialNoiseScale ,
				initialNoiseMagnitude,
				octaveScaleMultiplier ,
				octaveMagnitudeMultiplier ,
				seeder
		);
		BufferedImage img = new BufferedImage(360, 180, BufferedImage.TYPE_INT_ARGB);
		final double degrees2radians = Math.PI/180.0;
		for(int lon = 0; lon < 360; lon++){
			int x = lon;
			for(int lat = -90; lat < 90; lat++){
				int y = 90 + lat;
				//
				final double v = gen.valueAt(10, lon*degrees2radians, lat*degrees2radians);
				int vi = (int)(255*v);
				if(vi > 255) vi = 255;
				if(vi < 0) vi = 0;
				int px = vi | vi<<8 | vi<<16 | 0xFF000000;
				img.setRGB(x, y, px);
			}
		}
		JOptionPane.showMessageDialog(null, new JLabel(new ImageIcon(img)));
	}
}
