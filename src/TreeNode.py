#!/usr/bin/python3
#-*- coding: utf-8 -*-

class TreeNode():
    def __init__(self, parent = None, state, cost, action, depth):
        self.parent = parent
        self.state = state
        self.pathCost = cost
        self.action = action
        self.d = depth
        self.f = random.randrange(1000000)
