from environment import config
import json
import aiohttp
import json
import asyncio


class Products:
    def __init__(self, products_path=config['PRODUCTS_PATH'],api_url=config['API_URL']):
        self.session = aiohttp.ClientSession()
        self.products_path = products_path
        self.api_url = api_url

    async def import_product(self, product):
        ''' Create product mapping via Reternal API '''
        async with self.session.post(f'{self.api_url}/products', json=product) as resp:
            if not resp.status == 200:
                error_message = await resp.json()

    def load_products(self):
        with open(self.products_path, 'r') as productlist:
            products_json = json.loads(productlist.read())

        for product in products_json:
            yield product

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        ''' Close aiothttp session '''
        await self.session.close()


async def main():
    async with Products() as products:
        for product in products.load_products():
            await products.import_product(product)

if __name__ == "__main__":
    asyncio.run(main())
