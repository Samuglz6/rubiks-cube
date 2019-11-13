#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')

from Problem import Problem
from pprint import pprint


def main():
    problem = Problem("../json/x2cube.json")
    list = problem.stateSpace.successors(problem.initial, 8, 10)
    for (move, state, cost) in list:
        print("\n---------- Movement: ", move, "-------------")
        print("\n\tOriginal")
        pprint(problem.initial.current.faces)
        print("\n\tChanged")
        pprint(state.current.faces)
if __name__ == '__main__':
    main()
