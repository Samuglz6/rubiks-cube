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

    def movel0(self):
        self.Faces["LEFT"] = np.rot90(self.Faces["LEFT"],2).tolist()
