#! /usr/bin/env python
# encoding: utf-8

VERSION = "0.1"
APPNAME = "wafTest"

def options(opt):
	opt.load('compiler_cxx')

def configure(cfg):
	cfg.load('compiler_cxx')
	cfg.LIB_SFML = ['sfml-graphics', 'sfml-system', 'sfml-window']
	cfg.LIBPATH_SFML   = ['thirdParty/SFML-2.2/lib']
	cfg.INCLUDES_SFML  = ['thirdParty/SFML-2.2/include']
	cfg.check(
		features='cxx cxxprogram', 
		cxxflags=['-std=c++11', '-Wall']
	)

def build(bld):
#	bld(export_includes='thirdParty/SFML-2.2/include', name='sfml')
	bld.recurse('src')

