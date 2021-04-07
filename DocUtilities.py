import os
import click

MAIN_DIR = os.getcwd()


def version():
    with open(MAIN_DIR + "/version.txt", "r") as f:
        version = f.read()
    return version


def main_docstring():
    return "Sego command line interface version: " + version()


def doc(docstring):
    def document(func):
        func.__doc__ = docstring
        return func

    return document
