from cli.operations.models import CommandMapping
import mongoengine
 
 
class MapCommand:
    def __init__(self, name):
        self.name = name

    def create(self, technique_data, mapping_data, all_commands, phase):
        try:
            mitre_object = CommandMapping(
                name=self.name, technique_id=technique_data['technique_id'],
                technique_name=technique_data['name'], external_id=mapping_data['external_id'],
                kill_chain_phase=phase, platform=mapping_data['platform'], commands=all_commands,
                reference=mapping_data['reference'], actors=technique_data['actors'],
                author=mapping_data['author'], description=mapping_data['description']).save()
            result = {"result":"success", "message":"Succesfully added Mitre command/technique reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre command/technique reference already exists"}

        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre command/technique reference"}

        return result

 
