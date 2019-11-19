#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, time
from pprint import pprint
sys.path.append('../src')

from JsonManager import JsonManager as jManager
from Cube import Cube
from State import State

def start():
    try:
        while 1:
            testConsecutiveMoves()
    except KeyboardInterrupt:
        print("\nTest has been interrupted")

def testConsecutiveMoves():
    cube = Cube(jManager.jsonReading("../json/x4cube.json"))
    state = State(cube)
    print(state.md5)

    letters = ["B", "b", "D", "d", "L", "l"]
    moves = []
    for element in letters:
        for number in range(cube.size):
            moves.append(element + str(number))
    while True:
        key = 0
        print("\nOption's movements: ")
        print(",".join([item for item in moves]))

        key = input("Selection:")
        try:
            method = getattr(cube, key[0])
            method(int(key[1]))
            state = State(cube)
            print(state.md5)
        except:
            print("ERROR. Not valid movement")

        jManager.jsonWriting('/testing', state.current)
        pprint(state.current.faces)
        print("Results have been saved in testing.json")


        time.sleep(1)

def testMove(cube):
    letters = ["B", "b", "D", "d", "L", "l"]
    moves = []
    for element in letters:
        for number in range(cube.size):
            moves.append(element + str(number))
    while True:
        key = 0
        print("\nOption's movements: ")
        print(",".join([item for item in moves]))

        key = input("Selection:")

        if key in moves:
            if list(key)[0] == 'b':
                cube.b(int(list(key)[1]))
            elif list(key)[0] == 'B':
                cube.B(int(list(key)[1]))
            elif list(key)[0] == 'l':
                cube.l(int(list(key)[1]))
            elif list(key)[0] == 'L':
                cube.L(int(list(key)[1]))
            elif list(key)[0] == 'D':
                cube.D(int(list(key)[1]))
            elif list(key)[0] == 'd':
                cube.d(int(list(key)[1]))
            break
        else:
            print("Not a valid selection")

    jManager.jsonWriting('/testing', cube)
    print("Results have been saved in testing.json")

    time.sleep(1)

if __name__ == '__main__':
    start()
