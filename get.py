#!/usr/bin/python


"""
    Author: Kyle Kersey 2014
    
    This script extracts links from the JSON output of "onedrive-cli list_links"
    the input JSON file must only contain properley formated JSON,
    the list of file names may be removed from the file using grep -v "-" input.json
"""

import sys
import json
import os

if len(sys.argv) < 2:
    print "usage: JSON file"
    sys.exit(0)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    print "cannot open file"
    sys.exit(0)

with open(file_name, "r") as f:
    data = json.loads(f.read())

for item in data:
    print item["name"].encode("utf-8")
    print item["link"]