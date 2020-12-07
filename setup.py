#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='CkanMetaTester',
    version='0.1',
    description='Testing Framework for Validating ckans/netkans',
    author='Leon Wright',
    author_email='techman83@gmail.com',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'development': [
            'pylint',
            'autopep8',
            'mypy',
        ]
    },
)
