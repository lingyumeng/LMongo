# -*- coding:utf-8 -*-

from autos import process_file
from pymongo import MongoClient

def insert_autos(infile, db):
    data = process_file(infile)
    print(data)
    db.autos.insert(data)



if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print(db.autos.find_one())
