#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager

class StateSpace:
    def __init__(self, json):
        self.path = json
        self.json = jManager.jsonReading(self.path)

    def successors(state, depth, x):
        nodes = []
        if depth == x:
            return []
        else:
            for move in state.cube.validMovements:
                newState = (state.cube.clone)
                acc = move
                costAct = 1
                print(acc, newState, costAct)
            return nodes
