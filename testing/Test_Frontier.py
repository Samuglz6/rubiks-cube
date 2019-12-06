#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem


def main():
    problem = Problem("../json/x4cube.json")
    fringe = Frontier()

    print("Inserting...\n")
    for i in range(5, 0, -1):
        node = TreeNode(i, problem.initial, 0, None, 1, None, 1)
        fringe.insert(node)

    for i in range(6,11,1):
        node = TreeNode(i, problem.initial, 0, None, 1, None, 2)
        fringe.insert(node)

    print("Elements:")
    for element in fringe.frontier:
        print("id: ", element.id, "f: " ,element.getF())

    print("\nRemoving...")
    while not fringe.isEmpty():
        fringe.remove()

    print("\nisEmpty: ", fringe.isEmpty())

if __name__ == '__main__':
    main()
