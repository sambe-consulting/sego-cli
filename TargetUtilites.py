import os,json
from pathlib import Path
from models.targets import Targets
from SetupUtilities import SetupUtilities


class TargetUtilities:
    def __init__(self):
        self.setup_utilities = SetupUtilities()
        self.working_dir = Path(os.getcwd())
        try:
            self.all_targets = Targets.all().all()
        except Exception:
            self.setup_utilities.setup()
            self.all_targets= []

    def get_targets(self):
        return self.all_targets

    def get_target_names(self):
        names = [x.target for x in self.all_targets]
        return names


