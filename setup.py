# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='KeepWorking',
    version='0.1.0',
    description='Keep working and don’t \'leave\'',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yelijing18/KeepWorking',
    author='Lijing Ye',
    author_email='yelijing18@gmail.com',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6',
)
