


<p align="center"><img src="https://raw.githubusercontent.com/sambe-consulting/sego/master/sego/assets/logo.png?token=ASI6IMQLECOW25335IBSGZLAJFVMW" width="400"></p>

<p align="center"><h3 style="color: #193967; text-align: center">The command line interface for the sego framework </h3></p>

<p align="center">
<a href="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml"><img src="https://github.com/sambe-consulting/sego-cli/actions/workflows/sego-cli-build.yml/badge.svg"></a>
<a href="https://houndci.com"><img src="https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg"></a>
<a href="https://github.com/sambe-consulting/sego-cli/blob/master/LICENSE"><img src="https://img.shields.io/github/license/apache/zookeeper"></a>


</p>


## Installation instructions 

### Windows
1. Set version number, go <a href="https://github.com/sambe-consulting/sego-cli/releases">here<a/> for all available versions e.g for `v5`
```bash 
SET SEGO_VERSION=v5  
```
To set the latest version run (recommended):

```bash
SET SEGO_URL="https://api.github.com/repos/sambe-consulting/sego-cli/releases/latest"
curl --silent %SEGO_URL%|findstr tag_name > temp.txt && SET /P temp_var=<temp.txt
SET temp_var=%temp_var: =% 
SET temp_var=%temp_var:"tag_name":"=% 
SET temp_var=%temp_var:",=% 
SET SEGO_VERSION=%temp_var: =%
```
2. Download the CLI:
```bash
curl https://github.com/sambe-consulting/sego-cli/releases/download/%SEGO_VERSION%/sego -Lo sego.py
```
3. Create a batch file
- Open a text editor 
- Add the following code
```bash
@echo off 

"python" "C:\<path where sego.py is saved>\sego.py" %*
 
```
e.g 

```bash
@echo off 

"python" "C:\Users\Kabelo\sego.py"

```

- Save the batch file in `C:\Windows\System32` as `sego.bat`

4. Setup the environment :
```bash
 sego --install 
```
5. Test the CLI :
```bash
 sego --help  
```
If successfully installed the following output will appear:
```bash
NAME
    sego - Sego command line interface version: 0.1.0.0

SYNOPSIS
    sego -

DESCRIPTION
    Sego command line interface version: 0.1.0.0


```
### Linux
1. Set version number, go <a href="https://github.com/sambe-consulting/sego-cli/releases">here<a/> for all available versions e.g for `v5`
```bash 
export SEGO_VERSION=v5  
```
To set the latest version run (recommended):

```bash
export SEGO_VERSION=$(curl --silent "https://api.github.com/repos/sambe-consulting/sego-cli/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
```
2. Download the CLI:
```bash
curl https://github.com/sambe-consulting/sego-cli/releases/download/${SEGO_VERSION}/sego -Lo sego
```
3. Make the CLI executable:

```bash
sudo chmod +x sego 
```

4. Move the CLI to the bin directory

```bash
sudo mv sego /usr/local/bin/sego 
```

5. Setup the environment :
```bash
 sego --install 
```
6. Test the CLI :
```bash
 sego --help  
```
If successfully installed the following output will appear:
```bash
NAME
    sego - Sego command line interface version: 0.1.0.0

SYNOPSIS
    sego -

DESCRIPTION
    Sego command line interface version: 0.1.0.0


```
### Mac-OS
1. Set version number, go <a href="https://github.com/sambe-consulting/sego-cli/releases">here<a/> for all available versions e.g for `v5`
```bash 
export SEGO_VERSION=v5  
```
To set the latest version run (recommended):

```bash
export SEGO_VERSION=$(curl --silent "https://api.github.com/repos/sambe-consulting/sego-cli/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
```
2. Download the CLI:
```bash
curl https://github.com/sambe-consulting/sego-cli/releases/download/${SEGO_VERSION}/sego -Lo sego
```
3. Make the CLI executable:

```bash
sudo chmod +x sego 
```

4. Move the CLI to the bin directory

```bash
sudo mv sego /usr/local/bin/sego 
```

5. Setup the environment :
```bash
 sego --install 
```
6. Test the CLI :
```bash
 sego --help  
```
If successfully installed the following output will appear:
```bash
NAME
    sego - Sego command line interface version: 0.1.0.0

SYNOPSIS
    sego -

DESCRIPTION
    Sego command line interface version: 0.1.0.0


```

