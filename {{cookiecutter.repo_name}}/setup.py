from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.repo_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    packages=find_packages(),
    keywords=["omero", "example"],
)
