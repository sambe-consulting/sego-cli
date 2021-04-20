from termcolor import colored
import click, os
from models.targets import Targets
from pluralizer import Pluralizer
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY,DEFAULT,PLAIN_COLUMNS,MARKDOWN,ORGMODE


from TargetUtilites import *


class ListUtilities:

    def __init__(self):
        self.target_utilities = TargetUtilities()

    def get_list_target_help(self):
        return "Set target to list [ %s ,%s,%s ]" \
               % (colored("commands", "blue"), colored("applications", "blue"), colored("routes", "blue"))

    def get_list_doc(self):
        try:
            targets = self.target_utilities.get_target_names()
        except:
            targets = []
        ret = [colored('list', 'green'),colored("--target", "yellow")]
        tgs = []
        for target in targets:
            tgs.append(colored(target,'blue'))

        doc = "The %s , command lists objects ,use the %s argument to choose object \n\n set --target= "%tuple(ret)+"|".join(tgs)

        return doc


    def run_list(self,target):
        if target.lower() in [x.lower() for x in self.target_utilities.get_target_names()]:
            pluralizer = Pluralizer()
            util_name = pluralizer.singular(target.lower().capitalize())+"Utilities"
            util_module = __import__(util_name)
            util_class = getattr(util_module,util_name)
            util_instance = util_class()
            util_instance.list()

        else:
            print(self.get_list_doc())


        # print(targets)


