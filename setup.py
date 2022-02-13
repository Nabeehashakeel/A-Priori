#!/usr/bin/env python
import apyori
import setuptools

setuptools.setup(
    name='Assignment',
    description='Data Mining Assignment 1 Association Rule Mining using A-Priori',
    long_description=open('README.rst').read(),
    version=apyori.__version__,
    author=apyori.__author__,
    author_email=apyori.__author_email__,
    py_modules=['apyori'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
    entry_points={
        'console_scripts': [
            'apyori-run = apyori:main',
        ],
    },
)
