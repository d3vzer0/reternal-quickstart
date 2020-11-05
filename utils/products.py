import json
import asyncio
from environment import config
from reternalapi import ReternalAPI


class Products:
    def __init__(self, products = None):
        """
        Initialize the products

        Args:
            self: (todo): write your description
            products: (str): write your description
        """
        self.products = products if products else []

    @classmethod
    def from_file(cls, path = '../mitre/datasource_mapping.json'):
        """
        Create a product from a productlist of products.

        Args:
            cls: (todo): write your description
            path: (str): write your description
        """
        with open(path, 'r') as productlist:
            products_json = json.loads(productlist.read())

        products = [product for product in products_json]
        return cls(products)

async def import_products(*args, **kwargs):
      """
      Import product files.

      Args:
      """
    products = Products.from_file(config['PRODUCTS_PATH'])
    async with ReternalAPI(api_url=config['API_URL']) as reternal:
        for product in products.products:
            await reternal.save('/products', product)

if __name__ == "__main__":
    asyncio.run(import_products())
