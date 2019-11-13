#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from TreeNode import TreeNode
from State import State
from pprint import pprint

class StateSpace:
    def __init__(self, json):
        self.path = json
        self.json = jManager.jsonReading(self.path)

    def successors(self, state, depth, x):
        nodes = []
        if depth == x:
            return []
        else:
            for move in state.current.validMovements():
                aux = State(state.current.clone())
                method = getattr(aux.current, move[0])
                method(int(move[1]))
                newState = State(aux.current)
                acc = move
                costAct = 1
                nodes.append((acc, newState, costAct))
            return nodes
