#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('../src')

from JsonManager import JsonManager as jManager
from Cube import Cube
from State import State

def main():
    cube = Cube(jManager.jsonReading("../json/x10cube.json"))
    state = State(cube)

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_l3.json"))
    state2 = State(cube2)

    print("Move l3:")
    cube.l(3)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_D1.json"))
    state2 = State(cube2)

    print("Move D1:")
    cube.D(1)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_l1.json"))
    state2 = State(cube2)

    print("Move l1:")
    cube.l(1)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_d0.json"))
    state2 = State(cube2)

    print("Move d0:")
    cube.d(0)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_B0.json"))
    state2 = State(cube2)

    print("Move B0:")
    cube.B(0)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_b5.json"))
    state2 = State(cube2)

    print("Move b5:")
    cube.b(5)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_l2.json"))
    state2 = State(cube2)

    print("Move l2:")
    cube.l(2)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)
    print("\n")

    cube2 = Cube(jManager.jsonReading("../json/moves_x10/x10cube_d1.json"))
    state2 = State(cube2)

    print("Move d1:")
    cube.d(1)
    state = State(cube)
    print("Obtained:" + state.md5)
    print("Expected:" + state2.md5)

if __name__ == '__main__':
    main()
