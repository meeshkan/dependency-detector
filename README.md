# dependency-detector

[![Python](https://github.com/meeshkan/dependency-detector/workflows/Python/badge.svg)](https://github.com/meeshkan/dependency-detector/actions?query=workflow%3APython)
[![PyPI version](https://badge.fury.io/py/dependency-detector.svg)](https://badge.fury.io/py/dependency-detector)
[![License](https://img.shields.io/pypi/l/http-types)](LICENSE)
[![Chat on Gitter](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/meeshkan/community)

A tool that analyzes a project and returns the packages necessary to build it.

Available as a PyPI package: [`dependency-detector`](https://pypi.org/project/dependency-detector/)

## What's in this document:

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
    - [Getting started](#getting-started)
    - [Running the tests](#running-the-tests)
- [Publishing the `dependency-detector` as a PyPI package](#publishing-the-dependency-detector-as-a-pypi-package)
- [Contributing](#contributing)

## Installation

Install via [pip](https://pip.pypa.io/en/stable/installing/) (requires **Python 3.8+**):

```sh
pip install dependency-detector
```

This will install the `dependency-detector` command-line tool. 

## Usage

To use the command-line tool, run `dependency-detector` followed by a path to a directory containing a project. 

```sh
dependency-detector path/to/directory
```

> Note: If you're inside the directory you'd like to check, you can designate `.` as the path.

This will output the commands necessary to install and build dependencies on a Ubuntu 20.04 environment.

Here are some example outputs from the [tests](./tests/):

```sh
# Python
$ dependency-detector tests/python37-from-pipfile
apt-get -q -y install software-properties-common; add-apt-repository ppa:deadsnakes/ppa; apt-get -q update; apt-get -q -y install python3.7

# Java
$ dependency-detector tests/java8-and-maven
apt-get -q -y install openjdk-8-jdk-headless; apt-get -q -y install maven

# JavaScript
$ dependency-detector tests/package-json
apt-get -q -y install npm
```

The `dependency-detector` currently supports Python, Java, or JavaScript projects, but we're hoping to support more in the future. Please [file an issue](https://github.com/meeshkan/dependency-detector/issues/new) if you have a request.

It's also important to note that while the `dependency-detector` can provide a good guess of the required dependencies, there will always be edges cases and unique constructs this tool might not cover.

## Development

Here are some useful tips for building and running the `dependency-detector` from source. 

If you run into any issues, please [reach out to our team on Gitter](https://gitter.im/meeshkan/community).

### Getting started

1. Clone and move into this repository: `git clone https://github.com/meeshkan/dependency-detector && cd dependency-detector`
1. Create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
1. Install dependencies: `pip install --upgrade -e '.[dev]'`
1. Install [pyright](https://github.com/microsoft/pyright).
1. Run `pip install dependency-detector` to install the command-line tool.

### Running the tests

All of the checks live in the [`tests` directory](./tests/). To execute them, run:

```bash
$ python setup.py test
```

## Publishing the `dependency-detector` as a PyPI package

1. Bump the version in [setup.py](./setup.py). Commit and push.
1. Run `python setup.py test` and `python setup.py dist` to check that everything works.
1. To build and upload the package, run `python setup.py upload`. Insert PyPI credentials to upload the package to `PyPI`. The command will also run `git tag` to tag the commit as a release and push the tags to remote.

## Contributing

Thanks for your interest in contributing! Please take a look at our [development guide](#development) for notes on how to develop the package locally. A great way to start contributing is to [file an issue](https://github.com/meeshkan/dependency-detector/issues/) or [make a pull request](https://github.com/meeshkan/dependency-detector/pulls).

Please note that this project is governed by the [Meeshkan Community Code of Conduct](https://github.com/meeshkan/code-of-conduct). By participating, you agree to abide by its terms.
