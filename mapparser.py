# -*- coding:utf-8 -*-

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tags = dict()

    with open(filename, 'r') as f:
        for event, elem in ET.iterparse(f):
            if elem.tag in tags:
                tags[elem.tag] += 1
            else:
                tags[elem.tag] = 1
    return tags

def test():
    tags = count_tags('example.osm')
    pprint.pprint(tags)

    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

if __name__ == '__main__':
    test()
