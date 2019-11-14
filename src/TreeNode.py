#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random


class TreeNode:
    def __init__(self, id, state, strategy, parent=None, cost=0, action=None, depth=0):
        self.id = id
        self.parent = parent
        self.state = state
        if self.parent is not None:
            self.pathCost = self.parent.pathCost+cost
            self.d = self.parent.d+1
        else:
            self.pathCost = cost
            self.d = depth
        self.action = action
        self.f = self.selection(strategy)

    def selection(self, strategy):
        switch = {0: self.d , 1: -(self.d), 2: '', 3: '', 4: self.pathCost, 5: '', 6: ''}
        return switch[strategy]

    def getF(self):
        return self.f
