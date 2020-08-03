
from .environment import config
import glob
import yaml
import asyncio
import aiohttp

class Techniques:
    def __init__(self, path=config['TECHNIQUES_PATH'], api_url=config['API_URL']):
        self.path = path
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) #todo fix trusting custom ca
        self.api_url = api_url

    async def import_config(self, mapping):
        ''' Create mapping via Reternal API '''
        async with self.session.post(f'{self.api_url}/mapping', json=mapping) as resp:
            if not resp.status == 200:
                error_message = await resp.json()
                print(error_message)


    def load_config(self):
        ''' Find all technique config files '''
        config_files = glob.iglob(f'{self.path}/**/*.yml', recursive=True)
        for config in config_files:
            with open(config) as yamlfile:
                yaml_object = yaml.load(yamlfile, Loader=yaml.FullLoader)
                mapping_data = {
                    'name': yaml_object['name'], 'platform': yaml_object['mitre_technique']['platform'],
                    'reference': yaml_object.get('reference', None), 'description': yaml_object.get('description', None),
                    'author': yaml_object.get('author', None),
                    'integration': yaml_object['integration'],
                    'external_id': yaml_object['mitre_technique']['id'],
                    'commands': [{"category":"Mitre", "module": command["module"], "input":command["input"],
                        "sleep":command["sleep"], 'integration': yaml_object['integration'] } for command in yaml_object['commands']],
                    'external_id': yaml_object['mitre_technique']['id'],
                }
                yield mapping_data
          
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        ''' Close aiothttp session '''
        await self.session.close()


async def import_techniques(*args, **kwargs):
    ''' Load all config files and import mapped techniques '''
    async with Techniques(**kwargs) as tasks:
        for config in tasks.load_config():
            await tasks.import_config(config)

if __name__ == "__main__":
    asyncio.run(import_techniques())
