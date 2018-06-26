# Copyright 2018, Development Gateway, Inc.
# This file is part of mkreadme, see COPYING.

from setuptools import setup

setup(
    name = "mkreadme",
    version = "0.1",
    license = "GPLv3+",
    description = "Readme generator for Ansible roles",
    author = "Development Gateway",
    python_requires = ">= 3.4",
    packages = ["mkreadme"],
    package_data = {
        '': '*.j2'
    },
    install_requires = [
        "PyYAML",
        "jinja2 >= 2.6"
    ],
    entry_points = {
        "console_scripts": [
            "mkreadme = mkreadme.main:main"
        ]
    }
)
