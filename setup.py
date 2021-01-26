#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="powerline-shell",
    version="1.0.0",
    description="A pretty prompt for your shell",
    author="shareof",
    author_email="shareof@test.com",
    license="MIT",
    url="https://github.com/shareof/powerline-shell",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    packages=[
        "powerline_shell",
        "powerline_shell.segments",
        "powerline_shell.themes",
    ],
    install_requires=[
        "argparse",
    ],
    entry_points="""
    [console_scripts]
    powerline-shell=powerline_shell:main
    """,
)
