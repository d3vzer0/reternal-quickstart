from cli.operations import MapCommand, Mitre
from cli.generic import FindFiles
from cli.config import config
import glob
import os
import yaml


class Mapping:
    def __init__(self, file_path=config['mapping']['path'], extension='.yml'):
        self.file_path = file_path
        self.extension = extension

    def update(self):
        metta_files = FindFiles.extension(self.file_path, self.extension)
        for config_file in metta_files:
            with open(config_file) as yamlfile:
                yaml_object = yaml.load(yamlfile)
                try:
                    mapping_data = {
                        'name': yaml_object['name'],
                        'platform': yaml_object['mitre_technique']['platform'],
                        'reference': yaml_object.get('reference', None),
                        'description': yaml_object.get('description', None),
                        'author': yaml_object.get('author', None),
                        'technique': yaml_object['mitre_technique']['id'],
                        'commands': yaml_object['commands'],
                        'external_id': yaml_object['mitre_technique']['id']}

                    technique_object = Mitre('external_id').technique(mapping_data['external_id'])['data']
                    all_commands = [{"type":"Mitre", "name":command["type"], "input":command["input"],
                        "sleep":command["sleep"]} for command in mapping_data['commands']]

                    for phase in technique_object['kill_chain_phases']:
                        map_result = MapCommand(mapping_data['name']).create(technique_object, mapping_data, all_commands, phase)

                except Exception as err:
                    pass

        return {'result':'success', 'message':'Finished loading mapped techniques'}

            


