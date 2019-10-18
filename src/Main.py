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

    cube.l(3)
    cube.D(1)
    cube.l(1)
    cube.d(0)

    cube2 = Cube(jManager.jsonReading("../testing/x10cube_d0.json"))

    print(cube.md5)
    print(cube2.md5)


if __name__ == '__main__':
    main()
