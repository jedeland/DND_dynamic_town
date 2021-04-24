import yaml
import os
import sqlite3
import random
from pprint import  pprint

def assign_categories(yaml_file, inventory_ratios):
    print("Checking over ratios")
    print(type(inventory_ratios))
    ranges = inventory_ratios["store_wealth"]
    print(type(ranges))
    #TODO have the function add in common items as well
    ratio_of_items = random.randint(30, 60)
    range_dict = {}
    for k, v in ranges.items():
        print(k, v)
        range_dict[k] = random.choice(v)
    print(range_dict)

def find_rarity(yaml_file, inventory_ratios):
    print()
    # rarity_set = set()
    # print(type(rarity_set))
    # for yaml_dict in yaml_file:
    #     try:
    #         # print(yaml_dict["item_info"]["rarity"])
    #
    #         rarity_set.add(yaml_dict["item_info"]["rarity"])
    #     except:
    #         #If value is pathfinder item it should be non magical regular item
    #         if "CRB" in str(yaml_dict["item_code"]):
    #             rarity_set.add("pathfinder_nonmagic")
    #         else:
    #             print("There was an exception at - ", yaml_dict["item_code"])
    #         pass
    # print(rarity_set)
    print("***")
    rarity_bins = {
        "non-magic": ["pathfinder_nonmagic", "none", "unknown"],
        "uncommon": ["uncommon", "unknown (magic)"],
        "common": ["common", "varies" ],
        "rare": ["rare", "varies"],
        "very rare": ["very rare", "varies", "unknown (magic)"],
        "legendary": ["legendary"],
        "artifact": ["artifact"]
    }
    print(rarity_bins)
    inventory_dict = {}
    for result in yaml_file:
        print(result["item_info"].keys())
        if "rarity" in result["item_info"].keys():
            print("Value is DND item")
        else:
            print("Value is pathfinder item")