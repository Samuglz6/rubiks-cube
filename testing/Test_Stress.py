#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager
import time


def main():
    problem = Problem("../json/x4cube.json")
    fringe = Frontier()

    print("Starting test... ")
    start = time.time()
    stress_test(problem, fringe)
    print("Total time: %.11f" % (time.time() - start))
    print("\nStress test has ended.")


def stress_test(p, f):
    total_nodes = 0
    t_avg = 0
    t_max = 0
    t_min = 9999

    print("Test is running (Press Ctrl+C to abort).\n")
    try:
        while True:
            try:
                if total_nodes == 0:
                    node = TreeNode(p.initial, 0, None, total_nodes)
                else:
                    node = TreeNode(p.initial, 0, None, total_nodes)
                init_time = time.time()
                f.insert(node)
                end_time = time.time()
                total_nodes += 1
                current_time = end_time - init_time
                t_avg += current_time
                if current_time > t_max: t_max = current_time
                if current_time < t_min and current_time != 0:
                    t_min = current_time

            except MemoryError:
                print("Memory Full")
                printData(t_avg, t_max, t_min, total_nodes)
                sys.exit(1)
    except KeyboardInterrupt:
        print("Test has been interrupted\n")
        printData(t_avg, t_max, t_min, total_nodes)


def printData(avg, t_max, t_min, total):
    print("-------------------------------")
    print("Average time: %.15f" % (avg / total))
    print("Max time; %.15f" % t_max)
    print("Min time: %.15f" % t_min)
    print("-------------------------------")
    print("\nTotal elements: %d" % total)


if __name__ == '__main__':
    main()
