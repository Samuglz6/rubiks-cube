#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import json

class JsonManager():
    
    def jsonReading():
        for file in os.listdir('.'):
            '''if os.path.splitext(file)[1] == ".json":'''
            if file == "cube.json":
                json_file = file

        if json_file:
            with open(json_file) as output:
                data = json.load(output)

        return data

    def jsonWriting(name, cube):
        with open(name+'.json','w') as file:
            json.dump(cube.Faces, file)
        
