#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('NEWS.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [
    'setuptools_scm'
]

test_requirements = [
    'pytest',
]

DESCRIPTION = ('Library that enables the creation of alternate constructor-like'
               'variant forms for arbitrary functions.')

setup(
    name='variants',
    use_scm_version={'write_to': 'src/variants/_version.py'},
    description=DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author="Paul Ganssle",
    author_email='paul@ganssle.io',
    url='https://github.com/python-variants/variants',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=True,
    keywords='variants',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
