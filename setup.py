from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AR",
    version="0.1",
    author="Deepank",
    packages=find_packages(),
    install_requires = requirements,
)