
import glob
import yaml
import asyncio
import aiohttp
from environment import config
from reternalapi import ReternalAPI

class Technique:
    def __init__(self, technique = None):
        self.technique = technique

    @property
    def parsed_reternal(self):
        return {
            'name': self.technique['name'], 
            'platform': self.technique['mitre_technique']['platform'],
            'reference': self.technique.get('reference', None), 
            'description': self.technique.get('description', None),
            'author': self.technique.get('author', None),
            'integration': self.technique['integration'],
            'external_id': self.technique['mitre_technique']['id'],
            'commands': [{"category":"Mitre", "module": command["module"], "input":command["input"],
                "sleep":command["sleep"], 'integration': self.technique['integration'] } for command in self.technique['commands']],
            'external_id': self.technique['mitre_technique']['id'],
        }


class Techniques:
    def __init__(self, techniques = None):
       self.techniques = techniques if techniques else []

    @staticmethod
    def __parse_technique_file(technique_path):
        with open(technique_path) as yamlfile:
            yaml_object = yaml.load(yamlfile, Loader=yaml.FullLoader)
            technique = Technique(yaml_object)
            return technique.parsed_reternal

    @classmethod
    def from_path(cls, path = '../mitre/techniques'):
        ''' Find all technique config files '''
        technique_files = glob.iglob(f'{path}/**/*.yml', recursive=True)
        techniques = [cls.__parse_technique_file(technique) for technique in technique_files]
        return cls(techniques)


async def import_techniques(*args, **kwargs):
    ''' Load all config files and import mapped techniques '''
    techniques = Techniques.from_path(config['TECHNIQUES_PATH'])
    async with ReternalAPI(api_url=config['API_URL']) as reternal:
        for technique in techniques.techniques:
            await reternal.save('/mapping', technique)

if __name__ == "__main__":
    asyncio.run(import_techniques())
