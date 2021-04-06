import json
import os
from pprint import pprint
import yaml

#File works to make sure only fantasy items can be found within the yaml files, and ensure a smaller selection to return more accurate results

def separate_values():
    print("separating values")
    skip_list = ["races.yaml", "region_modifiers.yaml", "languages.yaml"]
    yaml_dicts = {"deities": []}
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
    deities_dict = {"deities": []}
    for i in yaml_file:

        try:
            if (i["god_info"]["source"].lower() in bad_list) or (i["god_code"].split("_")[-1].lower() in bad_list):
                fantasy_deities.remove(i)
            elif i["god_info"]["pantheon"].lower() in bad_list:
                fantasy_deities.remove(i)
                #source = i["god_info"]["source"]
                #print("\n", i["god_code"], source, "\n")
            else:
                sources_set.add(i["god_info"]["source"])
                deities_dict["deities"].append(i)

        except Exception as e:
            print("Issue is", e, " ", i)
    print("Here are your fantasy versions")
    print(len(fantasy_deities))
    if len(fantasy_deities) == 333:
        print("This has already been cleaned, skipping write function!")
    else:
        with open("cleaned_data/deities.yaml", "w+") as f:
            print("")
            yaml.dump(deities_dict, f)


def deconstruct_baseitems(yaml_file):
    print("")
    print(type(yaml_file))
    print(len(yaml_file))
    fantasy_items = yaml_file.copy()
    sources_set = set()
    baseitem_dict = {"baseitem": []}
    for i in yaml_file:
        try:
            # if i["item_info"]["age"] == "modern" \
            #         or i["item_info"]["age"] == "futuristic":
            #       print("Item is not fantasy ")
            # elif i["item_info"]["age"] == "renaissance":
            #     print(i)
            #Checks if age key exists within i
            if "age" not in i["item_info"].keys():
                print(i)
                baseitem_dict["baseitem"].append(i)
            else:
                sources_set.add(i["item_info"]["age"])
                print(i["item_info"]["age"])
        except:
            print("UHOH")
            pass
    print("Here are your fantasy versions")
    print(len(fantasy_items))
    if len(fantasy_items) == 68:
        print("This has already been cleaned, skipping write function!")
    else:
        with open("cleaned_data/items-base.yaml", "w+") as f:
            print("")
            yaml.dump(baseitem_dict, f)

def splice_pathfinder_data():
    print()


if __name__ == "__main__":
    #Goes over relevant yaml files, adds them to dict using file name
    new_values = separate_values()
    print("New value is ", type(new_values))
    deconstruct_deities(new_values["deities.yaml"])
    deconstruct_baseitems(new_values["items-base.yaml"])
    splice_pathfinder_data()
    #TODO: add way to check rarity, source and other features to be removed be
    # fore adding to SQL