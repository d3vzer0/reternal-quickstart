from operations import MitreCommand
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
                    category = yaml_object['meta']['mitre_attack_phase']
                    technique = yaml_object['meta']['mitre_attack_technique']
                    commands = yaml_object['meta']['purple_actions']
                    platform_mapping = {
                        "windows":"Windows",
                        "linux":"Linux",
                        "osx":"macOS"
                    }

                    for key, value in commands.items():
                        technique_input  = value.replace('cmd.exe /c', '').strip()
                        task_object = MitreCommand.create(config['metta']['exec'], technique_input, 0)


                except Exception as err:
                    pass

