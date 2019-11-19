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
        switch = {0: self.d , 1: round(1/(self.d+1), 3), 2: '', 3: '', 4: self.pathCost, 5: self.pathCost+self.calculateHeuristic(), 6: self.calculateHeuristic()}
        return switch[strategy]

    def getF(self):
        return self.f

    def calculateHeuristic(self):
        entropy = {"BACK": 0,"DOWN": 0,"FRONT": 0,"LEFT": 0,"RIGHT": 0,"UP": 0}

        counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        '''for face, value in state.current.faces.items():
            for element in value:
                entropy = 0



            for c in range(6):
                if counter[c] > 0.0:
                    entropy[face] = entropy[face] + counter[c]/(N*N) * math.log(counter[c]/(N*N),6)'''

        return 1
