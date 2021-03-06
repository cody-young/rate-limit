#!/usr/bin/python
from setuptools import setup, find_packages
import sys

name = 'rate-limit'
version = "0.1.1"
_ver = sys.version_info

setup(
    name=name,
    version=version,
    description='Redis ratelimit implementation.',
    classifiers=[],
    packages=['ratelimit'],
    author='Jason Foote',
    author_email='',
    url='https://github.com/DomainTools/rate-limit',
)
