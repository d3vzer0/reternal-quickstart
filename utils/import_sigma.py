
from environment import config
import glob
import yaml
import asyncio
import aiohttp
import hashlib
import copy

# Thanks fo Srisaila for this nested merge sample (https://stackoverflow.com/a/47564936)
# this example doesn't override nested dictionaries, which is the default behaviour of the
# regular dict update operation or {**dict1, **dict2}

def merge_dicts(default, override):    
    for key in override:
        if key in default:
            if isinstance(default[key], dict) and isinstance(override[key], dict):
                merge_dicts(default[key], override[key])
        else:
            default[key] = override[key]
    return default


class Validations:
    def __init__(self, file_path=config['VALIDATIONS_PATH'], api_url=config['API_URL']):
        self.file_path = file_path
        self.api_url = api_url
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) #todo fix trusting custom ca

    async def import_config(self, mapping):
        ''' Create mapping via Reternal API '''
        async with self.session.post(f'{self.api_url}/sigma', json=mapping) as resp:
            if not resp.status == 200:
                kek = await resp.text()
                print(resp.status, kek, mapping)

    def load_config(self):
        ''' Find and parse all sigma config files '''
        config_files = glob.iglob(f'{self.file_path}/sigma/**/**/*.yml', recursive=True)
        for config in config_files:
            with open(config) as yamlfile:
                yaml_objects = list(yaml.load_all(yamlfile, Loader=yaml.FullLoader))
                if len(yaml_objects) > 1:
                    sigma_group = yaml_objects[0]
                    yaml_objects.pop(0)
                    for document in yaml_objects:
                        defaults = copy.deepcopy(sigma_group)
                        yield merge_dicts(defaults, document)

                elif len(yaml_objects) == 1:
                    yield yaml_objects[0]
          
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

