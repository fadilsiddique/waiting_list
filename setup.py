# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in waiting_list/__init__.py
from waiting_list import __version__ as version

setup(
	name='waiting_list',
	version=version,
	description='waitinglist',
	author='Tridz',
	author_email='fadil@tridz.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
