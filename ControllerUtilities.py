from termcolor import colored

class ControllerUtilities:
    def __init__(self):
        self.tasks = ["list", "generate", "delete"]

    def get_controller_doc(self):
        doc = "The "+colored("controller", "green")+" command manages controller level tasks." \
              " set the "+colored("--task","yellow" )+" argument to %s|%s|%s"%(colored("list","blue"),colored("generate","blue"),colored("delete","blue"))
        doc = doc + "\n\n The " + colored("list","blue") + " task lists all controllers for the active application "
        doc = doc + "\n\n The " + colored("generate","blue") + " task generates a new controller for the active application "
        doc = doc + "\n\n The " + colored("delete","blue") + " task deletes a controller for the active application "
        return doc

    def list(self,kwargs):
        pass

    def generate(self,kwargs):
        pass

    def delete(self,kwargs):
        pass

    def run(self,task,kwargs):
        if task.lower() in self.tasks:
            method = getattr(self, task.lower())
            method(kwargs)
