


<p align="center"><img src="https://raw.githubusercontent.com/sambe-consulting/sego/master/sego/assets/logo.png?token=ASI6IMQLECOW25335IBSGZLAJFVMW" width="400"></p>

<p align="center"><h3 style="color: #193967; text-align: center">The command line interface for the sego framework </h3></p>

<p align="center">
<a href="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml"><img src="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml/badge.svg"></a>
<a href="https://houndci.com"><img src="https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg"></a>
<a href="https://github.com/sambe-consulting/sego-cli/blob/master/LICENSE"><img src="https://img.shields.io/github/license/apache/zookeeper"></a>


</p>


## The `controller` command 
The **controller** command manages controller level tasks. This command operates only on the currently active application.
### `controller` Command synopsis:
```bash
sego controller --task TASK <flags>
```
or 
```bash
sego controller  TASK <flags>
```
The use of the **--task** argument is optional, the **controller** command handles the following tasks:

1. <a href="#controller-list">list</a>
2.  <a href="#controller-generate">generate</a>
3.  <a href="#controller-delete">delete</a>

## Command tasks 
<h3 id="controller-list">List Command</h3>

The **list** task lists all controllers for the active application. To list all controllers of an application named `demo`
1. <a href="https://github.com/sambe-consulting/sego-cli/blob/docs/documentation/app.md#app-activate" >Activate the application</a>
2. Run the list command: 
```bash
 sego controller list 
```
or 
```bash
 sego controller --task list 
```

### Output 

```bash
********************************************************************************
     _                       
  __| | ___ _ __ ___   ___   
 / _` |/ _ \ '_ ` _ \ / _ \  
| (_| |  __/ | | | | | (_) | 
 \__,_|\___|_| |_| |_|\___/  
                             
  ____ ___  _   _ _____ ____   ___  _     _     _____ ____  ____   
 / ___/ _ \| \ | |_   _|  _ \ / _ \| |   | |   | ____|  _ \/ ___|  
| |  | | | |  \| | | | | |_) | | | | |   | |   |  _| | |_) \___ \  
| |__| |_| | |\  | | | |  _ <| |_| | |___| |___| |___|  _ < ___) | 
 \____\___/|_| \_| |_| |_| \_\\___/|_____|_____|_____|_| \_\____/  
                                                                   

================================================================================
CONTROLLER NAME:  HomeController
--- ACTION NAME:   index
--- --- --- ARGUMENT NAME:   request
--- --- --- ARGUMENT NAME:   response
================================================================================
CONTROLLER NAME:  ProjectController
--- ACTION NAME:   __init__
--- ACTION NAME:   create
--- --- --- ARGUMENT NAME:   project_name
--- --- --- ARGUMENT NAME:   owner
--- --- --- ARGUMENT NAME:   type
--- ACTION NAME:   delete
--- ACTION NAME:   index
--- --- --- ARGUMENT NAME:   request
--- --- --- ARGUMENT NAME:   response
================================================================================


********************************************************************************

```
The `demo` application has two controllers namely **HomeController** and **ProjectController**. This command also lists the actions (functions) that each 
controller has and each argument the action accepts.

<h3 id="controller-generate">Generate Command</h3>

The **generate** task generates a new controller for the active application. 
```bash
 sego controller generate
```
You will be prompted for:
1. **controller name**
2. **description**
3. **developer name** (defaults to system username)
4. **developer email** 
5. **controller version**

```bash
sego controller generate

Please enter controller name e.g HomeController : PluginController
Please enter a short description of the controller:This controller will manage the plugin interface
Enter controller author default (kabelo):kabelo masemola
Enter the email address of the author/maintainer: kabelo.masemola@sambe.co.za
Enter the version of this controller: 1.0.0
# ************************************************************************#
# Title:                    PluginController                          #
# Description:              This controller will manage the plugin interface                    #
# Author:                   kabelo masemola <kabelo.masemola@sambe.co.za>                 #
# Original Date:            02/10/2021 01:44:40                           #
# Version:                  1.0.0                                   #
# ************************************************************************#
from . import BaseController

class PluginController(BaseController):

      def __init__(self):
          pass

      def index(self, request, response):
         return self.Views.render_view("home.html")

```

The `PluginController` will be saved in a file named `PluginController.py` in ` <app_dir>/app/Controllers` 


<h3 id="controller-delete">Delete Command</h3>

The **delete** task deletes a controller for the active application. 

```bash
 sego controller delete --name PluginController
```
