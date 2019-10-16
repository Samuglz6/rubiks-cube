#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import json


class JsonManager():

    def jsonReading(file=None):
        if not file == None:
            with open(file, 'r') as output:
                data = json.load(output)
                output.close()
        else:
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

        return JsonManager.jsonComprobation(data)

    def jsonWriting(path, name, cube):
        with open(path+name+'.json','w+') as file:
            file.write(json.dumps(cube.faces))
            file.close()

    def jsonComparison(file1, file2):
        #a = json.load(file1)
        #b = json.load(file2)

        if (file1 == file2):
            print("SUCCESS")
        else:
            print("FAILURE")
            for i in range(len(file2)):
                if file1[i] != file2[i]:
                    print(i, file1[i], file2[i])

    def jsonComprobation(data):
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
