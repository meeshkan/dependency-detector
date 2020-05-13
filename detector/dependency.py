#!/usr/bin/env python3

from enum import Enum


class Dependency(Enum):
    JAVA11 = ["openjdk-11-jdk-headless"]
    JAVA8 = ["openjdk-8-jdk-headless"]
    MAVEN = ["maven"]
    PYTHON36 = ["python3.6"]
    PYTHON37 = ["python3.7"]
    PYTHON38 = ["python3.8"]
