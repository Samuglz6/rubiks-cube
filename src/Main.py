#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, time

from JsonManager import JsonManager as jManager
from Problem import Problem
from Frontier import Frontier
from TreeNode import TreeNode
from pprint import pprint

def main():

    strategy, pruning, json, max_depth, increment = askData()
    problem =  Problem(json)

    #automatic()

    print("Finding solution...")
    search(problem, strategy, max_depth, increment, pruning)
    print("Program finished...")


def automatic():
    problem = Problem("../json/x2cube.json")
    search(problem, 0, 99, 1, 1)

def askData():
    json = jManager.jsonSelection()

    switch = {0: ['Breath First Search', 'BFS'], 1: ['Depth First Search', 'DFS'], 2:
    ['Depth Limited Search', 'DLS'], 3: ['Iterative Deepening Search', 'IDS'],
    4: ['Uniform Cost Search', 'UCS']}

    while 1:
        print("\nSelect now the searching strategy:")
        for element in switch.keys():
            print(element,' - ',switch.get(element)[0], '(',switch.get(element)[1],')')

        strategy = input("Selection: ")

        if strategy.isdigit():
            strategy = int(strategy)
            if strategy not in switch:
                print("ERROR. The number introduced is not valid.")
            else: break
        else:
            print("ERROR. The introduced strategy is not valid")


    while 1:
        pruning = input("Do you want to pruning? (y/n)\n")

        if pruning == 'y' or pruning == 'yes':
            pruning = 1
            break
        elif pruning == 'n' or pruning == 'no':
            pruning = 0
            break
        else: print("ERROR. The answer is not valid. You can use: yes/y or no/n.")

    if strategy == 2 or strategy in switch.get(2):
        max_depth = int(input("Choose the maximum depth: "))
    else:
        max_depth = 999

    if strategy == 3 or strategy in switch.get(3):
        increment = input("Specify the increment: ")
    else: increment = 1

    return strategy, pruning, json, max_depth, increment


def bounded_search(problem, strategy, max_depth, pruning):
    frontier =  Frontier()
    init_node =  TreeNode(problem.initial, strategy)
    frontier.insert(init_node)
    solution = False
    while (not solution) and (not frontier.isEmpty()):
        actual_node = frontier.remove()
        print(actual_node.state.md5)
        if(problem.isGoal(actual_node.state)):
            solution = True
        else:
            successors_list = problem.stateSpace.successors(actual_node.state, actual_node.d, max_depth)
            node_list = []
            for (action, state, cost) in successors_list:
                node = TreeNode(state, strategy, actual_node, cost, action)
                node_list.append(node)
            if pruning == 1:
                for node in node_list:
                    if node.state.md5 not in problem.visitedList:
                        frontier.insert(node)
                        problem.visitedList[node.state.md5] = node.f
                        print("nuevo visitado")
                    elif node.f < problem.visitedList[node.state.md5]:
                        frontier.insert(node)
                        problem.visitedList[node.state.md5] = node.f
                        print("mejorado")
            else:
                for node in node_list:
                    frontier.insert(node)

    if solution:
        return actual_node
    else:
        return None

def search(problem, strategy, max_depth, increment, pruning):
    actual_depth = increment
    solution = None
    while (not solution) and (actual_depth <= max_depth):
        solution = bounded_search(problem, strategy, actual_depth, pruning)
        depth = actual_depth + increment
    return solution

if __name__ == '__main__':

    main()
