import os

config = {
    "mongodb": {
        "database": "reternal",
        "address": "localhost",
        "port": "27017"
    },
    "mitre": {
        "url":"https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
    },
    "mapping": {
        "path": "/opt/reternal/mitre"
    }
}
