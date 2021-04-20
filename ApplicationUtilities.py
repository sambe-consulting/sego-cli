import os, json, requests, shutil
from pathlib import Path
from zipfile import ZipFile
import uuid, sys
from datetime import datetime
from DatabaseUtilities import DatabaseUtilities
from SetupUtilities import SetupUtilities
from SegoExceptions import *
from termcolor import colored
from models.application import Applications
from prettytable import PrettyTable
import getpass
from orator.exceptions.orm import *


class ApplicationUtilities:
    def __init__(self):
        self.app_template_url = "https://codeload.github.com/sambe-consulting/sego-app/zip/refs/heads/master"
        self.db_utils = DatabaseUtilities()
        self.setup_utils = SetupUtilities()
        self.tasks = ["list", "generate", "delete", "register", "activate"]

    def get_application_doc(self):
        doc = "The " + colored("application", "green") + " command manages application level tasks.\n"
        task_list = []
        for task in self.tasks:
            task_list.append(colored(task, "blue"))

        task_list = '|'.join(task_list)
        doc = doc + "  set the " + colored("--task", "yellow") + " argument to " + task_list

        doc = doc + "\n\n\n\n The " + colored("list", "blue") + " task lists all applications registered into " + \
              colored("sego-cli", "green")
        doc = doc + "\n\n The " + colored("generate", "blue") + " task generates a new application, to use add the " + \
              colored("--name", "yellow") + " flag. e.g python -m " + colored("sego-cli",
                                                                              "green") + " application" + " " + \
              colored("--task", "yellow") + " generate --name blog"

        doc = doc + "\n\n The " + colored("delete", "blue") + " task deletes an application from " + colored("sego-cli",
                                                                                                             "green") + \
              " use the " + colored("--name",
                                    "yellow") + " flag to specify the application in question.This command only removes\n" \
                                                " the app from the CLI but does not delete the codebase from the filesystem" \
                                                "\n to delete the codebase use the " + colored("--clean-up",
                                                                                               "yellow") + " flag\n " \
                                                                                                           " and set it to true"

        doc = doc + "\n\n The " + colored("register",
                                          "blue") + " task, registers an application to be managed by  " + colored(
            "sego-cli", "green")+" the "+ colored("--app-dir","yellow")+" must be set to the home path of the app"
        doc = doc + "\n\n The " + colored("activate", "blue") + " task, makes an app active, " + colored("sego-cli",
                                                                                                         "green") + " can only " \
                                                                                                                    "work on an active app, use the " + colored(
            "--name", "yellow") + " or " + colored("--id",
                                                   "yellow") + " to activate an app."                                                                                                                           ""
        return doc

    def generate_application(self, application_data):
        directory = Path(application_data["app_directory"])
        name = application_data["app_name"]
        backend_name = name + "_" + str(uuid.uuid4())
        sego_dir = Path.home() / ".sego"
        try:
            if os.path.exists(directory / name):
                raise DirectryNotEmptyException("This directory already exists")
        except DirectryNotEmptyException as e:
            # print(e)
            sys.exit(e)
        r = requests.get(self.app_template_url, allow_redirects=True)
        download_dir = sego_dir / backend_name

        with open(download_dir, "wb") as f:
            f.write(r.content)

        self.clean_application(download_dir, directory, name)
        self.register_application(application_data)

    def clean_application(self, zip, directory, name):
        print(directory)
        with ZipFile(zip, 'r') as zipObj:
            zipObj.extractall(path=directory)
        os.rename(directory / "sego-app-master", directory / name)
        os.remove(str(zip))

    def register_application(self, application_data):
        directory = Path(application_data["app_directory"])
        name = Path(application_data["app_name"])
        configuration_path = directory / name / "app/Configurations/application/sego.json"
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        application_data["application_identifier"] = str(uuid.uuid4())
        configurations = {
            "app_name": application_data["app_name"],
            "application_identifier": application_data["application_identifier"],
            "description": application_data["description"],
            "developer": application_data["developer"],
            "created_at": dt_string,
            "updated_at": dt_string,
            "version": application_data["version"]
        }
        with open(configuration_path, "w") as f:
            json.dump(configurations, f, indent=4)
        self.setup_utils.virtualenv(name="env",directory=directory/name)
        self.db_utils.register_application(application_data)

    def generate(self, kwargs):
        def exists(app_name):
            apps = [x.app_name.lower() for x in Applications.all().all()]
            if app_name.lower() in apps:
                return True
            return False

        app_data = {}
        app_data["app_name"] = input(colored("Enter application name: ", "green"))
        exit_flag = True
        while exists(app_data["app_name"]) and exit_flag:
            print("The app name: " + colored(app_data["app_name"], "red") + " already exists")
            app_data["app_name"] = input(colored("Enter application name or type exit to exit : ", "green"))
            if app_data["app_name"] == 'exit':
                print("EXITING !!!")
                exit_flag = False
        app_data["description"] = input(colored("Enter application description: ", "green"))
        app_data["developer"] = input(
            colored("Enter application developer ", "green") + colored("default (" + getpass.getuser() + "):"))
        app_data["version"] = input(colored("Enter application version: ", "green"))
        app_data["app_directory"] = input(
            colored("Enter application directory ", "green") + colored("default (" + str(Path.cwd()) + "):"))
        app_data["developer"] = app_data["developer"].strip()
        if not app_data["developer"].strip():
            app_data["developer"] = getpass.getuser()
        if not app_data["app_directory"].strip():
            app_data["app_directory"] = str(Path.cwd())
        app_data["app_directory"] = app_data["app_directory"]+"/"+app_data["app_name"]
        exit_flag2 = True
        while os.path.exists(app_data["app_directory"]+"/"+app_data["app_name"]) and exit_flag2:
            print("The app directory: " + colored(app_data["app_directory"]+"/"+app_data["app_name"], "red") + " already exists")
            app_data["app_directory"] = input(
            colored("Enter application directory or exit to exit:", "green") + colored("default (" + str(Path.cwd()) + "):"))
        self.generate_application(application_data=app_data)

    def list(self, kwargs):
        def decompose(app_model):
            return {
                "app_name": app_model.app_name,
                "description": app_model.description,
                "developer": app_model.developer,
                "version": app_model.version,
                "application_identifier": app_model.application_identifier,
                "created_at": app_model.created_at.to_datetime_string(),
                "updated_at": app_model.updated_at.to_datetime_string()

            }

        apps = Applications.all().all()
        rows = [decompose(x) for x in apps]

        headings = ["app_name", "description", "developer", "version", "application_identifier", "created_at",
                    "updated_at"]
        table = PrettyTable(headings)
        for row in rows:
            table.add_row(list(row.values()))

        print(table)

    def delete(self,kwargs):

        def _delete(app,kwargs):
            app_dir = str(app.app_directory)+"/"+str(app.app_name)
            app.delete()
            if 'clean_up' in kwargs:
                shutil.rmtree(app_dir)


        if 'name' in kwargs:
            name = kwargs["name"]
            try:
                app = Applications.where('app_name','=',name).first_or_fail()
                _delete(app,kwargs)
            except ModelNotFound as e:
                print(colored(e,"red"))
                sys.exit(colored("Application with name ","red")\
                         +colored("'"+name+"'","yellow")+colored(" is not found","red"))
        elif 'id' in kwargs:
            id = kwargs["id"]
            try:
                app = Applications.where('application_identifier','=',id).first_or_fail()
                _delete(app,kwargs)
            except ModelNotFound as e:
                print(colored(e,"red"))
                sys.exit(colored("Application with id ","red")\
                         +colored("'"+str(id)+"'","yellow")+colored(" is not found","red"))
        else:
            print(colored("Please use --name or --id to choose the application to delete","yellow"))

    def register(self,kwargs):
        print(kwargs)
        if 'app_dir' in kwargs:
            to_conf ="app/Configurations/application/sego.json"
            app_dir = Path(kwargs["app_dir"])
            conf_path = app_dir / Path(to_conf)
            if os.path.exists(conf_path):
                configs = None
                with open(conf_path,"r") as f:
                    configs = json.loads(f.read())
                configs["app_directory"] = str(app_dir)
                self.db_utils.register_application(configs)

            else:
                sys.exit(colored("The application must have ","red")+colored(to_conf,"yellow")+colored(" configuration file"))
        else:
            print("Please use "+ colored("--app-dir","yellow")+" to specify app")


    def run(self, task, kwargs):
        if task.lower() in self.tasks:
            method = getattr(self, task.lower())
            method(kwargs)
