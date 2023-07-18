#!/usr/bin/env python3
"""
Top students
"""
from collections import OrderedDict


def top_students(mongo_collection):
    """
    Top students
    """
    line = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
            {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]

    return mongo_collection.aggregate(line)
