import os
import time

import yaml
import json


def create_store_combined_file_yaml():
    #Creates two directories inside of cleaned data, one for regular stores, the other for "adventurer" stores (aka. blacksmith, alchemist ect.)
    print("Creating store data")
    if not os.path.exists("cleaned_data/citizen_store_data") and not os.path.exists("cleaned_data/hero_store_data"):
        os.mkdir("cleaned_data/citizen_store_data")
        os.mkdir("cleaned_data/hero_store_data")
    else:
        print("Directories already exist")

    print("Reading relevant data")
    path = "raw_pathfinder_data/store_data"
    relevant_data_list = os.listdir(path)
    path_list = []
    irrelevant_list = ["itemcategories.yaml", "items-staves.yaml", "weapongroups.yaml"]
    for i in relevant_data_list:
        if i not in irrelevant_list:
            print(i,"\n", path)
            x = "{}/{}".format(path, i)
            print(x)
            path_list.append(x)
    print(path_list, "\n",type(path_list))
    #The appended value lays inside of a different directory
    path_list.append("cleaned_data/items.yaml")

    relevant_data = path_list
    print(relevant_data)

    #TODO: go through each file and try to standardise item tags, use this to create two files which hold data about
    # both types of stores to be used in conjunction with store_class.py
    path_items_details = {}
    for path_item in path_list[2:-1]:
        with open(path_item, "r+") as f:
            print(f)

            store_file = yaml.safe_load(f)
            print(store_file)
            print(store_file.keys())
            print(next(iter(store_file.values())))
            list_of_dicts = next(iter(store_file.values()))
            print(len(list_of_dicts))
            item_list = [f, len(list_of_dicts), ]
            path_items_details["{}_itemlist".format(path_item)] = item_list
            print("\n"*10)
            time.sleep(10)
    #explore_differences(relevant_data)



def explore_differences(difference_list):
    with open(difference_list[-1], "r+", encoding="utf-8") as file_1:
        regular_yaml = yaml.safe_load(file_1)
    with open(difference_list[-2], "r+", encoding="utf-8") as file_2:
        json_translated_yaml = yaml.safe_load(file_2)
    #print(regular_yaml, "\n*\n"*5, json_translated_yaml)
    print(regular_yaml.keys())
    regular_yaml = regular_yaml["items"]
    head = [i for i in regular_yaml][0:10]
    print(list(enumerate(head)), sep="\n")
    print(json_translated_yaml.keys())


create_store_combined_file_yaml()