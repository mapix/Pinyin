# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

extra = {}

with open('README.md', 'rt') as f:
    extra['long_description'] = f.read()

setup(
    name='pinyin',
    version='0.2.1',
    description='Smart Chinese-to-Pinyin converter.)',
    author='mapix',
    author_email='mapix.me@gmail.com',
    url='https://github.com/mapix/pinyin',
    license='MIT',
    packages=find_packages(),
    package_data={
        'pinyin': [
            'data/mmseg/*',
            'data/pinyin/*',
        ]
    },
    install_requires=['distribute', 'mmseg'],
    **extra
)
