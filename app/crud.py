from db import collection
from bson.objectid import ObjectId

def create_cliente(cliente):
    return collection.insert_one(cliente)

def read_clientes():
    return list(collection.find())

def update_cliente(cliente_id, novos_dados):
    return collection.update_one({"_id": ObjectId(cliente_id)}, {"$set": novos_dados})

def delete_cliente(cliente_id):
    return collection.delete_one({"_id": ObjectId(cliente_id)})
