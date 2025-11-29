#!/usr/bin/env python3
"""salam"""


def update_topics(mongo_collection, name, topics):
"""ssssssssss"""
   mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
