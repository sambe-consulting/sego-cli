import os
from termcolor import colored

MAIN_DIR = os.getcwd()


def version():
    with open(MAIN_DIR + "/version.txt", "r") as f:
        version = f.read()
    return version


def main_docstring():
    return colored("Sego","green")+" command line interface version: " + colored(version(),"yellow")


def doc(docstring):
    def document(func):
        func.__doc__ = docstring
        return func

    return document
