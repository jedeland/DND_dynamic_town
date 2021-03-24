import json
import os
from pprint import pprint

import yaml
import re
import sqlite3

def get_names(culture):
    print("Calling the get_names function")
    print(culture)
    conn = sqlite3.connect("names_merged.db")
    cur = conn.cursor()
    #tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names = cur.execute("""SELECT * FROM NAMES""")
    pprint(cur.fetchall())

def explore_sql():
    #This function explores the SQL files
    sql_list = ["gen_townnames.db", "names_merged.db"]
    for i in range(2):
        print("On a fact finding mission! Iteration : {}".format(i))
get_names("Mexican")