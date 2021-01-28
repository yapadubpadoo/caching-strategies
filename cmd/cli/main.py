import sys
import pathlib
path_to_file = pathlib.Path(__file__).parent.absolute()
sys.path.append(f"{path_to_file}/../../")

from core.cache_redis import RedisCache
from core.repo import ProductRepo
from core.db_mysql import ProductDB
import pymysql
import redis

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='my_shop',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
redis = redis.Redis(host='localhost', port=6379, db=0)

product_db = ProductDB(connection)
cache = RedisCache(redis)

product_repo = ProductRepo(product_db, cache)
product_id = product_repo.save({"name": "Gundum", "price": 10.17})
print("ID:", product_id, )
print("Get product 1st attempt:", product_repo.get_by_id(product_id))
print("Get product 2nd attempt:", product_repo.get_by_id(product_id))