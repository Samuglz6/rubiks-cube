#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import pprint
import os
import hashlib

def jsonReading():
    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".json":
            print(file)
            json_file = file

    if json_file:
        with open(json_file) as output:
            data = json.load(output)

    return data

def generateMD5():
    cadena = ''
    for value in json_file.values():
        for x in value:
                cadena += ''.join(map(str,x))

    print("string: "+cadena)
    md5 = hashlib.md5(cadena.encode('utf-8')).hexdigest()
    print("md5: "+md5)

if __name__ == '__main__':
    json_file = jsonReading()
    pprint.pprint(json_file)
    generateMD5()
