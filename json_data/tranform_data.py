import json
import os

#This file is used to unspool and transorm the json data into usable sql or json files using my own format
def clean_files():
    files = []
    for file in os.listdir("raw_data"):
        print(file)
        files.append(file)
    for json_file in files:
        with open("raw_data\{}".format(json_file), "r") as f:
            print("raw_data/{}".format(json_file))
            print(f)
            data = f.read()
            print(data)

clean_files()