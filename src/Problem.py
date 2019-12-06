#!/usr/bin/python3
# -*- coding: utf-8 -*-

from StateSpace import StateSpace
from Cube import Cube
from State import State


class Problem():
    def __init__(self, json):
        self.stateSpace = StateSpace(json)
        self.initial = State(Cube(self.stateSpace.json))
        self.visitedList = {}

    def isGoal(self, state):
        goal = False

        for face in state.current.faces.values():
            color = set()
            for x in range(state.current.size):
                color = color.union(set(face[x]))
            if (len(color) == 1):
                goal = True
            else:
                return False
        return goal
