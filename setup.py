from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

extra = {}

try:
    from pinyin import version
except ImportError:
    version = 'unknown'

try:
    file = open('README.md', 'rt')
    content = file.read()
    file.close()
    extra['long_description'] = content
except IOError:
    pass

setup(
    name='pinyin',
    version=version,
    description='Convert chinese to Pinyin(Only CH Simple)',
    author='qingchen',
    author_email='luoweifeng1989@gmail.com',
    url='',
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
