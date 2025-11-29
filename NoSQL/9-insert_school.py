#!/usr/bin/env python3
"""salam"""


def insert_school(mongo_collection, **kwargs):
    """salam """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
