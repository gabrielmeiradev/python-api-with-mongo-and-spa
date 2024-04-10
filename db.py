from pymongo import MongoClient

def create_server_connection(connection_string, db_name, collection_name):
   client = MongoClient(connection_string)
   return client[db_name][collection_name]
