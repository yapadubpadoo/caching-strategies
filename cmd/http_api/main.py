
import sys
import pathlib
path_to_file = pathlib.Path(__file__).parent.absolute()
sys.path.append(f"{path_to_file}/../../")

from core.redis_cache import RedisCache
from core.product_repo import ProductRepo
from core.mysql_db import ProductDB
from core.console_logger import ConsoleLogger
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
logger = ConsoleLogger()

product_repo = ProductRepo(product_db, cache, logger)

from typing import Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products/{product_id}")
def read_item(product_id: int, q: Optional[str] = None):
    try:
        product = product_repo.get_by_id(id=product_id)
        return product
    except Exception as e: 
        raise HTTPException(status_code=404, detail=str(e))