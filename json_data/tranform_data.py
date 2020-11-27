import json
import os; import io
import time

#This file is used to unspool and transorm the json data into usable sql or json files using my own format



def clean_files():
    files = []
    for file in os.listdir("raw_data"):
        print(file)
        files.append(file)
    #Relevant objects only contains objects with entries
    relevant_objects = []
    for json_file in files:
        file_path = 'raw_data/{}'.format(json_file)

        print("raw_data/{}".format(json_file))

        f = open(file_path, encoding='utf-8')
        print("IO Wrapper is", f)
        data = json.load(f)
        #print(data)
        #print("Printing keys - " , data.keys())
        #Should only load the first key
        json_key = list(data.keys())[0]
        print("Main Json Key is - ", json_key)
        simplified_data = data[json_key]
        #print(simplified_data)
        print(simplified_data[0])
        for k in simplified_data:
            print("Json part starts here: {} {}".format(json_file, k))
            try:
                print("****** - ", k["entries"])
            except:
                pass
        #TODO: go down the line in similar fashion and extract data, make dictionary of dictionaries that contain useful information,
        # like descriptions of objects or backgrounds and export to YAML file



#Doot DOOT

clean_files()