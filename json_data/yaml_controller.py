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
    range_dict = {}
    for k, v in ranges.items():
        print(k, v)
        range_dict[k] = random.choice(v)
    print(range_dict)

def find_rarity