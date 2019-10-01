#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import pprint
import os
import hashlib
from Cube import Cube

def main():
    json = jsonReading()
    cube = Cube(json)
    print(cube.md5)

def jsonReading():
    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".json":
            json_file = file

    if json_file:
        with open(json_file) as output:
            data = json.load(output)

    return data

if __name__ == '__main__':
    main()
