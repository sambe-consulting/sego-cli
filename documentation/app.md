


<p align="center"><img src="https://raw.githubusercontent.com/sambe-consulting/sego/master/sego/assets/logo.png?token=ASI6IMQLECOW25335IBSGZLAJFVMW" width="400"></p>

<p align="center"><h3 style="color: #193967; text-align: center">The command line interface for the sego framework </h3></p>

<p align="center">
<a href="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml"><img src="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml/badge.svg"></a>
<a href="https://houndci.com"><img src="https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg"></a>
<a href="https://github.com/sambe-consulting/sego-cli/blob/master/LICENSE"><img src="https://img.shields.io/github/license/apache/zookeeper"></a>


</p>


## The `app` command 
The **app** command manages application level tasks. 
### `app` Command synopsis:
```bash
sego app --task TASK <flags>
```
or 
```bash
sego app  TASK <flags>
```
The use of the **--task** argument is optional, the **app** command handles the following tasks:
1. <a href="#app-list">list</a>
2.  <a href="#app-generate">generate</a>
3.  <a href="#app-delete">delete</a>
4.  <a href="#app-register">register</a>
5.  <a href="#app-activate">activate</a>
6.  <a href="#app-describe">describe</a>



## Command tasks 
<h3 id="app-list">List Command</h3>

The **list** task lists all applications registered into **sego-cli**

### Usage 

```bash
sego app --task list 
```
or 
```bash
sego app list 
```
### Output 

```bash
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|   guitar  |                    kabelo                   |  0.1.0  | 95e75792-ea8a-42a5-a4ca-d658b63fd9ac | 2021-05-09 21:59:55 |   0    |
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@sambe.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   0    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   1    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
```

<h3 id="app-generate">Generate Command</h3>

The **generate** task generates a new application e.g: 
```bash
sego app --task generate
```
You will be prompted for:
1. **application name** : This is the name of the application, this must be unique within the same sego installation, the name is used to run further operations on the application created
2. **application description** : This is a short summary of what the application is for or what it does. 
3. **application developer**: This is the name of the developer building the application, this value will default to the system username: 
4. **application version** : This is the version of the application 
5. **application directory** : This is the directory at which the application will be installed. This value defaults to the current directory. This 
   If you move your application you must update this value.

To create a new application named `new-blog`, the following steps can be followed:

```bash
$sego app generate 
Enter application name: new-blog
Enter application description: This is my new blog
Enter application developer default (kabelo):kabelo masemola
Enter application version: 1.0.0
Enter application directory default (/home/kabelo/workspace/open_source/sego-cli):
created virtual environment CPython3.6.9.final.0-64 in 297ms
  creator CPython3Posix(dest=/home/kabelo/workspace/open_source/sego-cli/new-blog/new-blog_env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/kabelo/.local/share/virtualenv)
    added seed packages: pip==21.2.4, setuptools==57.4.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator


```
After the generation of the application code a virtual environment is created using this naming convention `` <app-name>_env``, for ``new-blog`` the environment
will be appropriately named ``new-blog_env``

After generating a sego application go <a href="app-setup.md">here</a> to see what to do next.

<h3 id="app-delete">Delete Command</h3>

The **delete** task deletes an application from sego-cli's internal database, use the **--name** or **--id** flag to specify the application in question.
This command only removes the app from the CLI but does not delete the codebase from the filesystem to delete the codebase use the **--clean-up** flag
and set it to true.

To delete an application named ``new-blog`` we can run from the CLI :

```bash
$sego app delete --name new-blog 
```
or 
```bash
$sego app delete --id 0f99edc3-0125-47ac-a5a5-a724103bcbb7 
```
To delete the same application and remove the codebase from the filesystem:
```bash
$sego app delete --name new-blog --clean-up =true 
```
or 
```bash
$sego app delete --id 0f99edc3-0125-47ac-a5a5-a724103bcbb7  --clean-up =true 
```
<h3 id="app-register">Register Command</h3>
 The **register** task, registers an application to be managed by  sego-cli the **--app-dir**
must be set to the home path of the app. This can reverse the effects of the **delete** command so long the **--clean-up** flag was not set.
To show the workings of the **register** task lets:
1. List all applications:
```bash
sego app list 
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|   guitar  |                    kabelo                   |  0.1.0  | 95e75792-ea8a-42a5-a4ca-d658b63fd9ac | 2021-05-09 21:59:55 |   0    |
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@rmb.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   1    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   0    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
```
2. Lets delete the `guitar` application 
```bash
sego app delete --name guitar  
```
3. List all the applications again; notice that `guitar` is not on the list 
```bash
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@rmb.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   1    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   0    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+ 

```
4. Register guitar 

```bash
sego app register --app-dir=guitar 
```

5. List all applications again; notice that the `guitar` application is back on the list 
```bash
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@rmb.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   1    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   0    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
|   guitar  |                    kabelo                   |  0.1.0  | 95e75792-ea8a-42a5-a4ca-d658b63fd9ac | 2021-10-02 00:32:10 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
 
```

The **register** sub-command is useful in scenarios where you have collaborators this allows everyone to be able to manage the app development locally with th sego-cli
<h3 id="app-activate">Activate Command</h3>

The **activate** task, makes an app active, sego-cli can only work on an active app, use the **--name** or **--id** to activate an app. This means to operate on 
a specific app using the CLI it has to be active. 

To illustrate how the command works lets: 
1. list all applications:

```bash
$ sego app list
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|   guitar  |                    kabelo                   |  0.1.0  | 95e75792-ea8a-42a5-a4ca-d658b63fd9ac | 2021-05-09 21:59:55 |   0    |
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@rmb.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   0    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   1    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+

```
2. Check the column labelled `active`, you will notice that all entries have the value of `0/False` and only an application named `backend` has a state of 
`1/True`. 
3. To activate an application named `demo`, we run:

```bash
sego app activate --name demo 
```
or 

```bash 
sego app activate --id 02f4e21d-1dff-494f-8d29-b9f8218a6760
```

4. list all applications: 

```bash
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|  app_name |                  developer                  | version |        application_identifier        |      created_at     | active |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+
|   guitar  |                    kabelo                   |  0.1.0  | 95e75792-ea8a-42a5-a4ca-d658b63fd9ac | 2021-05-09 21:59:55 |   0    |
|    car    |                    kabelo                   |   1.0   | d2fd5dc1-fea2-4d35-b23a-7d029b572c42 | 2021-05-09 22:35:05 |   0    |
|   portal  | kabelo masemola <kabelo.masemola@rmb.co.za> |  0.1.0  | 7307c469-1398-4b34-a6f5-f40876150d0b | 2021-05-11 00:00:20 |   0    |
|    Blog   |                    kabelo                   |  1.0.0  | 8f713dd1-318f-4635-903f-fa88f6acdd24 | 2021-07-08 14:13:49 |   0    |
|    demo   |                    kabelo                   |  1.0.0  | 02f4e21d-1dff-494f-8d29-b9f8218a6760 | 2021-07-26 14:06:17 |   1    |
|   joker   |               kabelo masemola               |  1.0.0  | 8a32ab84-a1a4-46fb-833e-9e21bd33def1 | 2021-07-30 01:18:46 |   0    |
|  medisync |                    kabelo                   |  1.0.0  | ab272f35-409e-494e-b602-b5f79529d547 | 2021-08-01 01:24:42 |   0    |
|  backend  |                    kabelo                   |  0.0.1  | 98221f8e-8117-4320-8af5-9d627914aaec | 2021-08-21 22:24:04 |   0    |
| test_sego |                    kabelo                   |         | 3abc2126-3129-4ae0-acb8-a2140a703a54 | 2021-09-03 02:07:37 |   0    |
|    exp2   |                    kabelo                   |         | 0f99edc3-0125-47ac-a5a5-a724103bcbb7 | 2021-09-22 16:54:31 |   0    |
+-----------+---------------------------------------------+---------+--------------------------------------+---------------------+--------+

```
5. Check the column labelled `active`, you will notice that all entries have the value of `0/False` and only an application named `demo` has a state of 
`1/True`. This means any operation on an application's component/subsystem will be on `demo`.

<h3 id="app-describe">Describe Command</h3>

 The **describe** task, gives configuration information for a particular application, use the **--name** or **--id** flag to specify 
 the application in question. To describe `demo`

```bash
sego app describe --name demo

                         _                                          
                      __| | ___ _ __ ___   ___                      
 _____ _____ _____   / _` |/ _ \ '_ ` _ \ / _ \   _____ _____ _____ 
|_____|_____|_____| | (_| |  __/ | | | | | (_) | |_____|_____|_____|
                     \__,_|\___|_| |_| |_|\___/                     
                                                                    

APPLICATION NAME: demo
APPLICATION DESCRIPTION: this is a demo
APPLICATION DEVELOPER: kabelo
APPLICATION SOURCE DIRECTORY: /home/kabelo/demo
APPLICATION IDENTIFIER: 02f4e21d-1dff-494f-8d29-b9f8218a6760
APPLICATION VERSION: 1.0.0
APPLICATION TYPE: 1
APPLICATION CREATION DATE: 2021-07-26T14:06:17.504282+00:00
APPLICATION ACTIVE STATUS: 1

                        _                                         
__/\____/\____/\__   __| | ___ _ __ ___   ___   __/\____/\____/\__
\    /\    /\    /  / _` |/ _ \ '_ ` _ \ / _ \  \    /\    /\    /
/_  _\/_  _\/_  _\ | (_| |  __/ | | | | | (_) | /_  _\/_  _\/_  _\
  \/    \/    \/    \__,_|\___|_| |_| |_|\___/    \/    \/    \/  
                                                                  
```


