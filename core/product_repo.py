from core.interface.db import DBInterface
from core.interface.cache import CacheInterface
from core.interface.logger import LoggerInterface
from core.entity.product import Product

import json


class ProductRepo:

    CACHE_IN_MINUTES = 30
    
    def __init__(self, 
        db_adapter: DBInterface, 
        cache_adapter: CacheInterface,
        logger: LoggerInterface
    ):
        self.db = db_adapter
        self.cache = cache_adapter
        self.logger = logger
    
    def save(self, product) -> Product:
        return self.write_through(product)
    
    def get_by_id(self, product_id) -> Product:
        return self.lazy_load(product_id)
    
    def lazy_load(self, product_id) -> Product:
        # find in cache first
        product_data = self.cache.get(key=str(product_id)) 
        if product_data is not None:
            self.logger.debug("Cache hit!", product_id)
            return Product(json.loads(product_data))

        # if not found the find in the db
        self.logger.debug("Cache missed", product_id)
        product_data =  self.db.find_one_by_id(product_id) 
        if product_data is not None:
            product = Product(product_data)
            # cache what we've found
            self.cache.set_with_ttl(str(product_id), str(product), self.CACHE_IN_MINUTES * 60) 
            self.logger.debug("Cache set", product_id)
            return product

        raise Exception("Product not found")

    def write_through(self, stuff) -> Product:
        product_id = self.db.upsert(stuff)
        stuff['id'] = product_id
        product = Product(stuff)
        self.logger.debug("Product save", product_id)
        self.cache.set_with_ttl(str(product_id), str(product), self.CACHE_IN_MINUTES * 60) 
        return product