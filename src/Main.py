#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from Problem import Problem


def main():
    test_validMoves()


def test_isGoal():
    json = jManager.jsonReading("../json/x10cube.json")
    problem = Problem(json)

    if problem.isGoal(problem.initial):
        print("Success")
    else:
        print("Failure")


def test_validMoves():
    json = jManager.jsonReading("../json/x10cube.json")

    cube = Cube(json)

    print(cube.validMovements())


def test_10():
    json = jManager.jsonReading()
    if json is None:
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
