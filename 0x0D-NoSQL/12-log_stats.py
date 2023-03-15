#!/usr/bin/env python3
"""12. Log stats"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017")
    collection = client.logs.nginx
    print(f"{collection.estimated_document_count()} logs")
    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        logs_count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {logs_count}')
    docs = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{docs} status check')
