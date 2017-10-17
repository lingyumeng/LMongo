# -*- coding:utf-8 -*-

import pymongo

def add_city(db):
    db.cities.insert({"name" : "Chicago"})

def get_city(db):
    return db.cities.find_one()

def get_db():
    from pymongo import MongoClient
    client = MongoClient('192.168.56.101:27017')

    db = client.examples
    return db

if __name__ == '__main__':
    db = get_db()
    add_city(db)
    print(get_city(db))