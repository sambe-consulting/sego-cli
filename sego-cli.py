#!env/bin/python3

import fire
from DocUtilities import *
from SetupUtilities import *
from termcolor import colored


@doc(main_docstring())
class Sego(object):
    def __init__(self):
        self.setup_utilities = SetupUtilities()

    @doc(SetupUtilities().setup_documentation())
    def setup(self,clean_up=False):
        if clean_up:
            self.setup_utilities.clean_up()
        self.setup_utilities.setup()



if __name__ == '__main__':
    fire.Fire(Sego)
