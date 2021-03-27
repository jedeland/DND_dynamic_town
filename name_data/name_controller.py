import json
import os
from pprint import pprint

import yaml
import re
import sqlite3

def get_cultures():
    print("Finding cultures")
    conn = sqlite3.connect(r"C:\Users\jedel\PycharmProjects\DND_dynamic_town\name_data\names_merged.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT origin FROM NAMES")
    origins = cur.fetchall()
    culture_list = []
    for i in origins:

        if i[0] not in  ["Unisex", "Hawaiian"]:
            culture_list.append(i[0])
    return culture_list

def check_values():
    print("Checking values")
    conn = sqlite3.connect("names_merged.db")
    cur = conn.cursor()
    cultures = get_cultures()
    for i in cultures:
        cur.execute("SELECT DISTINCT tag FROM NAMES WHERE origin = '{}'".format(i))
        value = cur.fetchall()
        print(value)
        print(i)
        if value[0][0] == "N" and len(value) < 2:
            print("Issue found with", i)

def get_names(culture):

    print("Calling the get_names function")
    print(culture)
    conn = sqlite3.connect("names_merged.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()[0][0]
    #names = cur.execute("""SELECT * FROM NAMES""")

    # print(tables)
    # cur.execute("""SELECT name FROM PRAGMA_TABLE_INFO('NAMES')""")
    # out = cur.fetchall()
    # print(out)

    cur.execute("SELECT * FROM NAMES WHERE origin = '{}'".format(culture))
    names = cur.fetchall()
    pprint(names)

def explore_sql():
    #This function explores the SQL files
    sql_list = ["name_data/gen_townnames.db", "name_data/names_merged.db"]
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

check_values()