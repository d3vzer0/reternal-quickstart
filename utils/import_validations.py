
from environment import config
import glob
import yaml
import asyncio
import aiohttp

class Validations:
    def __init__(self, file_path=config['VALIDATIONS_PATH'], api_url=config['API_URL']):
        self.file_path = file_path
        self.api_url = api_url
        self.session = aiohttp.ClientSession()

    async def import_config(self, mapping):
        ''' Create mapping via Reternal API '''
        async with self.session.post(f'{self.api_url}/validations', json=mapping) as resp:
            if not resp.status == 200:
                kek = await resp.text()
                print(resp.status,kek, mapping)

    def load_config(self):
        ''' Find all technique config files '''
        config_files = glob.iglob(f'{self.file_path}/**/*.yml', recursive=True)
        for config in config_files:
            with open(config) as yamlfile:
                yaml_object = yaml.load(yamlfile, Loader=yaml.FullLoader)
                mapping_data = {
                    'name': yaml_object['name'],
                    'integration': yaml_object['integration'],
                    'reference': yaml_object.get('reference', None),
                    'description': yaml_object.get('description', None),
                    'author': yaml_object.get('author', None),
                    'external_id': yaml_object['mitre_technique']['id'],
                    'queries': [query for query in yaml_object['queries']]
                }
                yield mapping_data
          
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        ''' Close aiothttp session '''
        await self.session.close()


async def main():
    ''' Load all config files and import mapped techniques '''
    async with Validations() as validation:
        for config in validation.load_config():
            await validation.import_config(config)

if __name__ == "__main__":
    asyncio.run(main())
