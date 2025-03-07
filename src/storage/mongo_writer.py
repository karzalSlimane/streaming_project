from pymongo import MongoClient

# MongoDB client setup
client = MongoClient('mongodb://mongo:27017')
db = client['user_data']
collection = db['raw_data']

def store_in_mongo(data):
    collection.insert_one(data)
    print(f"Stored in MongoDB: {data}")
