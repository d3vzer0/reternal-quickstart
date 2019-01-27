from cli.generic import Random
import oyaml as yaml


class Compose:
    def __init__(self, path="./docker-compose.yml"):
        self.path = path

    def update(self):
        with open(self.path) as yaml_input:
            compose_settings = yaml.load(yaml_input)

        compose_settings['services']['api']['environment']['JWT_SECRET'] = Random(25).create()
        compose_settings['services']['api']['environment']['FLASK_SECRET'] = Random(25).create()
        compose_settings['services']['api-socket']['environment']['JWT_SECRET'] = Random(25).create()
        compose_settings['services']['api-socket']['environment']['FLASK_SECRET'] = Random(25).create()
        compose_settings['services']['c2']['environment']['C2_SECRET'] = Random(25).create()

        with open(self.path ,'w') as yaml_output:
            yaml.dump(compose_settings, yaml_output, default_flow_style=False)

        result = {"result":"success", "message":"Succesfully created random keys for webservice and C2 endpoint"}
        return result
