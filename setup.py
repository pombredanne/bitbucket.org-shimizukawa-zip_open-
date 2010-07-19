# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.1.0'
long_description = open("README.txt").read()

classifiers = [
   "Development Status :: 4 - Beta",
   "Intended Audience :: Developers",
   "License :: OSI Approved :: Python Software Foundation License",
   "Programming Language :: Python",
   "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name='zip_open',
    version=version,
    description='file open from nested zip file archive.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['zip file open'],
    author='Takayuki SHIMIZUKAWA',
    author_email='shimizukawa at gmail.com',
    url='http://bitbucket.org/shimizukawa/zip_open/',
    license='PSL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=True,
    test_suite='tests',
)

