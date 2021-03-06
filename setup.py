import os
import sys
from distutils import errors
from shutil import rmtree

from setuptools import Command, find_packages, setup

VERSION = "0.7.0"

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

REQUIRED = [
    "toml==0.10.0",
]

DEV = [
    "autopep8",
    "black",
    "flake8",
    "pylint",
    "pytest",
    "setuptools",
    "twine",
    "wheel",
]


# Optional packages
EXTRAS = {"dev": DEV}


class SetupCommand(Command):
    """Base class for setup.py commands with no arguments"""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def rmdir_if_exists(self, directory):
        self.status("Deleting {}".format(directory))
        rmtree(directory, ignore_errors=True)


def build():
    return os.system(
        "{executable} setup.py sdist bdist_wheel --universal".format(
            executable=sys.executable
        )
    )


def type_check():
    return os.system("pyright --lib -p pyrightconfig.json")


class BuildDistCommand(SetupCommand):
    """Support setup.py upload."""

    description = "Build the package."

    def run(self):
        self.status("Removing previous builds...")
        self.rmdir_if_exists(os.path.join(here, "dist"))

        self.status("Building Source and Wheel (universal) distribution...")
        exit_code = build()
        if exit_code != 0:
            raise errors.DistutilsError("Build failed.")
        sys.exit()


class TypeCheckCommand(SetupCommand):
    """Run type-checking."""

    description = "Run type-checking."

    def run(self):
        exit_code = type_check()
        self.status("Typecheck exited with code: {code}".format(code=exit_code))
        if exit_code != 0:
            raise errors.DistutilsError("Type-checking failed.")


class TestCommand(SetupCommand):
    """Support setup.py test."""

    description = "Run local test if they exist"

    def run(self):
        self.status("Formatting code with black...")
        exit_code = os.system("black .")
        if exit_code != 0:
            raise errors.DistutilsError("Formatting with black failed.")

        self.status("Running pytest...")
        exit_code = os.system("pytest")
        if exit_code != 0:
            raise errors.DistutilsError("Tests failed.")

        self.status("Running type-checking...")
        exit_code = type_check()
        if exit_code != 0:
            raise errors.DistutilsError("Type-checking failed.")

        self.status("Running flake8...")
        exit_code = os.system("flake8 --exclude .git,.venv,venv,__pycache__,build,dist")
        if exit_code != 0:
            raise errors.DistutilsError(" failed.")


class UploadCommand(SetupCommand):
    """Support setup.py upload."""

    description = "Build and publish the package."

    def run(self):

        self.status("Removing previous builds...")
        self.rmdir_if_exists(os.path.join(here, "dist"))

        self.status("Building Source and Wheel (universal) distribution...")
        exit_code = build()
        if exit_code != 0:
            raise errors.DistutilsError("Build failed.")
        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{about}".format(about=VERSION))
        os.system("git push --tags")

        sys.exit()


setup(
    name="dependency-detector",
    version=VERSION,
    description="Detect dependencies necessary to build a project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meeshkan/dependency-detector",
    author="Meeshkan Dev Team",
    author_email="dev@meeshkan.com",
    python_requires=">=3.8.0",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["dependency-detector = detector.detect:cli"]},
    cmdclass={
        "dist": BuildDistCommand,
        "test": TestCommand,
        "typecheck": TypeCheckCommand,
        "upload": UploadCommand,
    },
)
