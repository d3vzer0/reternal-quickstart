from cli.operations.models import Commands
import mongoengine


class Command:
    def __init__(self, name):
        self.name = name

    def create(self, command_type="Manual"):
        try:
            commands = Commands(
              name=self.name,
              type=command_type,
            ).save()
            result = {"result":"success", "message":"Succesfully added command reference to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Command reference already exists"}

        return result

