from detector.detect import Dependency, detect_dependencies


def test_java8_and_maven():
    assert set([Dependency.JAVA8, Dependency.MAVEN]) == detect_dependencies(
        "tests/java8-and-maven"
    )


def python37_from_pipfile():
    assert set([Dependency.PYTHON37]) == detect_dependencies(
        "tests/python37-from-pipfile"
    )