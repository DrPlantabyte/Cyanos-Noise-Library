#!/usr/bin/python3

import os
from os import path
import sys

import pyb_java as java
import pyb_util as util
import pyb_maven as maven
import config

os.chdir(config.root_dir)

util.shell_command([config.python_exec, 'clean.py'])

compile_dir = path.join(config.build_dir,'compile')

# maven deps
maven.fetch(
	repositories_list=config.maven_deps, 
	download_dir=config.dependency_dirs[0], 
	maven_exec=config.maven_exec, 
	temp_dir=config.temp_dir
)

# module order must be explicit to avoid problems
modules = ['cchall.noise', 'cchall.noisetests'] # os.listdir(config.module_dir)

def compile_module(module_name):
	java.compile_module(
		module_name=module_name, 
		source_dir=path.join(config.module_dir, module_name,'src'),
		resource_dir=path.join(config.module_dir, module_name,'resources'),
		module_dependencies = [compile_dir] +
				util.list_files_by_extension(config.dependency_dirs,'.jar') +
				['%s/%s' % (x, config.this_os_arch) for x in config.jmod_dirs],
		temp_dir=config.temp_dir,
		output_dir=compile_dir,
		javac_exec=config.javac_exec
	)

for module_name in modules:
	compile_module(module_name)
# jar
java.jar_module(
	module_name='cchall.noise',
	module_version='2.02',
	compile_dir=path.join(compile_dir,'cchall.noise'),
	output_dir=config.jar_out_dir,
	temp_dir=config.temp_dir,
	main_class = None,
	jar_exec=config.jar_exec
)

java.jar_module(
	module_name='cchall.noisetests',
	module_version=None,
	compile_dir=path.join(compile_dir,'cchall.noisetests'),
	output_dir=config.jar_out_dir,
	temp_dir=config.temp_dir,
	main_class = 'cchall.noisetests.Test1',
	jar_exec=config.jar_exec
)

# jlink
java.jlink_module(
	module_name='cchall.noisetests',
	module_locations=['%s/%s' % (x, config.this_os_arch) for x in config.jmod_dirs] + 
			[compile_dir] + 
			util.list_files_by_extension(config.dependency_dirs,'.jar'),
	output_dir=path.join(config.build_dir,'image', config.this_os_arch),
	temp_dir=config.temp_dir,
	main_class = 'cchall.noisetests.Test1',
	jlink_exec=config.jlink_exec
)

# done
print('\nBUILD SUCCESFUL!\n')
