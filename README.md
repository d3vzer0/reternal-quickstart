#  RE:TERNAL
-------------

<img src="https://i.postimg.cc/7hwhx4Dp/reternal.png" alt="Drawing" style="width: 300px;"/>

![version](https://img.shields.io/badge/Version-Alpha_0.0.1-orange.svg)



---------------------

#### Note: Still under development, only use for testing and do not expose interfaces #####

RE:TERNAL is a centralised purple team simulation platform. Reternal uses agents installed on a simulation network to execute various known
red-teaming techniques in order to test blue-teaming capabilities. The simulations are mapped to the MITRE ATT&CK framework. This repo contains
the compose file in order to set up the reternal platform via docker. An additional import script is available to create your first user
and import Mitre and Metta databases.

#### Reternal components
| Component        | Description | Code           | Build  |
| ------------- |:-------------- |:--------------| :------| 
| [API](https://github.com/d3vzer0/reternal-api)      | Administrative API to schedule tasks | ![Python](https://img.shields.io/badge/Python-3.6-green.svg) | ![Build Status](https://travis-ci.com/d3vzer0/reternal-backend.svg?branch=development) |
| [UI](https://github.com/d3vzer0/reternal-ui)     | VueJS-based UI buildscript and NGinx webserver |![VueJS](https://img.shields.io/badge/VueJS-2-green.svg) | ![Build Status](https://travis-ci.com/d3vzer0/reternal-ui.svg?branch=development)|
| [C2](https://github.com/d3vzer0/reternal-c2) | Seperate API endpoint that agents use to communicate with | ![Python](https://img.shields.io/badge/Python-3.6-green.svg) | ![Build Status](https://travis-ci.com/d3vzer0/reternal-c2.svg?branch=development) |
| [Agent Compiler](https://github.com/d3vzer0/reternal-agent) | Service that compiles the agent (Golang) payloads| ![Python](https://img.shields.io/badge/Python-3.6-green.svg) ![Go](https://img.shields.io/badge/Go-1.11.4-green.svg) | ![Build Status](https://travis-ci.com/d3vzer0/reternal-agent.svg?branch=development) |


#### Compose Status
| Component        | Description | Build  |
| ------------- |:-------------- | :------| 
| Total Stack | Build verifying entire stack via docker-compose in this repository | [![Build Status](https://travis-ci.com/d3vzer0/reternal-quickstart.svg?branch=development)](https://travis-ci.com/d3vzer0/reternal-quickstart) |



#### Additional components
| Component        | Description           | 
| ------------- |:--------------| 
| [Quickstart](https://github.com/d3vzer0/reternal-quickstart)      | Quickstart repo that contains the compose-file and management tools to create users, techniques etc |
| [Mitre](https://github.com/d3vzer0/reternal-mitre)     | Repository containing already existing mapped techniques for reternal |

<img src="https://i.postimg.cc/15nGCgws/Untitled-Diagram-3.png" alt="Drawing" style="width: 600px;"/>


#### Component installation
Reternal components are primarily aimed to be run as docker containers since the component configuration depends on environment variables set by docker-compose or the dockerfile. A docker-compose with all the default options can be found in this repository.

#### Pre-Requirements
  - docker
  - docker-compose
  - python3
  - pip (3)

#### Getting started
- **Clone the quickstart repo to your system:** `git clone https://github.com/d3vzer0/reternal-quickstart`
- **Clone the reternal-mitre repo containing pre-defined simulations:** `git clone https://github.com/d3vzer0/reternal-mitre`
- **Navigate to the reternal-quickstart directory:** `cd reternal-quickstart`
- **Install pip dependencies:** `pip3 install requirements.txt`
- **Create unique keys for JWT and Session tokens:** `python manage.py -a update -t compose`

When done, execute '`docker-compose up -d --build`' to run all the services. The latest version from the Development branch will be pulled and build.

#### Post-setup
The quickstart repo contains a management script called 'manage.py'. You can use this script to create your first user and import already existing techniques. 

- **Configure all variables and create first user:** `python manage.py -a install -t all`

You can now open a browser of choice and navigate to http://localhost. Use the credentials you just created via the manage.py script.

##### Individual options
- **Create user:** `python import.py -a create -t user`
- **Import Mitre DB:** `python import.py -a import -t mitre`
- **Import Techniques:** `python import.py -a import -t mapping`
- **Create Default commands:** `python import.py -a create -t ccommand`


#### Feature Requests & Bugs
We use the Github to manage Feature requests and Bug reports.

#### Developers and Contact

Joey Dreijer < joeydreijer@gmail.com >  
Yaleesa Borgman < yaleesa@gmail.com >

#### Whats up with the name?

This project has been re-developed so many times, it will probably never really finish. Hence RE (Redo) and Ternal (Eternal).

#### Special Thanks
  - MITRE ATT&CK - Framework used for mapping simulations: https://attack.mitre.org/wiki/Main_Page
  - Uber Metta -  Using Metta's templates for MITRE techniques with small (optional) adjustments to the purple_action format: https://github.com/uber-common/metta


### Screenshots
#### Technique mapping
![alt text](https://i.postimg.cc/PqCFxBVZ/mapping.png)

#### Recipe builder
![alt text](https://i.postimg.cc/Xvt1yQtP/recipes.png)

#### Interactive terminal
![alt text](https://i.postimg.cc/V679QJBS/reternal-terminal.png)

#### Screenshot galery from agents
![alt text](https://i.postimg.cc/JnJ63jLz/output.png)

#### Agents overview
![alt text](https://i.postimg.cc/zGtcqJ78/agents.png)

##### Included MITRE DB for details
![alt text](https://i.postimg.cc/QC36fV8k/mitredetails.png)

