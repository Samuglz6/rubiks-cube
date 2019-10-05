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
    testing(cube)

def jsonReading():
    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".json":
            json_file = file

    if json_file:
        with open(json_file) as output:
            data = json.load(output)

    return data

def testing(cube):
    '''for value in cube.Faces.keys()
        print(value)
        for x in cube.Faces[value]:
            print(x)'''
    
    for n in range(3):
        print("Aplying B%d movement" %n)
        cube.B(n)
        
    for n in range(3):
        print("Aplying b%d movement" %n)
        cube.b(n)


    

if __name__ == '__main__':
    main()
