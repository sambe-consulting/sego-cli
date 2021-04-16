
#***********************************************************************************#
# Title:             Database Utilities                                             #
# Description:       This code is for sego_cli Database Utilities                   #
# Author:            Pfarelo Raliphada                                              #
# Date:              16 April 2021                                                  #
#***********************************************************************************#


import os
import sqlite3
from pathlib import Path
from sqlite3 import Error

from orator import DatabaseManager, Schema
from orator import Model

from models.application import Applications


class DatabaseUtilities:
"""DatabaseUtilities class represents and manipulates sego_home, database and config"""
        conn = None
    def __init__(self):
     """ Create a new point at the origin """
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

    def create_applications_table(self):
    """ create a table applications to a SQLite database """
        conn = None
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
    """  provides some simple utilities to make it easy to create pluggable applications """
        conn = None
        with self.schema.connection('sqlite').create('plugins') as table:
            table.increments('id')
        with self.schema.table('plugins') as table:
            table.string("name")
            table.string("description")
            table.string("version")

    def register_application(self, app_data):
    """ registers the table application to a SQLite database """
        conn = None
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
    """ lists the table application to a SQLite database """
        conn = None
        return Applications.all()

    def setup(self):
    """ sets up connection, applicton table and plugins table to a SQLite database """
        conn = None
        if not os.path.exists(self.database):
            self.create_connection(str(self.database))
            self.create_applications_table()
            self.create_plugins_table()






















































#***********************************************************************************#
# Title:             Database Utilities                                             #
# Description:       This code is for sego_cli Database Utilities                   #
# Author:            Pfarelo Raliphada                                              #
# Date:              16 April 2021                                                  #
#***********************************************************************************#


import os
import sqlite3
from pathlib import Path
from sqlite3 import Error

from orator import DatabaseManager, Schema
from orator import Model

from models.application import Applications


class DatabaseUtilities:
"""DatabaseUtilities class represents and manipulates sego_home, database and config"""
        conn = None
    def __init__(self):
     """ Create a new point at the origin """
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

    def create_applications_table(self):
    """ create a table applications to a SQLite database """
        conn = None
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
    """  provides some simple utilities to make it easy to create pluggable applications """
        conn = None
        with self.schema.connection('sqlite').create('plugins') as table:
            table.increments('id')
        with self.schema.table('plugins') as table:
            table.string("name")
            table.string("description")
            table.string("version")

    def register_application(self, app_data):
    """ registers the table application to a SQLite database """
        conn = None
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
    """ lists the table application to a SQLite database """
        conn = None
        return Applications.all()

    def setup(self):
    """ sets up connection, applicton and  to a SQLite database """
        conn = None
        if not os.path.exists(self.database):
            self.create_connection(str(self.database))
            self.create_applications_table()
            self.create_plugins_table()
    def create_plugins_table(self):
        with self.schema.connection('sqlite').create('plugins') as table:
            table.increments('id')
        with self.schema.table('plugins') as table:
            table.string("name")
            table.string("description")
            table.string("version")

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
        if not os.path.exists(self.database):
            self.create_connection(str(self.database))
            self.create_applications_table()
            self.create_plugins_table()
