#!/usr/bin/env python3
"""12. Log stats"""
from pymongo import MongoClient

if __name__ == '__main__':
    mongo_client = MongoClient("mongodb://localhost:27017/")
    mongo_collection = mongo_client.logs.nginx
    print(f'{mongo_collection.count_documents()} logs')
    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        logs_count = mongo_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {logs_count}')
    docs = mongo_collection.count_documents({'method': 'GET',
                                            'path': '/status'})
    print(f'{docs} status check')
