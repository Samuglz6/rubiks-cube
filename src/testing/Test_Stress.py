#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
sys.path.append('../')

from TreeNode import TreeNode
from State import State
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager
import time

def main():
    problem = Problem(jManager.jsonReading("../../json/x4cube.json"))
    fringe = Frontier()

    start = time.time()
    stress_test(problem, fringe)
    print("Total time: %.11f" % (time.time()-start))

def stress_test(p,f):
    total_nodes = 0
    t_avg = 0
    t_max = 0
    t_min = 9999
    try:
        while True:
            try:
                if(total_nodes == 0): node = TreeNode(p.initial,0,0,total_nodes)
                else: node = TreeNode(p.initial, 0,0,total_nodes)

                init_time = time.time()
                f.insert(node)
                end_time = time.time()
                total_nodes+=1
                current_time = (end_time - init_time)
                t_avg += current_time
                if(current_time > t_max): t_max = current_time
                if(current_time < t_min): t_min = current_time
            except MemoryError:
                print("Memory Full")
                printData(t_avg, t_max, t_min, total_nodes)
    except KeyboardInterrupt:
        print("Test has been interrupted")
        printData(t_avg, t_max, t_min, total_nodes)

def printData(avg, max, min, total):
    print("Average time: %.11f" % (avg/total))
    print("Max time; %.11f" % max)
    print("Min time: %.11f" % min)
    print("Total elements: %d" % total)

if __name__ == '__main__':
    main()
