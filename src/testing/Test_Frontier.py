#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
sys.path.append('../')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager

def main():
    problem = Problem(jManager.jsonReading("../../json/x4cube.json"))
    node1 = TreeNode(problem.initial,0,0,0)
    node2 = TreeNode(problem.initial,0,0,1)
    node3 = TreeNode(problem.initial,0,0,2)

    fringe = Frontier()
    fringe.insert(node1)
    fringe.insert(node2)
    fringe.insert(node3)

    for element in fringe.frontier: print(element.f)

    fringe.remove()

    for element in fringe.frontier: print(element.f)

    print(fringe.isEmpty())
    fringe.remove()
    fringe.remove()
    print(fringe.isEmpty())
    print(problem.isGoal(problem.initial))


if __name__ == '__main__':
    main()
