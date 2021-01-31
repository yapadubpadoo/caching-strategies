import json

class Product:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.desc = data['desc'] if 'desc' in data else ''
        self.price = float(data['price'])
    
    def __str__(self) -> str:
        return json.dumps(self.__dict__)