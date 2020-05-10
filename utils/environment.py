import os

config = {
    'ATTCK_URL': os.getenv('RT_ATTCK_URL', 'https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'),
    'API_URL': os.getenv('RT_API_URL', 'http://localhost:5000/api/v1'),
    'TECHNIQUES_PATH': os.getenv('RT_TECHNIQUES_PATH', '../mitre/techniques'),
    'VALIDATIONS_PATH': os.getenv('RT_VALIDATIONS_PATH', '../mitre/validations')
}