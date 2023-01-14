# -*- coding: utf-8 -*-
'''
Setup file for ruk_utils python package.
'''
from setuptools import setup, find_packages

setup(
	name='ruk_utils',
	version='1.0',
	url='https://github.com/rukyr97/ruk_utils',
	author='Ruben Queiros',
	description='A growing repo of code snippets, in the form of a python package,'
	'that I found useful saving',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	],
	package_dir={"": "src"},
	packages=find_packages(where="src"),
	python_requires=">=3.9.15",
)
