from cli.operations.models import Actors
from cli.operations.models import ActorTechniques
import mongoengine


class Actor:
    def __init__(self, reference_id):
        self.reference_id = reference_id

    def relate(self, technique_id, name):
        try:
            actor_object = Actors.objects.get(actor_id=self.reference_id)
            actor_techniques = ActorTechniques(technique_id=technique_id, name=name )
            actor_object.techniques.append(actor_techniques)
            actor_object.save()
            result = {'result':'success', 'message':'Succesfully added actor relationship'}

        except mongoengine.errors.DoesNotExist:
            result = {"result":"failed", "message":"Actor does not exists"}

        except Exception as err:
            print(err)
            result = {"result":"failed", "message":"Error importing relationship"}

        return result

    def create(self, name, description, references=None, aliases=None):
        try:
            actor_object = Actors(
                name=name, actor_id=self.reference_id,
                description=description, references=references,
                aliases=aliases).save()
            result = {"result":"success", "message":"Succesfully added Actor DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Actor already exists"}

        except Exception as err:
            result = {"result":"failed", "message":"Error importing Actor"}

        return result
