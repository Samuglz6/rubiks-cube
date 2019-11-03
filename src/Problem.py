#!/usr/bin/python3
# -*- coding: utf-8 -*-

from StateSpace import StateSpace
from Cube import Cube
from State import State


class Problem():
    def __init__(self, json):
        self.stateSpace = StateSpace(json)
        self.initial = State(Cube(self.stateSpace.json))

    def isGoal(self, state):
        goal = False
        goal_conditions = {'BACK': 3,'LEFT': 4, 'DOWN': 1, 'RIGHT': 5, 'UP': 0, 'FRONT': 2}

        for face in state.current.faces.keys():
            for element in state.current.faces[face]:
                color = set(element)
                if (len(color) == 1) and (next(iter(color)) == goal_conditions[face]):
                    goal = True
                else:
                    return False
        return goal
