from operations import MitreCommand, Mitre
from generic import FindFiles
from config import config
import glob
import os
import yaml

class ImportMetta:
    def update():
        metta_files = FindFiles.extension(config['metta']['path'], ".yml")
        for config_file in metta_files:
            with open(config_file) as yamlfile:
                yaml_object = yaml.load(yamlfile)
                try:
                    platform = yaml_object['os']
                    attack_phase = yaml_object['meta']['mitre_attack_phase']
                    technique = yaml_object['meta']['mitre_attack_technique']
                    commands = yaml_object['meta']['purple_actions']
                    mitre_link = yaml_object['meta']['mitre_link']
                    mitre_technique_id = mitre_link.split('/')[-1]
                    metta_id = yaml_object['uuid']

                    platform_mapping = {
                        "windows":"Windows",
                        "linux":"Linux",
                        "osx":"macOS"
                    }
                
                    mitre_object_id = Mitre.get(mitre_technique_id)
                    mitre_commands = []
                    for key, value in commands.items():
                        technique_input  = value.replace('cmd.exe /c', '').strip()
                        mitre_commands.append({"type":mitre_object_id['data'], "name":"exec_shell", "input":technique_input, "sleep":1})

                    task_object = MitreCommand.create(mitre_object_id['data'], platform_mapping[platform], mitre_commands, metta_id, mitre_technique_id, attack_phase)


                except Exception as err:
                    pass

