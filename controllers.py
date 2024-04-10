from db import create_server_connection
from models import Item
import uuid
import json

connection = create_server_connection("mongodb://localhost:27017", "my_db", "shop")

def create_item(item: Item):
    item.id = str(uuid.uuid4())
    mydict = { "id": item.id, "name": item.name, "description": item.description, "price": item.price, "on_offer": item.on_offer }
    connection.insert_one(mydict)
    return item

def get_all_items():
    items = connection.find()  
    items_list = []  
    for item in items:
        item['_id'] = str(item['_id'])
        items_list.append(item)  
    return items_list

def update_item(item_id: str, item: Item):
    query = { "id": item_id }
    new_values = { "$set": { "name": item.name, "description": item.description, "price": item.price, "on_offer": item.on_offer } }
    connection.update_one(query, new_values)
    return item

def delete_item(item_id: str):
    query = { "id": item_id }
    connection.delete_one(query)
    return {"message": "Item deletado com sucesso"}
