# -*- coding: utf-8 -*-
"""
Setup script for a Python package
"""
import os
import re
from setuptools import setup

# Get the version from __init__.py
path = os.path.join(os.path.dirname(__file__), 'otak', '__init__.py')
with open(path) as f:
    version_file = f.read()

version = re.search(r"^\s*__version__\s*=\s*['\"]([^'\"]+)['\"]",
version_file, re.M)
if version:
    version = version.group(1)
else:
    raise RuntimeError("Unable to find version string.")

# Long description
with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name="otak",
    version=version,
    author="Mathieu Balesdent",
    description="This repository is a package offering rare event estimation methods based on active surrogate models.",
    license='GPLv3+',
    keywords=[
        'OpenTURNS', 
        'Reliabillity'
        ],
    url="https://github.com/m-balesdent/otak",
    packages=[
        'otak', 
        'test'
        ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        ],
    install_requires=[
        "numpy",
        "openturns>=1.18"
        ],
    )