from cli.operations.models import Techniques, TechniqueActors
import mongoengine


class Technique:
    def __init__(self, technique_id):
       self.technique_id = technique_id

    def relate(self, actor_id, name):
        try:
            technique_object = Techniques.objects.get(technique_id=self.technique_id)
            technique_actors = TechniqueActors(actor_id=actor_id, name=name)
            append_actors = technique_object.actors.append(technique_actors)
            technique_object.save()
            result = {'result':'success', 'message':'Succesfully added actor relationship'}

        except mongoengine.errors.DoesNotExist:
            result = {"result":"failed", "message":"Technique already exists"}

        except Exception as err:
            result = {"result":"failed", "message":"Error importing relationship"}

        return result

    def create(self, name, description, platforms, permissions_required, data_sources, references, killchain):
        try:
            mitre_object = Techniques(
                name = name, technique_id = self.technique_id,
                description = description, platforms = platforms,
                permissions_required = permissions_required, data_sources = data_sources,
                references = references, kill_chain_phases = killchain).save()
                    
            result = {"result":"success", "message":"Succesfully added Mitre technique to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre technique already exists"}


        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre technique"}

        return result
