import json
import os; import io
import time

#This file is used to unspool and transorm the json data into usable sql or json files using my own format



def clean_files():
    files = []
    for file in os.listdir("raw_data"):
        print(file)
        files.append(file)

    for json_file in files:
        file_path = 'raw_data/{}'.format(json_file)

        print("raw_data/{}".format(json_file))
        print("*"*5)
        f = open(file_path, encoding='utf-8')
        print("there", f)
        data = json.load(f)
        print(data)
        print(data["backgroundFluff"])


clean_files()