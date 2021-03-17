#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='gc_cpm_networks',
    version='0.0.1',
    description='Global Context Convolutional Pose Machine Network',
    author='Kacper Kulczak',
    author_email='k.kulczak@xberry.tech',
    packages=find_packages(include=['gc_cpm_networks']),
    python_requires=">=3.8.*",
)
