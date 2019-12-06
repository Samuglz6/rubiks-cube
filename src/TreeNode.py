#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

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
          if strategy == 0: return self.d
          if strategy == 1: return round(1/(self.d+1),2)
          if strategy == 2: return round(1/(self.d+1),2)
          if strategy == 3: return round(1/(self.d+1),2)
          if strategy == 4: return self.pathCost
          if strategy == 5: return self.pathCost+self.calculateHeuristic()
          if strategy == 6: return self.calculateHeuristic()

    def getF(self):
        return self.f

    def calculateHeuristic(self):
        h = 0
        entropy = {"BACK": 0,"DOWN": 0,"FRONT": 0,"LEFT": 0,"RIGHT": 0,"UP": 0}
        N = self.state.current.size

        #As we are going to calculate for each face we set a for loop
        for face in self.state.current.faces:
            counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0} #nº of colors in a face

            #Now we get the number of tiles of each color for a specific face
            for list in self.state.current.faces[face]:
                for color in list:
                    counter[color] += 1

            #calculation of the entropy for each face
            for c in range(6):
                if counter[c] > 0.0:
                    entropy[face] = entropy[face] + counter[c]/(N*N) * math.log(counter[c]/((N)*(N)),6)

        #Addition of the entropy of each face in order to calculate h
        for face in entropy:
            h += abs(entropy[face])

        return round(h,2)
