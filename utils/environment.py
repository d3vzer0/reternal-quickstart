import os

config = {
    'CTI_URL': os.getenv('RT_ATTCK_URL', 'https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'),
    'API_URL': os.getenv('RT_API_URL', 'https://reternal.local:8443/api/v1'),
    'API_TOKEN': os.getenv('RT_API_TOKEN', None),
    'TECHNIQUES_PATH': os.getenv('RT_TECHNIQUES_PATH', '../mitre/techniques'),
    'VALIDATIONS_PATH': os.getenv('RT_VALIDATIONS_PATH', '../mitre/validations'),
    'PRODUCTS_PATH': os.getenv('RT_PRODUCTS_PATH', '../mitre/datasource_mapping.json'),
    'MAGMA_PATH': os.getenv('RT_MAGMA_PATH', '../mitre/magma_mapping.json'),
}