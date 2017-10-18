# -*- coding:utf-8 -*-

import pprint
from pymongo import MongoClient

def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche
    query = {"manufacturer" : "Porsche"}

    return query

def get_db(db_name):
    # For local use
    client = MongoClient('192.168.56.101:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    return db.autos.find(query)

if __name__ == '__main__':
    # For local use
    db = get_db('example')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    for car in results:
        pprint.pprint(car)