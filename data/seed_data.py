from faker import Faker
from pymongo import MongoClient

fake = Faker()
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
collection = db["clientes"]

batch_size = 10000
for _ in range(100):  # 100 * 10k = 1 milhão
    batch = [{
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number()
    } for _ in range(batch_size)]
    collection.insert_many(batch)

print("1 milhão de registros inseridos com sucesso!")
