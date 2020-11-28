
from .reternalapi import ReternalAPI
import glob
import yaml
import asyncio
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


class Sigma:
    def __init__(self, rules = None):
        self.rules = rules if rules else []

    @classmethod
    def from_path(cls, path = '../mitre/validations'):
        sigma_rules = []
        config_files = glob.iglob(f'{path}/sigma/**/**/*.yml', recursive=True)
        for config in config_files:
            with open(config) as yamlfile:
                yaml_objects = list(yaml.load_all(yamlfile, Loader=yaml.FullLoader))
                if len(yaml_objects) > 1:
                    sigma_group = yaml_objects[0]
                    yaml_objects.pop(0)
                    for document in yaml_objects:
                        defaults = copy.deepcopy(sigma_group)
                        sigma_rules.append(merge_dicts(defaults, document))

                elif len(yaml_objects) == 1:
                    sigma_rules.append(yaml_objects[0])

        return cls(sigma_rules)


async def import_sigma(*args, **kwargs):
    ''' Load all config files and import mapped techniques '''
    sigma = Sigma.from_path(kwargs['path'])
    async with ReternalAPI(kwargs['api_url'], api_token=kwargs['access_token']) as reternal:
        for rule in sigma.rules:
            await reternal.save('/sigma', rule)


if __name__ == "__main__":
    asyncio.run(import_sigma())

