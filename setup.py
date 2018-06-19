from setuptools import setup, find_packages

setup(
name='dictsorted',
version='0.0.5',
packages=['dictsorted'],
scripts =['dictsorted/__init__.py', 'dictsorted/dictsorted.py'],
author='lucyking',
author_email='joehisaishi1943@gmail.com',
url='https://github.com/lucyking/dictsorted',
description='return [sorted(dict.key||value)]',
)

