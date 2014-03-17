# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sisposto
version = sisposto.__version__

setup(
    name='sgt',
    version=version,
    author='',
    author_email='bnafta@gmail.com',
    packages=[
        'sisposto',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['sisposto/manage.py'],
)