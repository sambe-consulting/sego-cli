import os, shutil,sys
from pathlib import Path
import subprocess
from termcolor import colored
from DatabaseUtilities import *
from time import sleep
import requests
from zipfile import ZipFile

class SetupUtilities:

    def __init__(self):
        self.sego_home = Path.home() / ".sego"
        self.working_dir = Path(os.getcwd())
        self.database_utilities = DatabaseUtilities()

    @staticmethod
    def setup_documentation():
        doc = "The setup command setups up the %s environment" % (colored("sego-cli", "green"))
        return doc

    def printProgressBar(self,value,label,pause_time=0):
        sleep(pause_time)
        n_bar = 40 #size of progress bar
        max = 100
        j= value/max
        sys.stdout.write('\r')
        bar = '█' * int(n_bar * j)
        bar = bar + '-' * int(n_bar * (1-j))

        sys.stdout.write(f"{label.ljust(10)} | [{bar:{n_bar}s}] {int(100 * j)}% ")
        sys.stdout.flush()
        sys.stdout.flush()

    def clean_up(self):
        if os.path.exists(self.sego_home):
            shutil.rmtree(self.sego_home)

    def set_home(self):
        if not os.path.exists(self.sego_home):
            os.mkdir(self.sego_home)

    def get_home_dir(self):
        return self.sego_home

    def setup_database(self):
        self.database_utilities.setup()

    def setup_dependencies(self):
        deps_file = "https://raw.githubusercontent.com/sambe-consulting/sego-cli/master/requirements.txt"
        self.installer(deps_file,True)

    def setup_templates(self):
        template_files = "https://codeload.github.com/sambe-consulting/sego-cli/zip/refs/heads/master"

        r = requests.get(template_files, allow_redirects=True)
        download_dir = self.sego_home / "template_master"
        extract_dir = self.sego_home/"extract"
        old_templates = extract_dir / "sego-cli-master/templates"

        with open(download_dir, "wb") as f:
            f.write(r.content)

        with ZipFile(download_dir, 'r') as zipObj:
            zipObj.extractall(path=extract_dir)

        os.remove(str(download_dir))
        templates_dir = self.sego_home / "templates"
        try:
            shutil.rmtree(templates_dir)
            os.rename(old_templates,templates_dir)
        except:
            pass
        shutil.rmtree(str(extract_dir))



    def setup(self):
        self.printProgressBar(10,"Initializing process",1)
        self.printProgressBar(20,"Setting up Sego cli home directory ~/.sego",2)
        self.set_home()
        self.printProgressBar(40,"Home directory created ",4)
        self.printProgressBar(50,"Initializing dependency installation",2)
        self.printProgressBar(50,"Installing dependencies",3)
        self.setup_dependencies()
        self.printProgressBar(70,"All dependencies have been installed",3)
        self.printProgressBar(80,"Initializing database setup",2)
        self.setup_database()
        self.printProgressBar(90,"Database setup complete",1)
        self.printProgressBar(91,"Install generator templates",1)
        self.setup_templates()
        self.printProgressBar(100,"Templates successfully installed")

    def installer(self,package,req_file=False):
        if req_file:
            subprocess.check_call([sys.executable, "-m", "pip", "install","-r", package])
        else:
             subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def virtualenv(self,name,directory):

        current_working_dir=os.getcwd()
        os.chdir(directory)
        subprocess.check_call(["python","-m","virtualenv",name,"--python","python3"])
        os.chdir(current_working_dir)
