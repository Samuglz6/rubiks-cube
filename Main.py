#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json, pprint
import os


def jsonReading():
    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".json":
            print(file)
            json_file = file

    if json_file:
        with open(json_file) as output:
            data = json.load(output)

    return data

if __name__ == '__main__':
    pprint.pprint(jsonReading())
