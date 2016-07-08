# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup, find_packages

extra = {}

with open('README.md', 'rt') as f:
    extra['long_description'] = f.read()

setup(
    name='smart_pinyin',
    version='0.4.1',
    description='Smart Chinese-to-Pinyin converter.',
    author='mapix',
    author_email='mapix.me@gmail.com',
    url='https://github.com/mapix/pinyin',
    license='MIT',
    packages=find_packages(),
    package_data={
        'pinyin': [
            'data/*',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=['distribute', 'jieba'],
    **extra
)
