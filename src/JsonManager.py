#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import json

class JsonManager():
    
    def jsonReading():
        print("Select the json file:")
        for file in os.listdir('../json'):
            if os.path.splitext(file)[1] == ".json":
                print('-'+os.path.splitext(file)[0])
                
        selected = input("Selected file:")
        json_file = '../json/'+selected+'.json'     

        if json_file:
            with open(json_file) as output:
                data = json.load(output)

        return data

    def jsonWriting(name, cube):
        with open(name+'.json','w') as file:
            json.dump(cube.Faces, file)
        
