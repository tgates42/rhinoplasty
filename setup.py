"""Packaging."""

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    """Import another file into the setup function.
    
    Taken from the example PyPI project. See
        http://packages.python.org/an_example_pypi_project/setuptools.html
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Rhinoplasty",
    version = "0.1.0",
    author = "Gary Donovan",
    author_email = "garyd@crucialfruit.com.au",
    license = "LGPL",
    keywords = "Nose test unittest",
    description = ("Experimental extensions to Nose."),
    long_description = read('README.txt'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Testing",
    ],
    packages = ["rhinoplasty"],
)
