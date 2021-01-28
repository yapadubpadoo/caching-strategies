from core.interface.db import DBInterface
from core.interface.cache import CacheInterface
from core.entity.product import Product

import json


class ProductRepo:
    def __init__(self, db_adapter: DBInterface, cache_adapter: CacheInterface):
        self.db = db_adapter
        self.cache = cache_adapter
    
    def save(self, stuff) -> int:
        result = self.db.upsert(stuff)
        return result
    
    def get_by_id(self, id) -> dict:
        return self.lazy_load(id)
    
    def lazy_load(self, id) -> dict:
        # find in cache first
        product_data = self.cache.get(key=str(id)) 
        if product_data is not None:
            return Product(json.loads(product_data))

        # if not found the find in the db
        product_data =  self.db.find_one_by_id(id) 
        if product_data is not None:
            product = Product(product_data)
            # cache what we've found
            self.cache.set_with_ttl(str(id), str(product), 60 * 60) 
            return product

        raise Exception("Product not found")
        