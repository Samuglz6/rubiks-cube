#!/usr/bin/python3
# -*- coding: utf-8 -*-


from TreeNode import TreeNode


class Frontier:
    def __init__(self):
        self.frontier = self.create()

    def create(self):
        return []

    def useFirst(self, element):
        return element[0]

    def insert(self, node):
        if isinstance(node, TreeNode):
            self.frontier.append((node.f, node))
            sorted(self.frontier, key=self.useFirst)

        else:
            print("Not a valid node.")

    def remove(self):
        self.frontier.pop(0)

    def isEmpty(self):
        return not self.frontier
