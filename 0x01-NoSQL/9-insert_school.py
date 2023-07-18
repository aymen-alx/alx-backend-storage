#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python
    """
    obj = mongo_collection.insert_one(kwargs)

    return obj.inserted_id
