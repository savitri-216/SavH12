"""Python setup.py for savh12 package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("savh12", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="savh12",
    version=read("savh12", "VERSION"),
    description="Awesome savh12 created by savitri-216",
    url="https://github.com/savitri-216/SavH12/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="savitri-216",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["savh12 = savh12.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
