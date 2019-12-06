#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib


class State:
    def __init__(self, cube):
        self.current = cube
        self.md5 = self.generateCode()

    def generateCode(self):
        string = ''
        for value in self.current.faces.values():
            for x in value:
                string += ''.join(map(str, x))
        return hashlib.md5(string.encode('utf-8')).hexdigest()
