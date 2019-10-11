#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import json


class JsonManager():

    def jsonReading():
        listed_files = []

        while(1):
            print("Select the json file:")
            for file in os.listdir('../json'):
                if os.path.splitext(file)[1] == ".json":
                    listed_files.append(os.path.splitext(file)[0])

            for item in listed_files:
                print('-'+item)

            selected = input("Selected file:")
            if selected not in listed_files:
                print("ERROR. Selected file is not valid.\n")
            else:
                break

        json_file = '../json/'+selected+'.json'

        if json_file:
            with open(json_file, 'r') as output:
                data = json.load(output)
                output.close()

        size = len(list(data.values())[0]);
        if len(list(data.keys())) != 6:
            data = None
        else:
            for values in data.values():
                if len(values) != size:
                    data = None
                for element in values:
                    if len(element) != size:
                        data = None

        return data

    def jsonWriting(name, cube):
        with open('../output/'+name+'.json','w+') as file:
            file.write(json.dumps(cube.faces))
            file.close()
