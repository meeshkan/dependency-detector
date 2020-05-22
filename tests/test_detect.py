from detector.detect import Dependency, detect_dependencies


def test_docker_and_docker_compose():
    assert [Dependency.DOCKER, Dependency.DOCKER_COMPOSE] == detect_dependencies(
        "tests/docker-and-docker-compose"
    )


def test_java8_and_maven():
    assert [Dependency.JAVA8, Dependency.MAVEN] == detect_dependencies(
        "tests/java8-and-maven"
    )


def test_java11_from_pom():
    assert [Dependency.JAVA11, Dependency.MAVEN] == detect_dependencies(
        "tests/java11-from-pom"
    )


def test_python37_from_pipfile():
    assert [Dependency.PYTHON37] == detect_dependencies("tests/python37-from-pipfile")


def test_package_json():
    assert [Dependency.NODEJS] == detect_dependencies("tests/package-json")
