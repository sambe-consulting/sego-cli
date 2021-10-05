from termcolor import colored
from models.application import Applications
from orator.exceptions.orm import *
import sys, os, inspect
from pathlib import Path
from contextlib import contextmanager
import importlib
from uuid import uuid4
import pyfiglet
import getpass
from CodeGenerationUtilities import CodeGenerationUtilities
from datetime import datetime


class ControllerUtilities:
    def __init__(self):
        self.tasks = ["list", "generate", "delete"]
        self.active_app = None
        self.known_controllers = []
        self.code_generator = CodeGenerationUtilities()

    def get_controller_doc(self):
        doc = "The " + colored("controller", "green") + " command manages controller level tasks." \
                                                        " set the " + colored("--task",
                                                                              "yellow") + " argument to %s|%s|%s" % (
                  colored("list", "blue"), colored("generate", "blue"), colored("delete", "blue"))
        doc = doc + "\n\n The " + colored("list", "blue") + " task lists all controllers for the active application "
        doc = doc + "\n\n The " + colored("generate",
                                          "blue") + " task generates a new controller for the active application "
        doc = doc + "\n\n The " + colored("delete", "blue") + " task deletes a controller for the active application "
        return doc

    @contextmanager
    def add_to_path(self, path):
        import sys
        old_path = sys.path
        sys.path = sys.path[:]
        sys.path.insert(0, path)
        try:
            yield
        finally:
            sys.path = old_path

    def path_import(self, absolute_path):
        '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
        with self.add_to_path(os.path.dirname(absolute_path)):
            spec = importlib.util.spec_from_file_location(absolute_path, absolute_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module

    def cleanup(self, path, newpath):
        bad_words = ['import']
        with open(path) as oldfile, open(newpath, 'w') as newfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in bad_words):
                    if 'BaseController' in line:
                        line = line.split("(")[0] + ":\n"
                        newfile.write(line)
                    else:
                        newfile.write(line)
        return newfile

    def set_active(self):
        try:
            self.active_app = Applications.where('active', '=', 1).first_or_fail()
        except ModelNotFound as e:
            sys.exit(colored("No active application found.", "red") + colored(" Please active a application to proceed",
                                                                              "yellow"))

        self.active_app = Applications.where('active', '=', 1).first_or_fail()
        self.active_app_dict = self.active_app.attributes_to_dict()
        app_directory = Path(self.active_app_dict["app_directory"]) / "app/Controllers"
        root_directory = Path(self.active_app_dict["app_directory"])
        sys.path.append(str(root_directory))
        self.all_files = []
        for root, subdirs, files in os.walk(app_directory):
            if '__pycache__' not in root:
                temp_root = Path(root)
                self.all_files = self.all_files + [temp_root / file for file in files if file != '__init__.py']

    def list(self, kwargs):
        self.set_active()
        print(colored("*", "yellow") * 80)
        print(colored(pyfiglet.figlet_format("" + self.active_app_dict["app_name"] + "  CONTROLLERS "), "green"))

        print(colored("=", "yellow") * 80)

        for file in self.all_files:
            new_name = str(uuid4()) + ".py"
            self.cleanup(file, new_name)
            module = self.path_import(new_name)
            for name, obj in inspect.getmembers(module):
                try:
                    if inspect.isclass(obj):
                        self.known_controllers.append(name)
                        print(colored("CONTROLLER NAME: ", "green") + " " + colored(name, "blue"))
                        functions = inspect.getmembers(obj, predicate=inspect.isfunction)
                        for function_name, function in functions:
                            # print(function)
                            print(colored("---", "yellow") + " " + colored("ACTION NAME: ", "green"),
                                  " " + colored(function_name, "blue"))
                            arguments = inspect.getfullargspec(function)[0]
                            for arg in arguments:
                                if arg != 'self':
                                    print(colored("--- --- ---", "yellow") + " " + colored("ARGUMENT NAME: ", "green"),
                                          " " + colored(arg, "blue"))
                except:
                    pass
            print(colored("=", "yellow") * 80)

            os.remove(new_name)
        print("\n")
        print(colored("*", "yellow") * 80)

    def generate(self, kwargs):
        save_stdout = sys.stdout
        sys.stdout = open('trash', 'w')
        self.list(kwargs)
        sys.stdout = save_stdout

        ctrl_data = {}
        controller_path = Path(self.active_app_dict["app_directory"]) / "app/Controllers"
        exit_flag = True
        ctrl_data["name"] = input(
            colored("Please enter controller name ", "green") + colored("e.g HomeController : ", "yellow"))
        while ctrl_data["name"] in self.known_controllers and exit_flag:
            print("The controller name: " + colored(ctrl_data["name"], "red") + " already exists")
            ctrl_data["name"] = input(colored("Enter controller name or type exit to exit : ", "green"))
            if ctrl_data["name"] == 'exit':
                exit_flag = False
                sys.exit("EXITING !!!")
        ctrl_data["controller_description"] = input(
            colored("Please enter a short description of the controller:", "green"))
        ctrl_data["author"] = input(
            colored("Enter controller author ", "green") + colored("default (" + getpass.getuser() + "):"))
        ctrl_data["author_email"] = input(colored("Enter the email address of the author/maintainer: ", "green"))
        ctrl_data["version"] = input(colored("Enter the version of this controller: ", "green"))
        ctrl_data["controller_title"] = ctrl_data["name"]
        ctrl_data["controller_name"] = ctrl_data["name"]
        now = datetime.now()
        ctrl_data["generation_date"] = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        results = self.code_generator.generate('controller.tpl', ctrl_data)
        filename = ctrl_data["name"] + ".py"
        controller_file = controller_path / filename
        with open(controller_file, "w") as f:
            f.write(results)
        print(results)

    def delete(self, kwargs):
        save_stdout = sys.stdout
        sys.stdout = open('trash', 'w')
        self.list(kwargs)
        sys.stdout = save_stdout
        controller_path = Path(self.active_app_dict["app_directory"]) / "app/Controllers"
        if 'name' in kwargs and isinstance(kwargs['name'],str):
            filename = kwargs["name"] + ".py"
            controller_file = controller_path / filename
            if  os.path.exists(controller_file):
                os.remove(controller_file)
            else:
                print(colored("Controller with name ", "red") + colored(str(kwargs['name']),"yellow") +colored(" does not exist!!","red"))
        else:
            print(colored("Please use --name  to choose the controller to delete", "yellow"))




    def run(self, task, kwargs):
        if task.lower() in self.tasks:
            method = getattr(self, task.lower())
            method(kwargs)
