#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint

def main():
    json = jManager.jsonReading()
    if json == None: exit()
    cube = Cube(json)
    print(cube.md5)
    pprint(cube.faces)
    cube.l(2)
    pprint(cube.faces)

if __name__ == '__main__':
    main()
