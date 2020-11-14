#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='metadata-testing',
    version='0.1',
    description='Testing Library for CKAN/NetKAN Metadata',
    author='Leon Wright',
    author_email='techman83@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'git+https://github.com/KSP-CKAN/NetKAN-Infra.git#egg=pkg&subdirectory=netkan',
    ],
    extras_require={
        'development': [
            'pylint',
            'autopep8',
            'mypy',
        ]
    },
)
