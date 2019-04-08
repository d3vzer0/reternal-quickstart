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
| [API](https://github.com/d3vzer0/reternal-backend)      | Administrative API to schedule tasks | ![Python](https://img.shields.io/badge/Python-3.6-green.svg) | [![Build Status](https://travis-ci.com/d3vzer0/reternal-backend.svg?branch=development)](https://travis-ci.com/d3vzer0/reternal-backend) |
| [UI](https://github.com/d3vzer0/reternal-ui)     | VueJS-based UI buildscript and NGinx webserver |![VueJS](https://img.shields.io/badge/VueJS-2-green.svg) | [![Build Status](https://travis-ci.com/d3vzer0/reternal-ui.svg?branch=development)](https://travis-ci.com/d3vzer0/reternal-ui)|
| [C2](https://github.com/d3vzer0/reternal-c2) | Seperate API endpoint that agents use to communicate with | ![Python](https://img.shields.io/badge/Python-3.6-green.svg) | [![Build Status](https://travis-ci.com/d3vzer0/reternal-c2.svg?branch=development)](https://travis-ci.com/d3vzer0/reternal-c2) |
| [Agent Compiler](https://github.com/d3vzer0/reternal-agent) | Service that compiles the agent (Golang) payloads| ![Python](https://img.shields.io/badge/Python-3.6-green.svg) ![Go](https://img.shields.io/badge/Go-1.11.4-green.svg) | [![Build Status](https://travis-ci.com/d3vzer0/reternal-agent.svg?branch=development)](https://travis-ci.com/d3vzer0/reternal-agent) |


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

#### Installation and configuration
The installation guide and configuration guide can be found on the repo's Wiki @ 
https://github.com/d3vzer0/reternal-quickstart/wiki/Install--Guide


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


#### Video showing intro to Recipe building
[VIMEO Link](https://vimeo.com/328926622)


