#!/usr/bin/python3

import os
from os import path
import sys


temp_dir = 'temp'
build_dir = 'out'
run_dir = 'out/run'
jar_out_dir = 'out/jar'
jmod_out_dir = 'out/jmod'
module_dir='.'
dependency_dirs=['dependencies/jars']
jmod_dirs=['dependencies/native/jmods']
timestamp_cachefile=path.join(temp_dir, 'file_timestamp_cache.json')

maven_deps = []

java_exec='java'
javac_exec='javac'
jlink_exec='jlink'
jar_exec='jar'
jmod_exec='jmod'
python_exec='python'
maven_exec='mvn'

this_file = path.realpath(__file__)
this_dir = path.dirname(this_file)
root_dir = path.dirname(path.abspath(__file__))
os.chdir(root_dir)

if 'win' in sys.platform:
	this_os_arch='windows-x64'
elif 'linux' in sys.platform:
	this_os_arch='linux-x64'
elif 'darwin' in sys.platform:
	this_os_arch='osx-x64'

