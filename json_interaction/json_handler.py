"""This file provides preliminary methods of accessing and storing JSON data."""
import json
import os

data_path = "./data/"


def main():
    """Pull data from a provided json, and write it back to the json."""
    print("Retrieved data from json: \n")
    user_data_dict = get_dict_from_json_file("demofile")
    for username in user_data_dict:
        print(username + ":", user_data_dict[username], "\n")
    write_dict_to_json_file(user_data_dict, "demofile")
    with open(os.path.join(data_path, "demofile.json"), "r") as json_file:
        print("Contents of json file: \n", json_file.read())
    new_user = {"testuser": {"commits": [], "issues": [], "pull_requests": []}}
    print("\nAdding testuser to dictionary\n")
    add_user_to_users_dictionary(user_data_dict, new_user)
    write_dict_to_json_file(user_data_dict, "demofile")
    with open(os.path.join(data_path, "demofile.json"), "r") as json_file:
        print("Contents of json file: \n", json_file.read())


def get_dict_from_json_file(json_file_name):
    """Populate and return a dictionary of all the data in a specified json file."""
    with open(os.path.join(data_path, json_file_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        user_data_dict = json.load(json_file)
        # json.load() converts a json file into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, json_file_name):
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


if __name__ == "__main__":
    main()
