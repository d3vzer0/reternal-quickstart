from cli.imports import Mapping
from cli.imports import ImportMitre
from cli.imports import ImportUser
from cli.imports import ImportCommand
from cli.imports import Install
from cli.operations import Compose
import argparse, getpass, yaml


function_mapping = {
    "mitre": {
        "import":ImportMitre().update
    },
    "mapping": {
        "import":Mapping().update
    },
    "user":{
        "create":ImportUser().create
    },
    "command":{
        "create": ImportCommand().create
    },
    "compose": {
        "update": Compose().update
    },
    "all": {
        "install": Install().all
    }
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", help="Action to perform: delete||import||create", required=True)
    parser.add_argument("-t", "--type", help="Action to perform: mitre||metta||user", required=True)
    args = parser.parse_args()
    try:
        result = function_mapping[args.type][args.action]()
    except KeyError as error:
        result = {"result":"failed", "data":"Invalid option, use --help for an overview of types and options"}
    print(result)

