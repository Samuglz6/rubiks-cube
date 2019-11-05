#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from Problem import Problem
from Frontier import Frontier
from TreeNode import TreeNode
from pprint import pprint

def main():
    json = "../json/x4cube.json"
    problem =  Problem(json)

    search(problem, 0, 10, 1)

    print("Solved")

def bounded_search(problem, strategy, max_depth):
    frontier =  Frontier()
    init_node =  TreeNode(problem.initial, strategy)
    frontier.insert(init_node)
    solution = False
    while (not solution) and (not frontier.isEmpty()):
        actual_node = frontier.remove()[1]
        #print(actual_node)
        if(problem.isGoal(actual_node.state)):
            solution = True
        else:
            successors_list = problem.stateSpace.successors(actual_node.state, actual_node.d,max_depth)
            for (action, state, cost) in successors_list:
                node = TreeNode(state, strategy, actual_node, cost, action)
                print("nuevo: ",node)
                frontier.insert(node)
    if solution:
        return createSolution(actual_node)
    else:
        return None

def search(problem, strategy, max_depth, increment):
    actual_depth = increment
    solution = None
    while (not solution) and (actual_depth <= max_depth):
        solution = bounded_search(problem, strategy, actual_depth)
        depth = actual_depth + increment
    return solution

if __name__ == '__main__':
    main()
