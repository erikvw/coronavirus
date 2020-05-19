# -*- coding: utf-8 -*-
import os

from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    VERSION = f.read().strip()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="coronavirus",
    version=VERSION,
    author=u"Erik van Widenfelt",
    author_email="ew2789@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/erikvw/coronavirus",
    license="GPL license, see LICENSE",
    description="",
    long_description=README,
    zip_safe=False,
    keywords="django",
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    test_suite="runtests.main",
)