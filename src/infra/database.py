import pymongo
from utils.variables import CONNECTION_URL


class MongoDB:
    def __init__(self, database_name, collection_name):
        self.database_name = database_name
        self.collection_name = collection_name

    def set_mongo_client(self):
        self.mongo_client = pymongo.MongoClient(CONNECTION_URL)

    def set_mongo_database(self):
        self.mongo_database = self.mongo_client[self.database_name]

    def set_mongo_collection(self):
        self.mongo_collection = self.mongo_database[self.collection_name]

    def insert_document(self, json_document):
        if type(json_document) is dict:
            response = self.mongo_collection.insert_one(json_document) \
                .inserted_id
        elif type(json_document) is list:
            response = self.mongo_collection.insert_many(json_document)\
                .inserted_ids
        return response

    def read_document(self, query):
        result = self.mongo_collection.find_one(query)
        return result

    def delete_document(self, keys):
        result = self.mongo_collection.find_one_and_delete(keys)
        return result

    def update_document(self, keys, update_data):
        new_data = {
            "$set": update_data
        }
        result = self.mongo_collection.find_one_and_update(
            filter=keys,
            update=new_data
        )
        return result
