import sys
import pathlib
path_to_file = pathlib.Path(__file__).parent.absolute()
sys.path.append(f"{path_to_file}/../../")

from core.redis_cache import RedisCache
from core.product_repo import ProductRepo
from core.mysql_db import ProductDB
import pymysql
import redis