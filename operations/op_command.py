from operations.models import Commands
import mongoengine

class Command:
    def create(name, command_type="manual"):
        try:
            commands = Commands(
              name=name,
              type=command_type,
            ).save()
            result = {"result":"success", "message":"Succesfully added command reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Command reference already exists"}

        return result

