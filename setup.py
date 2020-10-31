#!/usr/bin/env python
# -*- coding: latin-1 -*-
import codecs
import os
from setuptools import setup, find_packages
from wktdggs import __version__


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        *paths
    )
    return codecs.open(path, mode, encoding)


with open_local(["README.md"], encoding="utf-8") as readme:
    long_description = readme.read()

with open_local(["requirements.txt"]) as req:
    install_requires = req.read().split("\n")

setup(
    name="wkt-dggs",
    description="An OWL ontology documentation tool using Python and templating, based on LODE.",
    long_description=long_description,
    version=__version__,
    author="Nicholas J. Car",
    author_email="nicholas.car@surroundaustralia.com",
    packages=find_packages(exclude=["examples", "tests"]),
    url="https://github.com/rdflib/pyLODE",
    download_url="https://github.com/surroundaustralia/wkt-dggs/archive/v{:s}.tar.gz".format(__version__),
    license="LGPL",
    keywords=["Discrete Global Grid System", "DGGS", "Well-Known Text", "WKT", "geometry"],
    # entry_points={
    #     "console_scripts": [
    #         "pylode = pylode.cli:main",
    #     ]
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Bug Reports": "https://github.com/surroundaustralia/wkt-dggsissues",
        "Source": "https://github.com/surroundaustralia/wkt-dggs",
    },
    install_requires=install_requires,
    long_description_content_type="text/x-rst"
)
