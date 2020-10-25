import aiohttp


class ReternalAPI:
    def __init__(self, api_url=None, api_token=None):
        ''' Import the MITRE ATTCK techniques and actors from Github '''
        self.session = None
        self.api_url = api_url
        self.api_token = api_token

    async def save(self, endpoint, data):
        ''' Create Sigma rule via Reternal API '''
        headers = {'Authorization': f'Bearer {self.api_token}'}
        async with self.session.post(f'{self.api_url}{endpoint}', json=data, headers=headers) as resp:
            if not resp.status == 200:
                error_message = await resp.json()
                print(error_message)

    async def __aenter__(self):
        ''' Initialize session and populate techniques and actors '''
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        ''' Close aiothttp session '''
        await self.session.close()

