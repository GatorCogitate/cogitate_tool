"""This file provides preliminary methods of accessing and storing JSON data."""
import json
import os


def main():
    """Pull data from a provided json, and write it back to the json."""
    dict = get_dict_from_json_file("demofile")
    print("dict format: ")
    for key in dict:
        print(key + ":", dict[key])
    print()
    json_format = write_dict_to_json_file(dict, "demofile")
    print("json format: ")
    print(json_format)
    print()


def get_dict_from_json_file(json_file_name):
    """Populate and return a dictionary of all the data in a specified json file."""
    with open(os.path.join("./data/", json_file_name + ".json"), "r") as json_file:
        json_string = json_file.read()
        dict = json.loads(json_string)
    return dict


def write_dict_to_json_file(dict, json_file_name):
    """Overwrite specified json file with data from a given dictionary."""
    with open(os.path.join("./data/", json_file_name + ".json"), "w") as json_file:
        json_string = json.dumps(dict, indent=4)
        json_file.write(json_string)
    return json_string


def append_user_to_json(dict, to_add, json_file_name):
    """Append data to the dictionary and write it to json"""
    dict.append(to_add)
    return write_dict_to_json_file(dict, json_file_name)


if __name__ == "__main__":
    main()
