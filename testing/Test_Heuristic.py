#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Problem import Problem

def main():
    problem = Problem("../json/x3cube.json")

    node = TreeNode(1, problem.initial, 6, None, 1)
    print(node.getF())
    
if __name__ == '__main__':
    main()
