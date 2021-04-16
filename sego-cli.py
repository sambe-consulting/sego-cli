#!env/bin/python3

import fire
from DocUtilities import *
from SetupUtilities import *
from ListUtilities import *
from models.targets import Targets
from termcolor import colored
from orator.exceptions.query import QueryException


@doc(main_docstring())
class Sego(object):
    def __init__(self):
        self.list_utilities  = ListUtilities()


    @doc(ListUtilities().get_list_doc())
    def list(self,target):
        self.list_utilities.run_list(target=target)





if __name__ == '__main__':
    fire.Fire(Sego)

