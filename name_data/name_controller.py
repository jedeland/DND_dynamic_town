import json
import os
from pprint import pprint

import yaml
import re
import sqlite3

def get_cultures():
    print("Finding cultures")
    conn = sqlite3.connect("names_merged.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT origin FROM NAMES")
    origins = cur.fetchall()
    culture_list = []
    for i in origins:
        if i[0] != "Unisex":
            culture_list.append(i[0])
    return culture_list

def get_names(culture):

    print("Calling the get_names function")
    print(culture)
    conn = sqlite3.connect("names_merged.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()[0][0]
    #names = cur.execute("""SELECT * FROM NAMES""")

    print(tables)

    cur.execute("SELECT * FROM NAMES WHERE origin = '{}'".format(culture))
    names = cur.fetchall()
    pprint(names)

def explore_sql():
    #This function explores the SQL files
    sql_list = ["gen_townnames.db", "names_merged.db"]
    for i in range(2):
        print("On a fact finding mission! Iteration : {}".format(i))
        facts_dict = {}
        conn = sqlite3.connect(sql_list[i])

        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()[0][0]
        facts_dict["tables"] = tables

        cur.execute("""SELECT sql FROM sqlite_master WHERE tbl_name = '{}' AND type = 'table'""".format(tables))
        columns = cur.fetchall()
        print(tables, columns)
        #Find unique values
        # if i == 0:
        #     #Use Name and Origin
        # else:
        #     #Use name and origin
explore_sql()
get_names("France")
possible_cultures = get_cultures()
pprint(possible_cultures)