from os import access
from .environment import config
import json
import aiohttp
import json
import asyncio

def load_magma(path=config['MAGMA_PATH']):
    magma_mapping = { }
    with open(path, 'r') as magma_file:
        json_object = json.loads(magma_file.read())
        for mapping in json_object:
            magma_mapping[mapping['external_id']] = mapping
    return magma_mapping

class MitreAttck:
    def __init__(self, cti_url=config['ATTCK_URL'], api_url=config['API_URL'], magma_path=None, access_token=None):
        ''' Import the MITRE ATTCK techniques and actors from Github '''
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) #todo fix trusting custom ca
        self.cti_url = cti_url
        self.api_url = api_url
        self.access_token = access_token
        self.magma_path = magma_path
        self.magma_mapping = { }
        self.actors = { }
        self.techniques = { }

    async def import_technique(self, technique):
        ''' Create technique via Reternal API '''
        headers = {'Authorization': f'Bearer {self.access_token}'}
        async with self.session.post(f'{self.api_url}/mitre/techniques', json=technique, headers=headers) as resp:
            if not resp.status == 200:
                error_message = await resp.json()
                print(error_message)


    def format_technique(self, technique_details):
        ''' Format technique to match expected API schema '''
        print(technique_details)
        external_id = technique_details['external_references'][0]['external_id']
        killchain = [phase['phase_name'] for phase in technique_details['kill_chain_phases']]
        technique_data = { 'technique_id': technique_details['id'], 'name':technique_details['name'],
            'description': technique_details['description'], 'platforms': technique_details['x_mitre_platforms'], 
            'permissions_required': technique_details.get('x_mitre_permissions_required', []),
            'data_sources': technique_details.get('x_mitre_data_sources', []),
            'references': technique_details['external_references'], 'kill_chain_phases': killchain,
            'data_sources_available': [], 'actors': [], 'is_subtechnique': technique_details.get('x_mitre_is_subtechnique', False)
        }
        if external_id in self.magma_mapping:
            mapped_usecase = self.magma_mapping[external_id]
            mapped_usecase.pop('external_id')
            technique_data['magma'] = mapped_usecase

        return technique_data

    async def import_actor(self, actor):
        ''' Create actor via Reternal API '''
        headers = {'Authorization': f'Bearer {self.access_token}'}
        async with self.session.post(f'{self.api_url}/mitre/actors', json=actor, headers=headers) as resp:
            if not resp.status == 200:
                print(resp.status)

    def format_actor(self, technique_details):
        ''' Format technique to match expected API schema '''
        actor_data = { 'actor_id': technique_details['id'],  'name': technique_details['name'],
            'references': technique_details['external_references'], 'aliases': technique_details.get('aliases', None),
            'description': technique_details.get('description', None), 'techniques': []
        }
        return actor_data

    def denormalize(self, relations):
        ''' Denormalize relationship between actors and techniques '''
        for relation in relations:
            if 'intrusion-set' in relation['source_ref'] and 'attack-pattern' in relation['target_ref']:
                technique_object = self.techniques.get(relation['target_ref'], None)
                actor_object = self.actors[relation['source_ref']]
                if technique_object:
                    technique_object['actors'].append({'actor_id': actor_object['actor_id'], 'name': actor_object['name']})
                    actor_object['techniques'].append({'technique_id': technique_object['technique_id'], 'name': technique_object['name']})
    
    async def __aenter__(self):
        ''' Initialize session and populate techniques and actors '''
        if self.magma_path:
            self.magma_mapping = load_magma(self.magma_path)

        async with self.session.get(self.cti_url) as resp:
            # Directly loading resp as json will raise an aiohttp exception
            # Github returns json but with incorrect mimetype (text/html). Read response as text first
            all_techniques = await resp.text()
    
        relations = []
        for technique_details in json.loads(all_techniques)['objects']:
            if technique_details.get('revoked', False) == False:
                if technique_details['type'] == 'attack-pattern': 
                    self.techniques[technique_details['id']] = self.format_technique(technique_details)
                elif technique_details['type'] == 'intrusion-set':
                    self.actors[technique_details['id']] =  self.format_actor(technique_details)
                elif technique_details['type'] == 'relationship':
                    relations.append(technique_details)
        self.denormalize(relations)
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        ''' Close aiothttp session '''
        await self.session.close()


async def import_attck(*args, **kwargs):
    ''' Retrieve MITRE ATTCK database and format data '''
    async with MitreAttck(**kwargs) as mitre:
        for technique in mitre.techniques.values():
            await mitre.import_technique(technique)
        for actor in mitre.actors.values():
            await mitre.import_actor(actor)

if __name__ == "__main__":
    asyncio.run(import_attack())
