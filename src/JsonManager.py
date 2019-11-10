#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json


class JsonManager:
    def jsonSelection():
        while 1:
            listed_files = []
            print("Select the json file:")
            for node in os.listdir('../json'):
                if os.path.splitext(node)[1] == ".json":
                    listed_files.append(os.path.splitext(node)[0])

            for item in listed_files:
                print('-' + item)

            selected = input("Selected file:")
            if selected not in listed_files:
                print("ERROR. Selected file is not valid.\n")
            else:
                break
        path = '../json/' + selected + '.json'

        return path

    def jsonReading(file=None):
        data = None
        if file is None: file = JsonManager.jsonListing()
        try:
            with open(file, 'r') as output:
                data = json.load(output)
                output.close()
        except:
            print("READING ERROR. The introduced file doesn't exist.")

        return JsonManager.jsonChecking(data)

    def jsonWriting(path, name, cube):
        with open(path + name + '.json', 'w+') as file:
            file.write(json.dumps(cube.faces))
            file.close()

    def jsonComparison(file1, file2):
        if file1 == file2:
            print("SUCCESS")
        else:
            print("FAILURE")
            for i in range(len(file2)):
                if file1[i] != file2[i]:
                    print(i, file1[i], file2[i])

    def jsonChecking(data):
        if data is not None:
            size = len(list(data.values())[0])
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
