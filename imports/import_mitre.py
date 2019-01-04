from operations import Mitre
from config import config
import requests
import json

class ImportMitre:
    def update():
        request_object = requests.get(config['mitre']['url'])
        json_object = request_object.json()
        for technique_details in json_object['objects']:
            if technique_details['type'] == 'attack-pattern':

                # Single value
                technique_id = technique_details['id']
                name = technique_details['name']
                description = technique_details['description']

                # Unique lists
                platforms = technique_details['x_mitre_platforms']
                permissions_required = technique_details.get('x_mitre_permissions_required', None)
                data_sources = technique_details.get('x_mitre_data_sources', None)

                # List with key/value
                references = technique_details['external_references']
                killchain = []
                kill_chain_phases = technique_details['kill_chain_phases']
                for phase in kill_chain_phases:
                    killchain.append(phase['phase_name'])
                    
                import_technique = Mitre.create(name, technique_id, description,
                    platforms, permissions_required, data_sources, references,
                    killchain)
                    
        return {'result':'success', 'message':'Finished loading Mitre techniques'}

