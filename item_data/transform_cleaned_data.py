import json
import os
import re
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
    with open("cleaned_data/items-base.yaml", "r+") as base:
        base_yaml = yaml.safe_load(base)
        base.close()
    #print("Base yaml is : ", base_yaml, " {}".format(type(base_yaml)))
    base_files = base_yaml[list(base_yaml.keys())[0]]
    for yaml_file in os.listdir("cleaned_data/pathfinder_data"):
        try:
            with open("cleaned_data/pathfinder_data/{}".format(yaml_file), "r", encoding="utf-8") as f:
                new_yaml = yaml.safe_load(f)
                print("\n\n")
                #print(yaml_file, new_yaml)
                new_yaml = translate_yaml(yaml_file=yaml_file, new_yaml=new_yaml)
                print("The new yaml has been created, it is a {} type, and has {} keys".format(type(new_yaml), new_yaml.keys()))
                #pprint(new_yaml)

                new_yaml_flat = new_yaml[list(new_yaml.keys())[0]]
                #print(new_yaml_flat)
                for i in new_yaml_flat:
                    # print(i["item_code"])
                    # print([g["item_code"] for g in base_files])
                    if any(i["item_code"].split("_")[0] in x["item_code"] for x in base_files):
                        print(i["item_code"], " was found in base files")
                        print("I FOUND IT")
                    else:
                        #TODO: add to top dict
                        print()
        except Exception as e:
            print(e)
            pass

    print()

def translate_yaml(yaml_file, new_yaml):
    json_items_list = {"{}".format(yaml_file.split(".")[0]): []}
    new_yaml = new_yaml[list(new_yaml.keys())[0]]
    print("TRANSLATING")
    for i in new_yaml:
        if "entries" in i:
            print("Json dict - {}".format(i))
            print(type(i))
        try:
            clean_name = re.sub(r'[^A-Za-z ]+', '', i["name"])
            clean_name = clean_name.replace("'", "")
            clean_name = re.sub(r"^\s", "", clean_name)
            #print("Cleaned name {} - Old name {}".format(clean_name, i["name"]))
            i = {"item_code": "{}_{}".format(clean_name.replace(" ", "-").upper(), i["source"][0]["abbr"].upper()), "item_info": i}
            json_items_list["{}".format(yaml_file.split(".")[0])].append(i)
        except Exception as e:
            print("Exception is ", e)
            pass
    return json_items_list


if __name__ == "__main__":
    #Goes over relevant yaml files, adds them to dict using file name
    new_values = separate_values()
    print("New value is ", type(new_values))
    deconstruct_deities(new_values["deities.yaml"])
    deconstruct_baseitems(new_values["items-base.yaml"])
    splice_pathfinder_data()
    #TODO: add way to check rarity, source and other features to be removed be
    # fore adding to SQL