#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json


class JsonManager:

    def jsonReading(self, file=None):
        if self is not None:
            with open(self, 'r') as output:
                data = json.load(output)
                output.close()
        else:
            listed_files = []

            while 1:
                print("Select the json file:")
                for self in os.listdir('../json'):
                    if os.path.splitext(self)[1] == ".json":
                        listed_files.append(os.path.splitext(self)[0])

                for item in listed_files:
                    print('-' + item)

                selected = input("Selected file:")
                if selected not in listed_files:
                    print("ERROR. Selected file is not valid.\n")
                else:
                    break

            json_file = '../json/' + selected + '.json'

            if json_file:
                with open(json_file, 'r') as output:
                    data = json.load(output)
                    output.close()

        return JsonManager.jsonChecking(data)

    def jsonWriting(self, path, name, cube):
        with open(path + name + '.json', 'w+') as file:
            file.write(json.dumps(cube.faces))
            file.close()

    def jsonComparison(self, file1, file2):

        if file1 == file2:
            print("SUCCESS")
        else:
            print("FAILURE")
            for i in range(len(file2)):
                if file1[i] != file2[i]:
                    print(i, file1[i], file2[i])

    def jsonChecking(self, data):
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
