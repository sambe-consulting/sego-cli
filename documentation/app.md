


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





<h3 id="app-list">List Command</h3>
<h3 id="app-list">List Command</h3>
<h3 id="app-list">List Command</h3>
<h3 id="app-list">List Command</h3>
