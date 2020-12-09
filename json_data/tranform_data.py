import json
import os; import io
import time
import yaml
import re

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

def translate_json():
    print("Trying to simplify json data")
    if os.path.exists("translated_data"):
            print("moving files to translated_data")
    else:
        try:
            os.mkdir("translated_data")
        except:
            print("Already exists")
    for file in os.listdir("raw_data"):
        print(file)
        f =  open("raw_data/{}".format(file), encoding="UTF-8")
        json_version = json.load(f)
        try:
            json_version.pop("_meta", None)
        except:
            pass
        json_key = list(json_version.keys())[0]
        json_onedown = json_version[json_key]
        #print(json_onedown)
        print(type(json_onedown), len(json_onedown))
        if "deities" in file and not os.path.exists("translated_data/deities.json"):
            deities_translation(file, json_onedown)
        elif "items" in file and os.path.exists("translated_data/items.json"):
            items_translation(file, json_onedown)

        #TODO: Add tags to each object in list, to make the object more readable in yaml format
        # Example: { "god_type" : "NAME-SOURCE-RACE" {'name': 'Abbathor', 'source': 'SCAG', 'page': 22, 'pantheon': 'Dwarven', 'alignment': ['N', 'E'], 'title': 'God of greed', 'domains': ['Trickery'], 'symbol': 'Jeweled dagger, point-down'}}
        #print(json_version[json_key])
        print("*\n"*5)

def items_translation(file, json_data):
    #Using a standardised translation service is ineffective, as the json files are formatted differently
    print("translating items")
    json_items_list = {"items" : []}
    for i in json_data:
        if "entries" in i:
            print("Json dict - {}".format(i))
            print(type(i))
        try:
            clean_name = re.sub(r'[^A-Za-z ]+', '', i["name"])
            clean_name = clean_name.replace("'", "")
            clean_name = re.sub(r"^\s", "", clean_name)
            print("Cleaned name {} - Old name {}".format(clean_name, i["name"]))
            i = {"item_code": "{}_{}_{}".format(clean_name.replace(" ", "-"), i["source"], i["rarity"].replace(" ", "-")).upper(), "item_info": i}
            json_items_list["items"].append(i)
        except Exception as e:
            print("Exception is " , e)
            pass
    print(json_items_list)
    if "items" in file:
        with open("translated_data/items.json", "w+") as f:
            print("writing to items.json")
            print(json_items_list)
            json.dump(json_items_list, f)

def deities_translation(file, json_onedown):
    json_deities_list = {"deities": []}
    # TODO: Refactor sub functions into specific translation cases
    for i in json_onedown:

        if "entries" in i:
            print("Json dict - {}".format(i))
            print(type(i))
        i = {"god_code": "{}_{}_{}".format(i["name"], i["source"], i["pantheon"]).upper(), "god_info": i}
        print(i)
        print(json_deities_list["deities"])
        print(type(json_deities_list["deities"]))
        json_deities_list["deities"].append(i)
    print(json_deities_list)
    if "deities" in file:
        with open("translated_data/deities.json", "w+") as f:
            print("writing to deities.json")
            print(json_deities_list)
            json.dump(json_deities_list, f)


translate_json()