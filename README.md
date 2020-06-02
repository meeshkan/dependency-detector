[![Python](https://github.com/meeshkan/dependency-detector/workflows/Python/badge.svg)](https://github.com/meeshkan/dependency-detector/actions?query=workflow%3APython)
[![PyPI version](https://badge.fury.io/py/dependency-detector.svg)](https://badge.fury.io/py/dependency-detector)
[![License](https://img.shields.io/pypi/l/http-types)](LICENSE)

# dependency-detector
Tool to analyse a project for packages necessary to build it.

# Installation
```sh
pip install dependency-detector
```

# Usage
Specify a directory containing a project. This will output the commands necessary to install build dependencies on a Ubuntu 20.04 environment:

```sh
$ dependency-detector tests/python37-from-pipfile
apt-get -q -y install software-properties-common; add-apt-repository ppa:deadsnakes/ppa; apt-get -q update; apt-get -q -y install python3.7

$ dependency-detector tests/java8-and-maven
apt-get -q -y install openjdk-8-jdk-headless; apt-get -q -y install maven
```

# Development
1. Create a new virtual environment.
1. Install dependencies: `pip install --upgrade -e '.[dev]'`
1. Install [pyright](https://github.com/microsoft/pyright).
1. Run `python setup.py test` to test.
1. Run `pip install dependency-detector` to install the command-line tool

# Publishing
1. Bump the version in [setup.py](./setup.py). Commit and push.
1. Run `python setup.py test` and `python setup.py dist` to check that everything works.
1. To build and upload the package, run `python setup.py upload`. Insert PyPI credentials to upload the package to `PyPI`. The command will also run `git tag` to tag the commit as a release and push the tags to remote.
