#!/usr/bin/python3
# -*- coding: utf-8 -*-


from TreeNode import TreeNode


class Frontier:
    def __init__(self):
        self.frontier = self.create()

    def create(self):
        return []

    def insert(self, node):
        if isinstance(node, TreeNode):
            self.frontier.append()
        else:
            print("Not a valid node.")

    def remove(self):
        self.frontier.pop(0)

    def isEmpty(self):
        return not self.frontier
