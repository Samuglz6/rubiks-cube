#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint

def main():
    json = jManager.jsonReading()
    if json == None:
        print("ERROR. The selected json does not contains a NxNxN cube.")
        exit()
    cube = Cube(json)
    print(cube)

if __name__ == '__main__':
    main()
