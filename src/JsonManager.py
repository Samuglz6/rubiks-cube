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
            with open(json_file, 'r') as output:
                data = json.load(output)
                output.close()

        size = len(list(data.values())[0]);
        for values in data.values():
            if len(values) != size:
                data = None

        return data

    def jsonWriting(name, cube):
        with open('../output/'+name+'.json','w+') as file:
            json.dump(cube.faces, file)
            file.close()
