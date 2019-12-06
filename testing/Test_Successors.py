#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')

from Problem import Problem
from pprint import pprint


def main():
    problem = Problem("../json/x5cube.json")
    list = problem.stateSpace.successors(problem.initial, 8, 10)
    print("Successors list for", problem.stateSpace.path, ":")
    for (move, state, cost) in list:
        print("move: ", move, " state: ", state, " cost: ", cost)
if __name__ == '__main__':
    main()
