#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from Problem import Problem


def main():
    problem = Problem("../json/x2cube.json")
    problem.stateSpace.successors(problem.initial, 8, 10)

if __name__ == '__main__':
    main()
