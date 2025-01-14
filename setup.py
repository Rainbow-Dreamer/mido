#!/usr/bin/env python
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


def get_about():
    about = {}

    path = os.path.join(here, 'mido_fix', '__about__.py')
    with open(path, 'rt') as aboutfile:
        exec(aboutfile.read(), about)

    return about


about = get_about()

from setuptools import setup, find_packages

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

elif sys.argv[-1] == "docs":
    os.system("sphinx-build docs docs/_build")
    sys.exit()

setup(
    name='mido_fix',
    version='1.2.12',
    description='MIDI Objects for Python',
    long_description=open('README.rst', 'rt').read(),
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    package_data={'mido_fix': ['./*']},
    packages=find_packages(),
    scripts=[
        'bin/mido-play', 'bin/mido-ports', 'bin/mido-serve', 'bin/mido-connect'
    ],
    include_package_data=True,
    install_requires=[],
    extras_require={
        'dev': [
            'check-manifest>=0.35',
            'flake8>=3.4.1',
            'pytest>=3.2.2',
            'sphinx>=1.6.3',
        ],
        'ports': ['python-rtmidi>=1.1.0']
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
