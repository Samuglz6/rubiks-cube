#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from Problem import Problem


def main():
    problem = Problem("../json/x4cube_solution.json")
    print("x4cube_solution.json\nisGoal: ", problem.isGoal(problem.initial))

    problem = Problem("../json/x4cube.json")
    print("\nx4cube.json\nisGoal: ", problem.isGoal(problem.initial))

if __name__ == '__main__':
    main()
