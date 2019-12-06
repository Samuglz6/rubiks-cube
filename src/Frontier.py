#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TreeNode import TreeNode
from sortedcontainers import SortedKeyList


class Frontier:
    def __init__(self):
        self.frontier = self.create()

    def create(self):
        return SortedKeyList(key=TreeNode.getF)

    def insert(self, node):
        if isinstance(node, TreeNode):
            self.frontier.add(node)
        else:
            print("Not a valid node.")

    def remove(self):
        return self.frontier.pop(0)

    def isEmpty(self):
        return not self.frontier
