#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint
import copy

def start():
    cube = Cube(jManager.jsonReading("../json/x10cube.json"))
    print(cube.md5)
    while(1):
        testMove(cube)

def testMove(cube):
    letters = ["B", "b", "D", "d", "L", "l"]
    moves = []
    for element in letters:
        for number in range(cube.size):
            moves.append(element+str(number))
    while True:
        key = 0
        print("\nOpciones de movimientos: ")
        print(",".join([item for item in moves]))
        try:
            key = input("Selection:")
        except ValueError:
            print("Error, selection must be integer")
            continue
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

    jManager.jsonWriting('../testing/output/','testing', cube)
    #print("Results have been saved in testing.json")
    print(cube.md5)
    #print(cube.faces)

if __name__ == '__main__':
    start()
