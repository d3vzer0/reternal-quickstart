from cli.operations.models import Techniques, Actors
import mongoengine

class Mitre:
    def __init__(self, query_field):
        self.query_field = query_field

    def technique(self, reference_id):
        try:
            if self.query_field == 'id':
                mitre_object = Techniques.objects.get(technique_id=reference_id)
            elif self.query_field == 'external_id':
                mitre_object = Techniques.objects.get(references__external_id=reference_id)

            result = {"result":"success", "data":mitre_object}

        except mongoengine.errors.DoesNotExist:
                result = {"result":"failed", "data":"Mitre technique does not exist"}

        except Exception as err:
            result = {"result":"failed", "data":"Mitre technique lookup error"}

        return result

    def actor(self, reference_id):
        try:
            if self.query_field == 'id':
                actor_object = Actors.objects.get(actor_id=reference_id)
            elif self.query_field == 'external_id':
                actor_object = Actors.objects.get(references__external_id=reference_id)

            result = {"result":"success", "data":actor_object}

        except mongoengine.errors.DoesNotExist:
                result = {"result":"failed", "data":"Actor does not exist"}

        except Exception as err:
            result = {"result":"failed", "data":"Actor lookup error"}

        return result
