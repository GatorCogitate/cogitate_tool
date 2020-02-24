"""This file provides preliminary methods of accessing and storing JSON data."""
import json
import os


def get_dict_from_json_file(json_file_name, data_path="./data/"):
    """Populate and return a dictionary of all the data in a specified json file."""
    with open(os.path.join(data_path, json_file_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        user_data_dict = json.load(json_file)
        # json.load() converts a json file into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, json_file_name, data_path="./data/"):
    """Overwrite specified json file with data from a given dictionary."""
    with open(os.path.join(data_path, json_file_name + ".json"), "w") as json_file:
        # In the open() function, "w" specifies write access
        json.dump(user_data_dict, json_file, indent=4)
        # json.dump() converts a dictionary into a json-formatted string.
        # Specifying an indent does not alter the data itself, it only increases
        # readability in the json file.


def add_user_to_users_dictionary(user_data_dict, to_add):
    """Append data to the users dictionary"""
    user_data_dict.update(to_add)
