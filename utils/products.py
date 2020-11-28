import json
import asyncio
from .reternalapi import ReternalAPI


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
    products = Products.from_file(kwargs['path'])
    async with ReternalAPI(api_url=kwargs['api_url'], api_token=kwargs['access_token']) as reternal:
        for product in products.products:
            await reternal.save('/products', product)

if __name__ == "__main__":
    asyncio.run(import_products())
