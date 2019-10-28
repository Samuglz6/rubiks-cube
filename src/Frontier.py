#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bisect as bisect
#import queue as Q
#import heapq
from TreeNode import TreeNode


class Frontier:
    def __init__(self):
        self.frontier = self.create()

    def create(self):
        #frontier = []
        #heapq.heapify(frontier)
        #return frontier
        return []

    def insert(self, node):
        if isinstance(node, TreeNode):
            bisect.insort(self.frontier, (node.f, node))
            #heapq.heappush(self.frontier, (node.f, node))
        else:
            print("Not a valid node.")

    def remove(self):
        del self.frontier[0]
        #return heapq.heappop(self.frontier)


    def isEmpty(self):
        return not self.frontier
