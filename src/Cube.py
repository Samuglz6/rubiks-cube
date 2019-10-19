#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import numpy as np
import copy


class Cube:
    def __init__(self, json):
        self.size = len(list(json.values())[0])
        self.faces = json
        self.md5 = self.generateCode()

    def generateCode(self):
        string = ''
        for value in self.faces.values():
            for x in value:
                string += ''.join(map(str, x))

        md5 = hashlib.md5(string.encode('utf-8')).hexdigest()

        return md5

    def clone(self):
        return copy.copy(self)

    def b(self, num):

        if num == 0:
            self.faces["BACK"] = np.rot90(self.faces["BACK"]).tolist()
        if num == self.size - 1:
            self.faces["FRONT"] = np.rot90(self.faces["FRONT"]).tolist()

        for x in range(self.size):
            bubble = self.faces["LEFT"][num][x]
            self.faces["LEFT"][num][x] = self.faces["UP"][num][x]
            self.faces["UP"][num][x] = self.faces["RIGHT"][num][x]
            self.faces["RIGHT"][num][x] = self.faces["DOWN"][num][x]
            self.faces["DOWN"][num][x] = bubble

        self.generateCode()

    def B(self, num):
        if num == 0:
            self.faces["BACK"] = np.rot90(self.faces["BACK"], -1).tolist()
        if num == self.size - 1:
            self.faces["FRONT"] = np.rot90(self.faces["FRONT"], -1).tolist()

        for x in range(self.size):
            bubble = self.faces["LEFT"][num][x]
            self.faces["LEFT"][num][x] = self.faces["DOWN"][num][x]
            self.faces["DOWN"][num][x] = self.faces["RIGHT"][num][x]
            self.faces["RIGHT"][num][x] = self.faces["UP"][num][x]
            self.faces["UP"][num][x] = bubble

        self.generateCode()

    def L(self, num):
        if num == 0:
            self.faces["LEFT"] = np.rot90(self.faces["LEFT"], -1).tolist()
        if num == self.size - 1:
            self.faces["RIGHT"] = np.rot90(self.faces["RIGHT"], -1).tolist()

        for x in range(self.size):
            bubble = self.faces["FRONT"][x][num]
            self.faces["FRONT"][x][num] = self.faces["UP"][(self.size - 1) - x][(self.size - 1) - num]
            self.faces["UP"][(self.size - 1) - x][(self.size - 1) - num] = self.faces["BACK"][x][num]
            self.faces["BACK"][x][num] = self.faces["DOWN"][x][num]
            self.faces["DOWN"][x][num] = bubble

        self.generateCode()

    def l(self, num):
        if num == 0:
            self.faces["LEFT"] = np.rot90(self.faces["LEFT"]).tolist()
        if num == self.size - 1:
            self.faces["RIGHT"] = np.rot90(self.faces["RIGHT"]).tolist()

        for x in range(self.size):
            bubble = self.faces["FRONT"][x][num]
            self.faces["FRONT"][x][num] = self.faces["DOWN"][x][num]
            self.faces["DOWN"][x][num] = self.faces["BACK"][x][num]
            self.faces["BACK"][x][num] = self.faces["UP"][(self.size - 1) - x][(self.size - 1) - num]
            self.faces["UP"][(self.size - 1) - x][(self.size - 1) - num] = bubble

        self.generateCode()

    def D(self, num):
        if num == 0:
            self.faces["DOWN"] = np.rot90(self.faces["DOWN"], -1).tolist()
        if num == self.size - 1:
            self.faces["UP"] = np.rot90(self.faces["UP"], -1).tolist()

        for x in range(self.size):
            bubble = self.faces["FRONT"][num][x]
            self.faces["FRONT"][num][x] = self.faces["RIGHT"][(self.size - 1) - x][num]
            self.faces["RIGHT"][(self.size - 1) - x][num] = self.faces["BACK"][(self.size - 1) - num][
                (self.size - 1) - x]
            self.faces["BACK"][(self.size - 1) - num][(self.size - 1) - x] = self.faces["LEFT"][(self.size - 1) - num][
                (self.size - 1) - x]
            self.faces["LEFT"][x][(self.size - 1) - num] = bubble

        self.generateCode()

    def d(self, num):
        if num == 0:
            self.faces["DOWN"] = np.rot90(self.faces["DOWN"]).tolist()
        if num == self.size - 1:
            self.faces["UP"] = np.rot90(self.faces["UP"]).tolist()

        for x in range(self.size):
            bubble = self.faces["FRONT"][num][x]
            self.faces["FRONT"][num][x] = self.faces["LEFT"][x][(self.size - 1) - num]
            self.faces["LEFT"][x][(self.size - 1) - num] = self.faces["BACK"][(self.size - 1) - num][
                (self.size - 1) - x]
            self.faces["BACK"][(self.size - 1) - num][(self.size - 1) - x] = self.faces["RIGHT"][(self.size - 1) - x][
                num]
            self.faces["RIGHT"][(self.size - 1) - x][num] = bubble

        self.generateCode()
