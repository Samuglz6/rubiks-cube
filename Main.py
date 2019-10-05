#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import os
from Cube import Cube
from pprint import pprint


def main():
    json = jsonReading()
    cube = Cube(json)
    print(cube.md5)

    pprint(cube.Faces)

    cube.B(0)
    print('-----------------')
    for value in cube.Faces.keys():
        print(value)
        for x in cube.Faces[value]:
            print(x)
        print('---------')

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
