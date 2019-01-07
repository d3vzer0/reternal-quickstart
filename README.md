#  RE:TERNAL
-------------

<img src="https://i.postimg.cc/7hwhx4Dp/reternal.png" alt="Drawing" style="width: 300px;"/>

![VueJS](https://img.shields.io/badge/VueJS-2-green.svg)
![version](https://img.shields.io/badge/Version-Alpha_0.0.1-orange.svg)

---------------------

RE:TERNAL is a centralised purple team simulation platform. Reternal uses agents installed on a simulation network to execute various known
red-teaming techniques in order to test blue-teaming capabilities. The simulations are mapped to the MITRE ATT&CK framework. This repo contains
the compose file in order to set up the reternal platform via docker. An additional import script is available to create your first user
and import Mitre and Metta databases.

#### Reternal components
- **API:** https://github.com/d3vzer0/reternal-backend.git
- **UI:** https://github.com/d3vzer0/reternal-ui.git
- **Agent:** https://github.com/d3vzer0/reternal-agent.git
- **Quickstart:** https://github.com/d3vzer0/reternal-quickstart.git

#### Component installation
Reternal components are primarily aimed to be run as docker containers since the component configuration depends on environment variables set by docker-compose or the dockerfile. A docker-compose with all the default options can be found on the reternal-quickstart repository. If you don't want to run the service within containers, adjust the config.py files with your own custom values.


#### Pre-Requirements
  - docker
  - docker-compose
  - pip: mongoengine and pyyaml


#### Getting started
Rename the config.py.example file to config.py. Open the file with your favourite editor and add the required configuration values. These are your MongoDB IP address, port, and database name. Note: Authentication to mongo is strongly advised and will be enforced later. Adjust the JWT_SECRET and FLASK_SECRET variables in the docker-compose.yml to secret keys that are used for session randomization and JWT token generation. When done, simply execute 'docker-compose up -d' to run all the services. The latest version from the Development branch will be pulled and build.

#### Post-install
When the docker containers are live, create your RE:TERNAL user via the included import.py script. The following commands are available (at this monent):
  - To create a new user for the admin portal: python import.py -a create -t user
  - To import all Mitre techniques for the Mitre archive: python import.py -a import -t mitre
  - To import existing Metta commands for Agent execution: python import.py -a import -t metta

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
![alt text](https://i.postimg.cc/nrgvrNWp/technique-mapping.png)


#### Recipe builder
![alt text](https://i.postimg.cc/qRBc5snV/recipe-builder.png)

#### Interactive terminal
![alt text](https://i.postimg.cc/V679QJBS/reternal-terminal.png)


#### Task History
![alt text](https://i.postimg.cc/kMpNTtgz/task-history.png)