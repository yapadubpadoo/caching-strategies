import sys
import pathlib
path_to_file = pathlib.Path(__file__).parent.absolute()
sys.path.append(f"{path_to_file}/../../")

from core.cache_redis import RedisCache
from core.repo import ProductRepo
from core.db_mysql import ProductDB
import pymysql
import redis