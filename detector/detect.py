#!/usr/bin/env python3

import sys
from typing import Set

from detector.dependency import Dependency
from detector.detect_java import detect_java
from detector.detect_python import detect_python


def detect_dependencies(directory_path: str) -> Set[Dependency]:
    detect_methods = [detect_java, detect_python]

    result = set()
    for detect_method in detect_methods:
        result.update(detect_method(directory_path))
    return result


def cli():
    if len(sys.argv) < 1:
        print("Usage: ./detect.py DIRECTORY")
        sys.exit(1)

    directory = sys.argv[1]
    packages_to_install = detect_dependencies(directory)
    print(str(packages_to_install))
