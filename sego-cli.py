#!env/bin/python3

import fire
from DocUtilities import *
from ApplicationUtilities import *
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

    @doc(ApplicationUtilities().get_application_doc())
    def application(self,task):
        pass
    



if __name__ == '__main__':
    setup_utils = SetupUtilities()
    db = DatabaseUtilities()
    db_path = db.get_database_path()
    home = setup_utils.get_home_dir()
    if os.path.exists(db_path):
        fire.Fire(Sego)
    else:
        setup_utils.setup()

