from operations.models import MitreCommands
import mongoengine

class MitreCommand:
    def create(command, technique_id, input, idle_time, metta_id):
        try:
            mitre_object = MitreCommands(
                        technique_id = technique_id,
                        command = command,
                        input = input,
                        idle_time = idle_time,
                        metta_id = metta_id
                    ).save()
                    
            result = {"result":"success", "message":"Succesfully added Mitre command/technique reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre command/technique reference already exists"}


        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre command/technique reference"}

        return result
