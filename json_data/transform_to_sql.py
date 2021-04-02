import json
import os
from pprint import pprint
import yaml
import sqlite3
import pandas

def separate_values():
    print("separating values")
    if not os.path.exists("sql_prep_data"):
        os.mkdir("sql_prep_data")
    skip_list = ["races.yaml", "region_modifiers.yaml", "languages.yaml"]
    yaml_dicts = {}
    for i in os.listdir("cleaned_data"):
        if ".yaml" in i and i not in skip_list:
            print(i)
            with open("cleaned_data/{}".format(i), "r+") as f:

                yaml_file = yaml.safe_load(f)
                print(yaml_file.keys())
                new_yaml_file = yaml_file[list(yaml_file.keys())[0]]
                yaml_dicts[i] = new_yaml_file
                print(len(new_yaml_file))
    return yaml_dicts

def deconstruct_deities(yaml_file):
    print("")
    print(type(yaml_file))
    print(len(yaml_file))
    fantasy_deities = yaml_file.copy()
    bad_list = ["greek", "egyptian", "norse", "celtic", "egw", "erlw", "mot", "theros"]
    sources_set = set()
    for i in yaml_file:
        sources_set.add(i["god_info"]["source"])
        try:
            if (i["god_info"]["source"].lower() in bad_list) or (i["god_code"].split("_")[-1].lower() in bad_list):
                fantasy_deities.remove(i)
            elif i["god_info"]["pantheon"].lower() in bad_list:
                fantasy_deities.remove(i)
                #source = i["god_info"]["source"]
                #print("\n", i["god_code"], source, "\n")

        except Exception as e:
            print("Issue is", e, " ", i)
    print("Here are your fantasy versions")
    print(len(fantasy_deities))
    print(sources_set)
    #print(fantasy_deities)

    #pprint(yaml_file)


if __name__ == "__main__":
    #Goes over relevant yaml files, adds them to dict using file name
    new_values = separate_values()
    deconstruct_deities(new_values["deities.yaml"])
    #TODO: add way to check rarity, source and other features to be removed before adding to SQL