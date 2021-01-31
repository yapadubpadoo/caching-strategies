from core.interface.db import DBInterface
from typing import Any, Union


class ProductDB(DBInterface):
    def __init__(self, mysql_connection) -> None:
        super().__init__()
        self.table = 'product'
        self.connection = mysql_connection
    
    def upsert(self, product: dict) -> int:
        inserted_id = None
        with self.connection.cursor() as cursor:
            conditions = self._generate_sql_conditions(product)
            sql = f"""
                INSERT INTO `{self.table}` SET {conditions['conditions']}
                ON DUPLICATE KEY UPDATE {conditions['conditions']}
            """
            # print(sql, conditions['values'] + conditions['values'])
            cursor.execute(sql, tuple(conditions['values'] + conditions['values']))
            inserted_id = cursor.lastrowid 
        self.connection.commit()
        return inserted_id
    
    def find_one_by_id(self, id: Any) -> Union[dict, None]:
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM `{self.table}` WHERE `id` = %s"
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
    
    def _generate_sql_conditions(self, data: dict) -> dict:
        conditions = []
        values = []
        for k, v in data.items():
            conditions.append(f"`{k}` = %s")
            values.append(v)
        
        return {
            "conditions": ", ".join(conditions),
            "values": values
        }