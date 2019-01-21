from operations.models import CommandMapping
import mongoengine
 
class MapCommand:
    def __init__(self, name):
        self.name = name

    def create(self, technique_id, technique_name, external_id, kill_chain_phase, platform, commands, reference=None, author=None, description=None):
        try:
            mitre_object = CommandMapping(
                name = self.name, technique_id = technique_id,
                technique_name = technique_name, external_id = external_id,
                kill_chain_phase = kill_chain_phase, platform = platform,
                commands = commands, reference = reference,
                author = author, description = description).save()
                    
            result = {"result":"success", "message":"Succesfully added Mitre command/technique reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre command/technique reference already exists"}

        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre command/technique reference"}

        return result

 
