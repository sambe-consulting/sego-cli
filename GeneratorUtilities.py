from termcolor import colored
import click
from ApplicationUtilities import ApplicationUtilities
def get_generate_doc():
    return f"The %s command generates sego objects ,use the %s argument to choose object \n\n\n set --target= %s|%s:" \
           % (colored("generate", "green"),
              colored("--target", "yellow"),
              colored("application", "blue"),
              colored("route", "blue"))

def get_generate_target_help():
    return "Set target to generate [%s,%s ]" \
           % (colored("application", "blue"), colored("routes", "blue"))


def run_generate_command(context, target):
    if target == "application":
        app_utils = ApplicationUtilities()
        app_utils.repl()

    elif target == "routes":
        pass

