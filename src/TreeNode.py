#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random


class TreeNode:
    def __init__(self, state, cost, action, depth, parent=None):
        self.parent = parent
        self.state = state
        self.pathCost = cost
        self.action = action
        self.d = depth
        self.f = random.random() * 10000
        
