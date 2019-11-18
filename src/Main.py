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

    solution = []

    print("Searching for the solution...")
    start = time.time()
    node = search(problem, strategy, max_depth, increment, pruning)
    print("Searching time: %.11f s" % (time.time() - start))

    print("\nGenerating the solution...")
    generateSol(solution, node)
    writeSolution(solution, node)

def askData():
    json = jManager.jsonSelection()

    switch = {0: ['Breath First Search', 'BFS'], 1: ['Depth First Search', 'DFS'], 2:
    ['Depth Limited Search', 'DLS'], 3: ['Iterative Deepening Search', 'IDS'],
    4: ['Uniform Cost Search', 'UCS'], 5: 'A*', 6: 'Greedy'}

    while 1:
        print("\nSelect now the searching strategy:")
        for element in switch.keys():
            if(element < 5):
                print(element,' - ',switch.get(element)[0], '(',switch.get(element)[1],')')
            else:
                print(element, ' - ', switch.get(element))

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
        max_depth = 20

    if strategy == 3 or strategy in switch.get(3):
        increment = input("Specify the increment: ")
    else: increment = 1

    return strategy, pruning, json, max_depth, increment


def bounded_search(problem, strategy, actual_depth, max_depth, pruning, total_nodes):
    frontier =  Frontier()
    init_node =  TreeNode(total_nodes, problem.initial, strategy)
    frontier.insert(init_node)
    total_nodes += 1
    solution = False
    while (not solution) and (not frontier.isEmpty()):
        actual_node = frontier.remove()

        if(problem.isGoal(actual_node.state)):
            solution = True
        else:
            successors_list = problem.stateSpace.successors(actual_node.state, actual_node.d, max_depth)
            node_list = []
            for (action, state, cost) in successors_list:
                node = TreeNode(total_nodes, state, strategy, actual_node, cost, action)
                node_list.append(node)
            if pruning == 1:
                for node in node_list:
                    if node.state.md5 not in problem.visitedList:
                        frontier.insert(node)
                        total_nodes += 1
                        problem.visitedList[node.state.md5] = node.f
                    elif node.f < problem.visitedList[node.state.md5]:
                        frontier.insert(node)
                        total_nodes += 1
                        problem.visitedList[node.state.md5] = node.f
            else:
                for node in node_list:
                    frontier.insert(node)
                    total_nodes += 1


    if solution:
        return actual_node
    else:
        return None

def search(problem, strategy, max_depth, increment, pruning):
    actual_depth = increment
    total_nodes = 0
    solution = None
    while (not solution) and (actual_depth <= max_depth):
        solution = bounded_search(problem, strategy, actual_depth, max_depth, pruning, total_nodes)
        depth = actual_depth + increment
    return solution

def generateSol(solution, node):
    if(node.parent is None):
        solution.append("["+str(node.id)+"](["+str(node.action)+"]"+str(node.state.md5)+", cost = "+str(node.pathCost)+", depth = "+str(node.d)+", f = "+str(node.f)+")")
    else:
        generateSol(solution, node.parent)
        solution.append("["+str(node.id)+"](["+str(node.action)+"]"+str(node.state.md5)+", cost = "+str(node.pathCost)+", depth = "+str(node.d)+", f = "+str(node.f)+")")

def writeSolution(solution, node):
    if node is not None:
        print("A solution has been found.")
        print("The solution has been saved: rubiks-cube/output/solution.txt")
        print("You can also check the result of the faces: rubiks-cube/output/solution.json ")
    else:
        print("No solution found.")

    jManager.jsonWriting('solution', node.state.current)

    with open(jManager.currentDirectory()+"output/solution.txt", "w+") as text_file:
        text_file.write('\n'.join([element for element in solution]))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("The program has been interrupted.")

    print("Program has finished.")
