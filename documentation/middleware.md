


<p align="center"><img src="https://raw.githubusercontent.com/sambe-consulting/sego/master/sego/assets/logo.png?token=ASI6IMQLECOW25335IBSGZLAJFVMW" width="400"></p>

<p align="center"><h3 style="color: #193967; text-align: center">The command line interface for the sego framework </h3></p>

<p align="center">
<a href="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml"><img src="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml/badge.svg"></a>
<a href="https://houndci.com"><img src="https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg"></a>
<a href="https://github.com/sambe-consulting/sego-cli/blob/master/LICENSE"><img src="https://img.shields.io/github/license/apache/zookeeper"></a>


</p>


## The `middleware` command 
The **middleware** command manages middleware related tasks. This command operates only on the currently active application.
### `middleware` Command synopsis:
```bash
sego middleware --task TASK <flags>
```

or 
```bash
sego middleware TASK <flags>
```
The use of the **--task** argument is optional, the **middleware** command handles the following tasks:
1. <a href="#middleware-list">list</a>
2.  <a href="#middleware-generate">generate</a>
3.  <a href="#middleware-delete">delete</a>


## Command tasks 
<h3 id="middleware-list">List Command</h3>

The **list** task lists all middleware for the active application. To list all middleware of an application named `demo`
1. <a href="https://github.com/sambe-consulting/sego-cli/blob/docs/documentation/app.md#app-activate" >Activate the application</a>
2. Run the list command: 
```bash
 sego middleware list 
```
or 
```bash
 sego middleware --task list 
```

### Output 

```bash
********************************************************************************
     _                       
  __| | ___ _ __ ___   ___   
 / _` |/ _ \ '_ ` _ \ / _ \  
| (_| |  __/ | | | | | (_) | 
 \__,_|\___|_| |_| |_|\___/  
                             
  __  __ ___ ____  ____  _     _______        ___    ____  _____  
|  \/  |_ _|  _ \|  _ \| |   | ____\ \      / / \  |  _ \| ____| 
| |\/| || || | | | | | | |   |  _|  \ \ /\ / / _ \ | |_) |  _|   
| |  | || || |_| | |_| | |___| |___  \ V  V / ___ \|  _ <| |___  
|_|  |_|___|____/|____/|_____|_____|  \_/\_/_/   \_\_| \_\_____| 
                                                                 

================================================================================
MIDDLEWARE NAME:  AuthMiddleware
--- PROCESSOR NAME:   __init__
--- PROCESSOR NAME:   process_request
--- --- --- ARGUMENT NAME:   request
--- PROCESSOR NAME:   process_response
--- --- --- ARGUMENT NAME:   request
--- --- --- ARGUMENT NAME:   response
================================================================================
MIDDLEWARE NAME:  ExampleMiddleware
--- PROCESSOR NAME:   __init__
--- PROCESSOR NAME:   process_request
--- --- --- ARGUMENT NAME:   request
--- PROCESSOR NAME:   process_response
--- --- --- ARGUMENT NAME:   request
--- --- --- ARGUMENT NAME:   response
================================================================================


********************************************************************************


```
The `demo` application has two middleware namely **AuthMiddleware** and **ExampleMiddleware**. This command also lists the processors (functions) that each 
middleware has and each argument the processor accepts.

<h3 id="middleware-generate">Generate Command</h3>

The **generate** task generates a new middleware for the active application. 
```bash
 sego middleware generate
```
You will be prompted for:
1. **middleware name**
2. **description**
3. **developer name** (defaults to system username)
4. **developer email** 
5. **middleware version**

```bash
sego controller generate

Please enter middleware name e.g AuthMiddleware : AuthMiddleware
Please enter a short description of the middleware:This middleare manages auth sessions
Enter middleware author default (kabelo):kabelo masemola
Enter the email address of the author/maintainer: kabelo.masemola@sambe.co.za
Enter the version of this middleware: 1.0.0
# ************************************************************************#
# Title:                    AuthMiddleware                                #
# Description:              This middleare manages auth sessions          #
# Author:                   kabelo masemola <kabelo.masemola@sambe.co.za> #
# Original Date:            06/10/2021 01:49:51                           #
# Version:                  1.0.0                                         #
# ************************************************************************

from sego.Middleware.Middleware import Middleware
from sego.Middleware.MiddlewareManager import MiddlewareManager
from flask import request
class AuthMiddleware(Middleware):

      def __init__(self):
          pass

      def process_request(self, request):
          print("Processing request", request.url)

      def process_response(self, request, response):
          print("Processing response", request.url)


```

The `AuthMiddleware` will be saved in a file named `AuthMiddleware.py` in ` <app_dir>/app/Middleware` 


<h3 id="middleware-delete">Delete Command</h3>

The **delete** task deletes a middleware for the active application. 

```bash
 sego controller delete --name AuthMiddleware
```
