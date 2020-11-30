import json
import os; import io
import time
import yaml

#This file is used to unspool and transorm the json data into usable sql or json files using my own format



def clean_files():
    files = []
    for file in os.listdir("raw_data"):
        print(file)
        files.append(file)
    #Relevant objects only contains objects with entries
    relevant_objects = []
    json_file_names = {}
    for json_file in files:
        file_path = 'raw_data/{}'.format(json_file)

        print("raw_data/{}".format(json_file))

        f = open(file_path, encoding='utf-8')
        print("IO Wrapper is", f)
        data = json.load(f)
        print("Data starts here ... " , data)
        if "fluff" in json_file:
            #Fluff files first object contain all info
            #print(json_file)
            json_key = list(data.keys())[0]
        else:
            #Non fluff files contain metadata in first position, aka 0
            #print("Not fluff file")
            json_key = list(data.keys())[1]
        try:
            data.pop("_meta", None)
            convert_to_yaml(data, file_path)
        except:
            pass
        #print(data)
        #print(data)
        #print("Printing keys - " , data.keys())
        #Should only load the first key

        #print("Main Json Key is - ", json_key)
        target_data = data[json_key]
        print(type(target_data))
        #print(target_data)
        #print("Simplified data stream , ", target_data[0])
        #print("name aquisition ", target_data[0]["name"])
        key_list = []
        for k in target_data:
            #print("Json part starts here: {} {}".format(json_file, k))
            try:
                key_list.append(k["name"])
                d = {json_key: key_list}
                json_file_names.update(d)
                #print("****** - ", k["entries"])
            except:
                pass
        #TODO: go down the line in similar fashion and extract data, make dictionary of dictionaries that contain useful information,
        # like descriptions of objects or backgrounds and export to YAML file
    print(json_file_names)

def convert_to_yaml(json_file, old_path):
    #TODO: Ensure yaml file is not alphabetically loaded
    file_name = old_path.split("/")[1]
    file_name = file_name.split(".")[0]
    #Splits filename at slash and keeps last bit, then splits on . and keeps regular name
    print("File name is : ", file_name)
    new_path = "cleaned_data/{}".format(file_name)
    print(new_path)
    with open("{}.yaml".format(new_path), "w+") as f:
        dump = yaml.dump(json_file, f, default_flow_style=False, sort_keys=False)
        print("Successfully transformed {} with {}".format(file_name, dump))

def load_yaml():

    for file in os.listdir("cleaned_data"):
        print(file)
        with open("cleaned_data/{}".format(file), "r") as out:
            output = yaml.safe_load(out)
            print(output)





load_yaml()