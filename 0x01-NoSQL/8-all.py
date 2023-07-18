#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """ List all documents in Python
    """
    found = mongo_collection.find()

    return [doc for doc in found]
