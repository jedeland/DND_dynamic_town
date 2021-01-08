import os
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
    for i in relevant_data_list:
        print(i,"\n", path)
        x = "{}/{}".format(path, i)
        print(x)
        path_list.append(x)
    print(path_list, "\n",type(path_list))
    path_list.append("cleaned_data/items.yaml")
    relevant_data = path_list
    print(relevant_data)


create_store_combined_file_yaml()