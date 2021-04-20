import os
import sqlite3
from pathlib import Path
from sqlite3 import Error
import sys, shutil
from orator import DatabaseManager, Schema
from orator import Model

from models.application import Applications
from models.targets import Targets


class DatabaseUtilities:

    def __init__(self):

        self.sego_home = Path.home() / ".sego"
        self.database = self.sego_home / "sego_database.db"
        self.config = {
            'sqlite': {
                'driver': 'sqlite',
                'database': str(self.database),
                'prefix': '',

            }
        }
        self.db = DatabaseManager(self.config)
        self.schema = Schema(self.db)
        Model.set_connection_resolver(self.db)

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def get_database_path(self):
        return self.database

    def create_applications_table(self):
        with self.schema.connection('sqlite').create('applications') as table:
            table.increments('id')

        with self.schema.table('applications') as table:
            table.string('app_name').nullable()
            table.string('description').nullable()
            table.string('developer').nullable()
            table.string('version').nullable()
            table.string('app_directory').nullable()
            table.string("application_identifier").nullable()
            table.big_integer('application_type').nullable()
            table.timestamp("created_at").nullable()
            table.timestamp("updated_at").nullable()

    def create_plugins_table(self):
        with self.schema.connection('sqlite').create('plugins') as table:
            table.increments('id')

        with self.schema.table('plugins') as table:
            table.string("name").nullable()
            table.string("description").nullable()
            table.string("version").nullable()

    def create_targets_table(self):
        with self.schema.connection('sqlite').create('targets') as table:
            table.increments('id')

        with self.schema.table('targets') as table:
            table.string('target').nullable()
            table.string('description').nullable()
            table.string('list_action').nullable()
            table.string('generate_action').nullable()
            table.timestamp("created_at").nullable()
            table.timestamp("updated_at").nullable()

    def register_targets(self):
        target = Targets()
        target.target = "Routes"
        target.description = "This generator target manages application routes"
        target.save()
        target = Targets()
        target.target = "Controllers"
        target.description = "This generator target manages application controllers"
        target.save()
        target = Targets()
        target.target = "Applications"
        target.description = "This generator target manages applications"
        target.save()

    def register_application(self, app_data):
        new_app = Applications()
        new_app.app_name = app_data["app_name"]
        new_app.description = app_data["description"]
        new_app.developer = app_data["developer"]
        new_app.version = app_data["version"]
        new_app.app_directory = app_data["app_directory"]
        new_app.application_identifier = app_data["application_identifier"]
        new_app.application_type = 1
        new_app.save()

    def list_applications(self):
        return Applications.all()

    def setup(self):

        self.create_connection(str(self.database))
        self.create_applications_table()
        self.create_plugins_table()
        self.create_targets_table()
        self.register_targets()
