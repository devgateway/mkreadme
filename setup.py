# Copyright 2018, Development Gateway, Inc.
# This file is part of readmegen, see COPYING.

from setuptools import setup

setup(
        name = "readmegen",
        version = "0.1",
        license = "GPLv3+",
        description = "Readme generator for Ansible roles",
        author = "Development Gateway",
        python_requires = ">= 3.4",
        packages = ["readmegen"],
        install_requires = [
            "PyYAML",
            "markdown"
            ],
        entry_points = {
            "console_scripts": [
                "readmegen = readmegen.main:main"
                ]
            }
        )
