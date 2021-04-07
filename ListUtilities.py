from termcolor import colored
import click,os

def get_list_target_help():
    return "Set target to list [ %s ,%s,%s ]" \
           % (colored("commands", "blue"), colored("applications", "blue"), colored("routes", "blue"))


def get_list_doc():
    return f"The %s command lists objects ,use the %s argument to choose object \n\n\n set --target= %s|%s|%s:" \
           % (colored("list", "green"),
              colored("--target", "yellow"),
              colored("commands", "blue"),
              colored("applications", "blue"),
              colored("routes", "blue"))


# execute list command
def run_list_command(context, target):
    if target == "commands":
        click.echo(context.obj["entry_point"].get_help(context))
    elif target == "applications":
        pass
    elif target == "routes":
        pass
