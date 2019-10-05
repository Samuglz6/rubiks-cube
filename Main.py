#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube

def main():
    cube = Cube(jManager.jsonReading())
    print(cube.md5)

if __name__ == '__main__':
    main()
