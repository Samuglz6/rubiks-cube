#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
sys.path.append('../')

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint

def main():
    cube = Cube(jManager.jsonReading("../../json/x10cube.json"))

    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_l3.json"))
    print("Move l3:")
    cube.l(3)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_D1.json"))
    print("Move D1:")
    cube.D(1)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_l1.json"))
    print("Move l1:")
    cube.l(1)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_d0.json"))
    print("Move d0:")
    cube.d(0)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_B0.json"))
    print("Move B0:")
    cube.B(0)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_b5.json"))
    print("Move b5:")
    cube.b(5)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_l2.json"))
    print("Move l2:")
    cube.l(2)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)
    print("\n")
    cube2 = Cube(jManager.jsonReading("../../testing/x10cube_d1.json"))
    print("Move d1:")
    cube.d(1)
    print("Obtained:"+cube.md5)
    print("Expected:"+cube.md5)

if __name__ == '__main__':
    main()
