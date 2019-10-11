#!/usr/bin/python3
#-*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from pprint import pprint


def start():
    cube = Cube(jManager.jsonReading())
    menu(cube)

def menu(cube):
    while True:
        selection = 0
        try: selection = int(input("Options for testing:\n\t1 - Test a move\n\t2 - Test every movement\nSelection:"))
        except ValueError:
            print("Error, selection must be integer")
            continue
        if selection == 1:
            testOneMove(cube)
            break
        if selection == 2:
            testingBackFront(cube)
            break
        else: print("Not a valid selection")

def testOneMove(cube):
    moves = ["B0", "B1", "B2", "b0", "b1", "b2", "L0", "L1", "L2", "l0", "l1", "l2", "D0", "D1", "D2", "d0", "d1", "d2"]
    while True:
        key = 0
        print("Opciones de movimientos: ")
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

    jManager.jsonWriting('testing', cube)
    print("Results have been saved in testing.json")

def testingBackFront(cube):
    for n in range(3):
        print("Aplying B%d movement" %n)
        cube.B(n)
        pprint(cube.faces)

    for n in range(3):
        print("Aplying b%d movement" %n)
        cube.b(n)
        pprint(cube.faces)

if __name__ == '__main__':
    start()
