# -*- coding:utf-8 -*-

import codecs
import csv
import json
import pprint
import re
#from pymongo import MongoClient

DATAFILE = 'arachnid.csv'
FIELDS = {'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}

def is_NULL(value):
    if value == None:
        return True
    if value == "NULL" or value == '':
        return True
    else:
        return False

def has_notWorld(value):
    try:
        m = re.search(r"[^0-9a-zA-Z]", value)
        m.group(0)
        return True
    except:
        return False


def del_Extra(value):
    try:
        m = re.search(r"(?P<before>.*?)(?P<in>\(.*)",value)
        return m.group('before')
    except:
        return value


def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            row=dict()
            classification = dict()
            for field in fields:
                #print("filed:{}".format(field))
                value = line[field]
                #print value
                if is_NULL(value):
                    value = None

                if field == "rdf-schema#label":
                    value = del_Extra(value)

                if field == "name":
                    if is_NULL(value) or has_notWorld(value):
                        value = row["label"]

                if field == "synonym":
                    if not is_NULL(value):
                        value = parse_array(value)
                        for i in range(len(value)):
                            value[i] = value[i].lstrip()
                            value[i] = value[i].rstrip()
                    else:
                        value = None

                if is_NULL(value) or type(value) == type([]):
                    pass
                else:
                    value = value.lstrip()
                    value = value.rstrip()

                if FIELDS[field] in ("kingdom", "family", "order", "phylum", "genus", "class"):
                    classification[FIELDS[field]] = value
                else:
                    row[FIELDS[field]] = value

            row["classification"] = classification
            data.append(row)

    return data

def parse_array(v):
    if(v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]

def test():
    data = process_file(DATAFILE, FIELDS)
    print("Your first entry:")
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name" : "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == '__main__':
    test()



