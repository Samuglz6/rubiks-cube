#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')

from JsonManager import JsonManager as jManager

from Problem import Problem


def main():
    json = jManager.jsonSelection()
    problem = Problem(json)
    print("isGoal: ", problem.isGoal(problem.initial))

if __name__ == '__main__':
    main()
