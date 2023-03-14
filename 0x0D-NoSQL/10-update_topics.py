#!/usr/bin/env python3
"""10. Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    doc_name = {'name': name}
    doc_topics = { "$set": {'topics': topics} }
    mongo_collection.update_many(doc_name, doc_topics)
