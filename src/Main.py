#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint

def main():
    cube = Cube(jManager.jsonReading())
    print(cube.md5)
    pprint(cube.Faces)

if __name__ == '__main__':
    main()
