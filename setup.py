from setuptools import find_packages
from setuptools import setup

setup(
    name="data_engineer_playground",
    version="0.1.0",
    description="A monorepo used to try things.",
    author="Cristian Webber",
    author_email="cbwebbers@gmail.com",
    url="https://github.com/cristianwebber/data_engineer_playground",
    packages=find_packages(exclude=("tests*", "testing*")),
)
