# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "DateTimeUUID",
    version = "0.1",
    description = "Provides a UUID-like string with a human readable timestamp",
    author = "P. Scott DeVos",
    author_email = "scott@bintouch.org",
    license = "BSD 4-Clause",
    packages = find_packages(exclude=['tests', 'tests.*']),
    install_requires = [
    ],
    keywords = "UUID uuid human readable",
    url = "https://github.com/pscottdevos/datetime_uuid",
)
