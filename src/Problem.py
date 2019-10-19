#!/usr/bin/python3
# -*- coding: utf-8 -*-

from StateSpace import StateSpace
from Cube import Cube
from State import State


class Problem():
    def __init__(self, json):
        self.initial = State(Cube(json))
        self.stateSpace = StateSpace()

    def isGoal(self, state):
        goal = False
        for key in state.current.faces.keys():
            for element in state.current.faces[key]:
                if len(set(element)) == 1:
                    goal = True
                else:
                    return False
        return goal
