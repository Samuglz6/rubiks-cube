#!/usr/bin/python3
#-*- coding: utf-8 -*-

import hashlib
import numpy as np

class Cube():
    def __init__(self,json):
        self.Faces = json
        self.md5 = self.generateMD5()

    def generateMD5(self):
        cadena = ''
        for value in self.Faces.values():
            for x in value:
                cadena += ''.join(map(str,x))
        md5 = hashlib.md5(cadena.encode('utf-8')).hexdigest()

        return md5

    def moveL0(self):
        self.Faces["LEFT"] = np.rot90(self.Faces["LEFT"]).tolist()
        self.md5 = self.generateMD5()

    def movel0(self):
        self.Faces["LEFT"] = np.rot90(self.Faces["LEFT"],-1).tolist()
        self.md5 = self.generateMD5()

    def moveD0(self):
        self.Faces["DOWN"] = np.rot90(self.Faces["DOWN"]).tolist()
        self.md5 = self.generateMD5()

    def moved0(self):
        self.Faces["DOWN"] = np.rot90(self.Faces["DOWN"],-1).tolist()
        self.md5 = self.generateMD5()

    def moveB0(self):
        self.Faces["BACK"] = np.rot90(self.Faces["BACK"]).tolist()
        self.md5 = self.generateMD5()

    def moveb0(self):
        self.Faces["BACK"] = np.rot90(self.Faces["BACK"],-1).tolist()
        self.md5 = self.generateMD5()
