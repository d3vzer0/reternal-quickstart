from operations.models import MitreCommands
import mongoengine

class MitreCommand:
    def create(technique_id, platform, commands, metta_id, external_id, attack_phase):
        try:
            mitre_object = MitreCommands(
                        technique_id = technique_id,
                        external_id = external_id,
                        commands = commands,
                        platform = platform,
                        metta_id = metta_id,
                        kill_chain_phase = attack_phase
                    ).save()
                    
            result = {"result":"success", "message":"Succesfully added Mitre command/technique reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre command/technique reference already exists"}

        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre command/technique reference"}

        return result
