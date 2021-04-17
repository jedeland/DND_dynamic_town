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
    for k, v in ranges.items():
        print(k, v)