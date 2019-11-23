#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json
from sys import platform

class JsonManager:
    def jsonSelection():
        cwd = JsonManager.currentDirectory() + 'json/'

        while 1:
            listed_files = []
            print("Select the json file:")
            for node in os.listdir(cwd):
                if os.path.splitext(node)[1] == ".json":
                    listed_files.append(os.path.splitext(node)[0])

            for item in listed_files:
                print('-' + item)

            selected = input("Selected file:")
            if selected not in listed_files:
                print("ERROR. Selected file is not valid.\n")
            else:
                break
        path = cwd + selected + '.json'

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

    def jsonWriting(name, cube):
        path = JsonManager.currentDirectory() + 'output/'
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

    def currentDirectory():
        if platform == 'win32':
            cwd = os.getcwd().split('\\')[-1]
        else:
            cwd = os.getcwd().split('/')[-1]
        if cwd == 'src': cwd = '../'
        elif cwd == 'rubiks-cube': cwd = './'
        elif cwd == 'testing' : cwd = '../'

        return cwd
