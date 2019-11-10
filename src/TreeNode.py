#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random


class TreeNode:
    def __init__(self, state, strategy, parent=None, cost=0, action=None, depth=0):
        self.parent = parent
        self.state = state
        if parent is not None:
            self.pathCost = parent.pathCost+cost
            self.d = parent.d+1
        else:
            self.pathCost = cost
            self.d = depth
        self.action = action
        self.f = self.selection(strategy)

    def selection(self, strategy):
        switch = {0: self.d , 1: -(self.d), 2: '', 3: '', 4: self.pathCost}
        return switch[strategy]

    def getF(self):
        return self.f
