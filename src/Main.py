#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Cube import Cube
from Problem import Problem


def main():
    json = jManager.jsonReading("../json/x3cube.json")
    cube = new Cube(json)
    initial = new State(cube)
    problem = new Problem(initial)

def bounded_search(problem, strategy, max_depth):
    frontier = new Frontier()
    init_node = new TreeNode(problem.initial, 0,0,0)
    frontier.insert(init_node)
    solution = False
    while (not solution) and (not frontier.isEmpty()):
        actual_node = frontier.remove()
        if(problem.isGoal()):
            solution = True
        else:
            successors_list = problem.stateSpace.successors(actual_node.state)
            for nodes in successors_list:
                successor_node = new TreeNode(None, 0, 0, max_depth, actual_node)
                frontier.insert(successor_node)
    if solution:
        return createSolution(actual_node)
    else:
        return None

def search(problem, strategy, max_depth, increment):
    depth = increment
    solution = None
    while (not Solution) and (depth <= max_depth):
        solution = bounded_search()
        depth = actual_depth + increment
    return solution

if __name__ == '__main__':
    main()
