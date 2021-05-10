import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class CodeGenerationUtilities:

    def __init__(self):
        self.sego_home = Path.home() / ".sego"
        self.templates = self.sego_home / "templates"
        self.templates_env = Environment(loader=FileSystemLoader(self.templates))

    def generate(self, view_name, context=None):
        if context is None:
            context = {}
        return self.templates_env.get_template(view_name).render(**context)
