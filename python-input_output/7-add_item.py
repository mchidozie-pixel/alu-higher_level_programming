#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with an empty list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save the updated list
save_to_json_file(items, filename)
