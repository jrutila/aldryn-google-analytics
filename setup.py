#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from aldryn_google_analytics import __version__


setup(
    name='aldryn-google-analytics',
    version=__version__,
    description='Adds Google Analytics support for django CMS cloud',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-google-analytics',
    packages=['aldryn_google_analytics'],
    install_requires=[
        'Django>=1.10',
        'aldryn-snake',
    ],
    license=open('LICENSE.txt', 'r').read(),
    include_package_data=True,
    zip_safe=False
)
