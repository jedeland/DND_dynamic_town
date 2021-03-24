import json
import os
import yaml
import re
import sqlite3

def get_names(culture):
    print("Calling the get_names function")
    print(culture)
    db = sqlite3.connect("names_merged.db")