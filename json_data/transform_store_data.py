import os
import time
from pprint import pprint

import yaml

#Global Variables
blacksmith_list = ["weapon", "armor", "tool", "shield", "bow", "axe", "sword", "spear", "plate",
                   "piercing", "bludgeoning", "slashing", "mail", "chain"]
general_list = ["potion", "tools", "saddle", "ink", "mining", "fishing", "book", "bag", "drink", "clothing" "eat", "food"]
enchanter_list = ["potion", "wand", "can cast", "book", "bottle",
                  "scroll", "staff", "ring", "token", "gem", "cloak", "talisman", "healing"]
scribe_list = ["ink", "robe", "cloak", "scroll", "book", "tome", "bottle"]
alchemist_list = ["potion", "flask", "bag", "poison", "elixir", "powder", "pouch"]




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
            #print(i,"\n", path)
            x = "{}/{}".format(path, i)
            #print(x)
            path_list.append(x)
    print(path_list, "\n",type(path_list))
    #The appended value lays inside of a different directory
    path_list.append("cleaned_data/items.yaml")

    relevant_data = path_list
    print(relevant_data)

    #TODO: go through each file and try to standardise item tags, use this to create two files which hold data about
    # both types of stores to be used in conjunction with store_class.py
    path_items_details = {}
    unique_keys = set()
    list_of_uniques = []
    #Skips the first 2 results as they are inconsequential
    for path_item in path_list[2:]:
        with open(path_item, "r+", encoding="utf-8") as f:
            #print(f)
            store_file = yaml.safe_load(f)
            print("Store file : ", f, path_item)
            list_of_dicts = next(iter(store_file.values()))
            print(len(list_of_dicts))
            #TODO: Find individual values relating to keys, and tag them as being from xyz fil
            # Set isnt working, it is updating using 2nd set of values
            # Need to make seperate function for items.yaml
            #print([i.keys() for i in list_of_dicts])

            for i in list_of_dicts:
                if path_item == "cleaned_data/items.yaml":
                    i = i["item_info"]
                    #print(i)
                #print(i.keys())
                unique_keys.update(i.keys())
            #print("Unique Keys = ", unique_keys)
            list_of_uniques.append(unique_keys)


            item_list = [len(list_of_dicts), unique_keys]
            path_items_details["{}_itemlist".format(f), "unique_keys"] = item_list[0], item_list[1]
            print("\n"*2)
            time.sleep(1)
    #explore_differences(relevant_data)
    #print(path_items_details, type(path_items_details))
    #print(unique_keys)
    for k in path_items_details:
        print(path_items_details[k])
    #print("List of uniques : ", list_of_uniques)

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

def conform_data_items():
    cleaned_dict = {}
    irrelevant_tags = ["otherSources", "containerCapacity", "staff", 'bonusWeapon',
                       'additionalSources', 'weaponCategory', 'bonusWeaponDamage',
                       'sentient', 'age','ability', "capPassenger", "reqAttuneAlt", "baseItem",
                       'capCargo', 'carryingCapacity', 'dmg2', 'ammoType', 'bonusSavingThrow', 'axe',
                       'lootTables', 'crew', 'bonusAc', 'packContents', 'crewMin',
                       "scfType", "grantsProficiency", "vehSpeed", 'vehDmgThresh', 'crewMax']
    standarisable_tags = {'dmgType': 'damagetype', "weaponCategory": "weaponcategory", "dmg1": "dice_size", "weightNote": "weight"}
    naughty_tags = ["curse", "tattoo"]
    with open("cleaned_data/items.yaml", "r+", encoding="utf-8") as f:

        store_file = yaml.safe_load(f)
        print(len(store_file["items"]))
        try:
            list_of_dicts = next(iter(store_file.values()))
            temp_dict = {"items": []}
            for i in list_of_dicts:
                temp_code = i["item_code"]
                i = i["item_info"]
                #TODO: drop all tags in irrelelvant tags, change standarisable tags to their value, and remove items with naughty tags
                print(i.keys())

                for k in irrelevant_tags:
                    if k in i:
                        print(k)
                        del i[k]
                        print("Deleted : ", k)
                dict_info = [{"item_code": temp_code, "item_info": i}]
                temp_dict["items"] = temp_dict["items"] + dict_info

            # print(temp_dict, len(temp_dict["items"]))

            updated_yaml = yaml.dump(temp_dict)
            print("This is the start of updated yaml, {} - {} , this is the end".format(updated_yaml, temp_dict))
            sort_data_to_stores(temp_dict)


        except Exception as e:
            print("There was an error, or this has already been executed \nError was {}".format(e))

def assign_store_category(store_list, types):
    print("Assigning stores to categories")
    print("Checking stores exist")
    if os.path.exists("cleaned_data/citizen_store_data") and os.path.exists("cleaned_data/hero_store_data"):
        print("The folders exist!")
        #Change replace to overwrite files

        replace = True
        #Note: the id tags in thr yaml do not affect the output
        for i in store_list.keys():
            print(store_list.keys())
            #print("This is i ", i)
            #print("This is the start of the store list: ", store_list.get(i))
            if i in types["civilian stores"]:
                print("{} is in civ stores".format(i))
                if not os.path.exists(r"cleaned_data/citizen_store_data/{}.yaml".format(i)) or replace:
                    with open(r"cleaned_data/citizen_store_data/{}.yaml".format(i), "w+") as f:
                        data = yaml.dump(store_list.get(i), f, sort_keys=False)
                        #print(data)
                else:
                    print("Data {} was not uploaded, as it already exists".format(i))
            if i in types["hero stores"]:
                if not os.path.exists(r"cleaned_data/hero_store_data/{}.yaml".format(i)) or replace:
                    with open(r"cleaned_data/hero_store_data/{}.yaml".format(i), "w+") as fil:
                        data = yaml.dump(store_list.get(i), fil, sort_keys=False)
                        #print(data)
                else:
                    print("Data {} was not uploaded, as it already exists".format(i))
        with open(r"cleaned_data/hero_store_data/Blacksmith.yaml", "r+") as file:
            blacksmith_data = yaml.safe_load(file)
            print(blacksmith_data[0:100])
            print(type(blacksmith_data), " : ")
            for g in blacksmith_data:
                print(g['item_code'])



    else:
        print("The folder couldnt be found, creating folders")
        os.mkdir("cleaned_data/citizen_store_data")
        os.mkdir("cleaned_data/hero_store_data")

def sort_data_to_stores(new_yaml):
    list_of_dicts = next(iter(new_yaml.values()))
    with open("cleaned_data/items-base.yaml", "r") as base_file:
        base_yaml = yaml.safe_load(base_file)
        list_of_base_dicts = next(iter(base_yaml.values()))
        base_file.close()
    # HE = input()
    # print("The list of base dicts is ...")
    # pprint(list_of_base_dicts)
    # HO = input()
    #Generic bins to classify data
    store_types = ["General_Store", "Wandmaker", "Blacksmith", "Armourer", "Weaponsmith", "Alchemist", "Enchanter", "Scribe"]
    assign_types = {"civilian stores": ["General_Store", "Wandmaker", "Alchemist", "Enchanter", "Scribe", "Alchemist"],
                     "hero stores": ["Blacksmith", "Armourer", "Weaponsmith", "Alchemist", "Enchanter"]}
    #Scope limited to 3 words to test types
    stores = {"Blacksmith" :[], "Enchanter": [], "Scribe": [], "General_Store": [], "Alchemist": []}
    key_words = {"Blacksmith" : blacksmith_list, "General_Store": general_list, "Enchanter": enchanter_list,
                 "Scribe": scribe_list, "Alchemist": alchemist_list}
    #print(len(new_yaml["items"]))
    #print("printing weapons")

    for i in list_of_dicts:
        assign_stores(i, key_words, stores)
    print("The first size")
    print(len(stores["Blacksmith"]))
    # print([g["item_code"] for g in stores["General Store"]])
    print(len(stores["General_Store"]))
    print(len(stores["Enchanter"]))
    print(len(stores["Scribe"]))

    for g in list_of_base_dicts:
        assign_stores(g, key_words, stores)
    print("The second size")
    print(len(stores["Blacksmith"]))
    # print([g["item_code"] for g in stores["General Store"]])
    print(len(stores["General_Store"]))
    print(len(stores["Enchanter"]))
    print(len(stores["Scribe"]))

    #Replace is a boolean asking to overwrite currently existing files or not
    assign_store_category(stores, assign_types)


def assign_stores(i, key_words, stores):
    item_info = i["item_info"]
    # print("Original I ", i)
    # print(item_info, type(item_info))
    # TODO: need to find a way to decide if i goes into the "bins" assigned above
    # Best bet is to make a classification system using simple inputs
    try:
        # Fixed issue with keywords
        for k, v in item_info.items():
            if any(word in str(v).lower() for word in key_words["Blacksmith"]):
                stores["Blacksmith"].append(i)
            if any(word in str(v).lower() for word in key_words["General_Store"]):
                stores["General_Store"].append(i)

                if i['item_info']['rarity'] in ["artifact", "legendary", "very rare"]:
                    stores["General_Store"].remove(i)

            if any(word in str(v).lower() for word in key_words["Enchanter"]):
                stores["Enchanter"].append(i)
            if any(word in str(v).lower() for word in key_words["Scribe"]):
                stores["Scribe"].append(i)
            if any(word in str(v).lower() for word in key_words["Alchemist"]):
                stores["Alchemist"].append(i)

    except Exception as e:
        print("There was an exception: ", e, e.args)
        pass


# print(stores["Scribe"])


conform_data_items()

"""{'curse', 'property', 'color', 'otherSources', 'poison', 'containerCapacity', 'staff',
 'resist', 'bonusWeapon', 'value', 'additionalSources', 'speed', 'weaponCategory', 'bonusWeaponDamage', 
 'sentient', 'age', 'charges', 'rarity', 'ability', 'attachedSpells', 'capPassenger', 'bonusSpellAttack', 'weaponcategory', 'reqAttuneAlt', 
 'sword', 'source', 'weapon', 'reqAttune', 'reload', 'capCargo', 'carryingCapacity', 'baseItem', 'dmg2', 'ammoType', 'stealth', 'bonusSavingThrow', 
 'level', 'bulk', 'weapongroup', 'axe', 'lootTables', 'crew', 'name', 'bonusAc', 'hands', 'packContents', 'crewMin', 'entries', 'wondrous', 'strength', 
 'dmgType', 'weightNote', 'descr', 'scfType', 'page', 'dmg1', 'grantsProficiency', 'type', 'vehSpeed', 'weight', 'damagetype', 'tattoo', 'ac', 
 'vehDmgThresh', 'crewMax', 'tier', 'focus', 'recharge', 'price_gp', 
'dice_size', 'srd', 'bonusWeaponAttack', 'vehAc', 'vehHp', 'range', 'additionalEntries', 'traits', 'poisonTypes', 'travelCost', 'price_cp', 'shippingCost'}"""