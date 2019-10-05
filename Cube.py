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
   
    def b(self, num):
        
        if num == 0: self.Faces["BACK"] = np.rot90(self.Faces["BACK"]).tolist()
        if num == 2: self.Faces["FRONT"] = np.rot90(self.Faces["FRONT"]).tolist()
        
        for x in range(3):
            bubble = self.Faces["LEFT"][num][x]
            self.Faces["LEFT"][num][x] = self.Faces["UP"][num][x]
            self.Faces["UP"][num][x] = self.Faces["RIGHT"][num][x]
            self.Faces["RIGHT"][num][x] = self.Faces["DOWN"][num][x]
            self.Faces["DOWN"][num][x] = bubble

        self.md5 = self.generateMD5()

    def B(self, num):
        if num == 0: self.Faces["BACK"] = np.rot90(self.Faces["BACK"],-1).tolist()
        if num == 2: self.Faces["FRONT"] = np.rot90(self.Faces["FRONT"],-1).tolist()
        
        for x in range(3):
            bubble = self.Faces["LEFT"][num][x]
            self.Faces["LEFT"][num][x] = self.Faces["DOWN"][num][x]
            self.Faces["DOWN"][num][x] = self.Faces["RIGHT"][num][x]
            self.Faces["RIGHT"][num][x] = self.Faces["UP"][num][x]
            self.Faces["UP"][num][x] = bubble
        
        self.md5 = self.generateMD5()
