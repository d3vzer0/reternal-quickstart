import json
import asyncio
from environment import config
from reternalapi import ReternalAPI


class Products:
    def __init__(self, products = None):
        self.products = products if products else []

    @classmethod
    def from_file(cls, path = '../mitre/datasource_mapping.json'):
        with open(path, 'r') as productlist:
            products_json = json.loads(productlist.read())

        products = [product for product in products_json]
        return cls(products)

async def import_products(*args, **kwargs):
    products = Products.from_file(config['PRODUCTS_PATH'])
    async with ReternalAPI(api_url=config['API_URL']) as reternal:
        for product in products.products:
            await reternal.save('/products', product)

if __name__ == "__main__":
    asyncio.run(import_products())
