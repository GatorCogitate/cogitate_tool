"""Access and store JSON data."""
import json
import os


def get_dict_from_json_file(json_name, data_path="./data/"):
    """Populate and return a dictionary of all the data in a specified json file.

    Arguments:
    - json_file_name: The name of the file to open.
    - data_path: Default/optional argument that stores the relative path
      to the directory containing the file.
    """
    with open(os.path.join(data_path, json_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        user_data_dict = json.load(json_file)
        # json.load() converts a json file into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, json_file_name, data_path="./data/"):
    """Overwrite specified json file with data from a given dictionary.

    Arguments:
    - user_data_dict: Dictionary to write to a json file.
    - json_file_name: The name of the file to which to write.
    - data_path: Default/optional argument that stores the relative path
      to the directory containing the file.
    """
    with open(os.path.join(data_path, json_file_name + ".json"), "w") as json_file:
        # In the open() function, "w" specifies write access
        json.dump(user_data_dict, json_file, indent=4)
        # json.dump() converts a dictionary into a json-formatted string.
        # Specifying an indent does not alter the data itself, it only
        # increases readability in the json file.


def add_user_to_users_dictionary(user_data_dict, to_add):
    """Append data to the users dictionary."""
    user_data_dict.update(to_add)


def add_entry(new_entry, json_file_name):
    """Append data to the users dictionary."""
    data = get_dict_from_json_file(json_file_name)
    data.update(new_entry)
    write_dict_to_json_file(data, json_file_name)
