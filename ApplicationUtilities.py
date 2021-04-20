import os, json, requests, shutil
from pathlib import Path
from zipfile import ZipFile
import uuid, click
from datetime import datetime
from DatabaseUtilities import DatabaseUtilities
from SegoExceptions import *
from termcolor import colored
from models.application import Applications
from prettytable import PrettyTable


class ApplicationUtilities:
    def __init__(self):
        self.app_template_url = "https://codeload.github.com/sambe-consulting/sego-app/zip/refs/heads/master"
        self.db_utils = DatabaseUtilities()

    def get_application_doc(self):
        doc = "The "+colored("application","green")+" command manages application level tasks.\n"
        doc = doc+"  use the "+colored("--task","yellow")+" argument to specify the task\n"

        return doc

    def generate_application(self, application_data):
        directory = Path(application_data["app_directory"])
        name = application_data["app_name"]
        backend_name = name + "_" + str(uuid.uuid4())
        sego_dir = Path.home() / ".sego"
        if os.path.exists(directory / name):
            raise DirectryNotEmptyException("This directory already exists")
        r = requests.get(self.app_template_url, allow_redirects=True)
        download_dir = sego_dir / backend_name

        with open(download_dir, "wb") as f:
            f.write(r.content)
        self.clean_application(download_dir, directory, name)
        self.register_application(application_data)

    def clean_application(self, zip, directry, name):
        with ZipFile(zip, 'r') as zipObj:
            zipObj.extractall(path=directry)
        os.rename(directry / "sego-app-master", directry / name)
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
        self.db_utils.register_application(application_data)

    def repl(self):
        data = {}
        data["app_name"] = click.prompt('Please application %s' % (colored('name', 'green')), type=str)
        print(os.getcwd())

    def list(self):
        def decompose(app_model):
            return {
                "app_name":app_model.app_name,
                "description":app_model.description,
                "developer":app_model.developer,
                "version":app_model.version,
                "application_identifier":app_model.application_identifier,
                "created_at":app_model.created_at.to_datetime_string(),
                "updated_at":app_model.updated_at.to_datetime_string()

            }
        apps = Applications.all().all()
        rows = [decompose(x) for x in apps]

        headings = [ "app_name","description","developer","version","application_identifier","created_at", "updated_at"]
        table = PrettyTable(headings)
        for row in rows:
           table.add_row(list(row.values()))

        print(table)

