import os
from termcolor import colored

MAIN_DIR = os.getcwd()


def version():

    return '0.1.0.0'


def main_docstring():
    return colored("Sego","green")+" command line interface version: " + colored(version(),"yellow")


def doc(docstring):
    def document(func):
        func.__doc__ = docstring
        return func

    return document
