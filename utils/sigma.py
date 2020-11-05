
from environment import config
from reternalapi import ReternalAPI
import glob
import yaml
import asyncio
import copy

# Thanks fo Srisaila for this nested merge sample (https://stackoverflow.com/a/47564936)
# this example doesn't override nested dictionaries, which is the default behaviour of the
# regular dict update operation or {**dict1, **dict2}

def merge_dicts(default, override):    
    """
    Merge a dictionary of a dictionary of dicts.

    Args:
        default: (todo): write your description
        override: (bool): write your description
    """
    for key in override:
        if key in default:
            if isinstance(default[key], dict) and isinstance(override[key], dict):
                merge_dicts(default[key], override[key])
        else:
            default[key] = override[key]
    return default


class Sigma:
    def __init__(self, rules = None):
        """
        Initialize the rules.

        Args:
            self: (todo): write your description
            rules: (str): write your description
        """
        self.rules = rules if rules else []

    @classmethod
    def from_path(cls, path = '../mitre/validations'):
        """
        Create a yamlrules from a yaml file.

        Args:
            cls: (todo): write your description
            path: (str): write your description
        """
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
    sigma = Sigma.from_path(config['VALIDATIONS_PATH'])
    async with ReternalAPI(api_url=config['API_URL']) as reternal:
        for rule in sigma.rules:
            await reternal.save('/sigma', rule)


if __name__ == "__main__":
    asyncio.run(import_sigma())

