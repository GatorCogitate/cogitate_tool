"""This file provides preliminary methods of accessing and storing JSON data."""
import json
import os


def main():
    """Pull data from a provided json, and write it back to the json."""
    user_data_dict = get_dict_from_json_file("demofile")
    print("Dictionary:")
    for username in user_data_dict:
        print(username + ":", user_data_dict[username])
    print()
    json_format_string = write_dict_to_json_file(user_data_dict, "demofile")
    print("Json-formatted string:")
    print(json_format_string)
    print()


def get_dict_from_json_file(json_file_name):
    """Populate and return a dictionary of all the data in a specified json file."""
    with open(os.path.join("./data/", json_file_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        json_string = json_file.read()
        user_data_dict = json.loads(json_string)
        # json.loads() converts a json-formatted string into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, json_file_name):
    """Overwrite specified json file with data from a given dictionary."""
    with open(os.path.join("./data/", json_file_name + ".json"), "w") as json_file:
        # In the open() function, "w" specifies write access
        json_string = json.dumps(user_data_dict, indent=4)
        # json.dumps() converts a dictionary into a json-formatted string

        # Specifying an indent does not alter the data itself, it only increases
        # readability in the json file.

        json_file.write(json_string)
    return json_string


def append_user_to_json(user_data_dict, to_add, json_file_name):
    """Append data to the dictionary and write it to json"""
    dict.append(to_add)
    return write_dict_to_json_file(user_data_dict, json_file_name)


if __name__ == "__main__":
    main()
