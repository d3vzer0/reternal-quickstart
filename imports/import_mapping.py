from operations import MapCommand, Mitre
from generic import FindFiles
from config import config
import glob
import os
import yaml


class Mapping:
    def update(self):
        metta_files = FindFiles.extension(config['mapping']['path'], ".yml")
        for config_file in metta_files:
            with open(config_file) as yamlfile:
                yaml_object = yaml.load(yamlfile)
                try:
                    name = yaml_object['name']
                    platform = yaml_object['mitre_technique']['platform']
                    reference = yaml_object.get('reference', None)
                    description = yaml_object.get('description', None)
                    author = yaml_object.get('author', None)
                    technique = yaml_object['mitre_technique']['id']
                    commands = yaml_object['commands']
                    mitre_object = Mitre().get(technique)['data']
                    all_commands = []
                    for command in commands:
                        all_commands.append({"type":"Mitre", "name":command["type"], "input":command["input"], "sleep":command["sleep"]})

                    for phase in mitre_object['kill_chain_phases']:
                        map_result = MapCommand(name).create(mitre_object['technique_id'], mitre_object['name'], technique, phase, platform, all_commands, reference, author, description)

                except Exception as err:
                    pass

        return {'result':'success', 'message':'Finished loading mapped techniques'}

            


