from cli.operations import Mitre
from cli.operations import Actor
from cli.operations import Technique
from cli.config import config
import requests
import json


class ImportMitre:
    def __init__(self, mitre_url=config['mitre']['url']):
        self.mitre_url = mitre_url

    def technique(self, technique_details):
        technique_id = technique_details['id']
        name = technique_details['name']
        description = technique_details['description']
        platforms = technique_details['x_mitre_platforms']
        permissions_required = technique_details.get('x_mitre_permissions_required', None)
        data_sources = technique_details.get('x_mitre_data_sources', None)
        references = technique_details['external_references']
        killchain = [phase['phase_name'] for phase in technique_details['kill_chain_phases']]
        import_technique = Technique(technique_id).create(name, description,
            platforms, permissions_required, data_sources, references, killchain)

        return import_technique

    def actor(self, technique_details):
        actor_id = technique_details['id']
        name = technique_details['name']
        description = technique_details.get('description', None)
        references = technique_details['external_references']
        aliases = technique_details.get('aliases', None)
        import_actor = Actor(actor_id).create(name, description, references, aliases)

    def relation(self, technique_details):
        for relation in technique_details:
            if 'intrusion-set' in relation['source_ref'] and 'attack-pattern' in relation['target_ref']:
                technique_object = Mitre('id').technique(relation['target_ref'])['data']
                actor_object = Mitre('id').actor(relation['source_ref'])['data']
                relate_technique = Technique(technique_object['technique_id']).relate(actor_object['actor_id'], actor_object['name'])
                relate_actor = Actor(actor_object['actor_id']).relate(technique_object['technique_id'], technique_object['name'])
        return {'result':'success', 'message':'Finished loading relationships'}

    def update(self):
        relations = []
        request_object = requests.get(self.mitre_url)
        json_object = request_object.json()
        for technique_details in json_object['objects']:
            if technique_details['type'] == 'attack-pattern': self.technique(technique_details)
            elif technique_details['type'] == 'intrusion-set': self.actor(technique_details)
            elif technique_details['type'] == 'relationship': relations.append(technique_details)
        relate_mitre = self.relation(relations)
        return {'result':'success', 'message':'Finished loading Mitre techniques'}

