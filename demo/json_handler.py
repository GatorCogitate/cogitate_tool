"""This file provides preliminary methods of accessing and storing JSON data."""
import json
import os

data_path = "./data/"


def main():
    """Pull data from a provided json, and write it back to the json."""
    user_data_dict = get_dict_from_json_file("demofile")
    print("Dictionary:\n")
    for username in user_data_dict:
        print(username + ":", user_data_dict[username], "\n")
    json_format_string = write_dict_to_json_file(user_data_dict, "demofile")
    print("Json-formatted string:", "\n", json_format_string, "\n")
    new_user = {"testuser": {"commits": [], "issues": [], "pull_requests": []}}
    add_user_to_users_dictionary(user_data_dict, new_user, "demofile")


def get_dict_from_json_file(json_file_name):
    """Populate and return a dictionary of all the data in a specified json file."""
    with open(os.path.join(data_path, json_file_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        user_data_dict = json.load(json_file)
        # json.loads() converts a json-formatted string into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, json_file_name):
    """Overwrite specified json file with data from a given dictionary."""
    with open(os.path.join(data_path, json_file_name + ".json"), "w") as json_file:
        # In the open() function, "w" specifies write access
        json_string = json.dumps(user_data_dict, indent=4)
        # json.dumps() converts a dictionary into a json-formatted string

        # Specifying an indent does not alter the data itself, it only increases
        # readability in the json file.

        json_file.write(json_string)
    return json_string


def add_user_to_users_dictionary(user_data_dict, to_add):
    """Append data to the users dictionary"""
    user_data_dict.update(to_add)


if __name__ == "__main__":
    main()
