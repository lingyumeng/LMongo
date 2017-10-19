# -*- coding:utf-8 -*-

from datetime import datetime
from pymongo import MongoClient
import pprint

def range_query():
    query = {"foundingDate" : {"$gt" : datetime(2000, 12, 31)}}

    return query

def get_db():
    client = MongoClient('localhost:27017')
    db = client.examples
    return db

if __name__ == '__main__':
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print("Found cities:", cities.count())
    pprint.pprint(cities[0])
