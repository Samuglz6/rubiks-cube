#!/usr/bin/python3
#-*- coding: utf-8 -*-

import hashlib

class Cube():
    def __init__(self,json):
        self.Left = json.get("LEFT")
        self.Back = json.get("BACK")
        self.Down = json.get("DOWN")
        self.Front = json.get("FRONT")
        self.Right = json.get("RIGHT")
        self.Up = json.get("UP")
        self.md5 = self.generateMD5(json)

    def generateMD5(self, json):
        cadena = ''
        for value in json.values():
            for x in value:
                cadena += ''.join(map(str,x))
        md5 = hashlib.md5(cadena.encode('utf-8')).hexdigest()

        return md5
