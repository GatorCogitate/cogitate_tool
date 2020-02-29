"""This module is intended to run after all data has been collected and added.

to the .json file. The purpose is to create a dictionary where the username is.

the key and other calculated metrics are the values.
"""

# from git import Repo
from pydriller import RepositoryMining
import json_handler
import data_collection

# from pydriller.domain.commit import ModificationType


# TODO not used yet, has no impact
def delete_duplicates(data, keys_to_delete):
    """Delete keys from dictionary, keys are sent in a list."""
    dictionary = data
    for key in keys_to_delete:
        print(dictionary[key], " will be removed")
        del dictionary[key]
        print(key in dictionary)
    return dictionary


# TODO not used yet, has no impact
def parse_email(email):
    """Locate @ and + sign in email and returns the string between them."""
    # find the index of @ sign
    plus_index = email.find("+")
    # find the index of + sign
    at_index = email.find("@")
    # slices string accordingly
    revised_email = email[(plus_index + 1) : at_index]
    return revised_email


# NOTE: there are issues with this function, calls have been commented out
# TODO not used yet, has no impact
def check_emails(data):
    """Remove @github email from users and merges data with duplicates."""
    dictionary = data
    # list intended to gather keys with issues
    name_issues = []
    # gather keys that have issues and duplicates in dictionary
    keys_to_delete = []
    # loop through the data and add keys that have @github email to name_issues
    for key in dictionary:
        # checks if the email is a github email
        if "noreply.github.com" in dictionary[key]["EMAIL"]:
            # adds the key to issues list
            name_issues.append(key)
            # send email to parsing function
            new_name = parse_email(dictionary[key]["EMAIL"])
            if new_name in dictionary:
                print(new_name, " name to be merged with ", key)
                dictionary[new_name]["COMMITS"] += dictionary[key]["COMMITS"]
                dictionary[new_name]["ADDED"] += dictionary[key]["ADDED"]
                dictionary[new_name]["REMOVED"] += dictionary[key]["REMOVED"]
                dictionary[new_name]["TOTAL"] += dictionary[key]["TOTAL"]
                keys_to_delete.append(key)
            else:
                print(new_name, " not found in data")

    dictionary = delete_duplicates(dictionary, keys_to_delete)
    return dictionary


def get_commit_average(lines, commits):
    """Find average lines modified per commit."""
    # Loop through the dictionary and calculate the average lines per commits
    # formula for average: (added + deleted)/number_of_commits
    if commits != 0:
        average = lines / commits
        return (int)(average)
    return 0


def parse_for_type(name):
    """Parse through file name and returns its format."""
    if "." in name:
        dot_index = name.find(".")
        return name[dot_index:]
    return name


def get_file_formats(files):
    """Create a list of unique file formats."""
    formats = []
    for file in files:
        current_format = parse_for_type(file)
        if current_format not in formats:
            formats.append(current_format)
    return formats


# NOTE: this function is temporary to test get_individual_metrics considering
# there is not a main module that connects eerything yet
def add_data_to_json(path_to_repo, file_name):

    # get the data from .json file
    current_data = json_handler.get_dict_from_json_file(file_name)
    # check if data has not been collected and do so if it was not
    if "RAW_DATA" not in current_data.keys():
        print("Data has not been collected, collecting it now...")
        # collects data from data_collection
        raw_data = {"RAW_DATA" : data_collection.collect_commits_hash(path_to_repo)}
        # Write raw data to .json file
        json_handler.add_entry(raw_data, file_name)
        # Update current_data with the new contents
        current_data = json_handler.get_dict_from_json_file(file_name)
    # Call the calculation function
    print("Data collected")
    indvividual_metrics_dict = calculate_individual_metrics(current_data)

    # update .json file with indvividual information
    json_handler.add_entry(indvividual_metrics_dict, file_name)




def calculate_individual_metrics(current_data):
    """Retrieve the data from .json file and create a dictionary keyed by user."""
    # creates a hashmap where the key is the authors username
    data_list = {}
    for key in current_data["RAW_DATA"]:
        author = key["author_name"]
        email = key["author_email"]
        # TODO check date compatibility with json
        date = "N/A"
        # check if the key already in in the dicitionary
        if author in data_list:
            # condition passed, adds one to the number of commits
            data_list[author]["COMMITS"] += 1
        else:
            # condition fails, creates a new key and adds empty data
            data_list[author] = {
                "EMAIL": email,
                "COMMITS": 1,
                "ADDED": 0,
                "REMOVED": 0,
                "TOTAL": 0,
                "MODIFIED": 0,
                "RATIO": 0,
                "FILES": [],
                "FORMAT": [],
                "COMMITDATE": [],
            }

        data_list[author]["ADDED"] += key["line_added"]
        data_list[author]["REMOVED"] += key["line_removed"]
        # TODO: consider adding lines of code from data
        # check if the explored file is not in the list in index seven
        current_files = key["filename"]
        data_list[author]["FILES"] += current_files
    # iterate through the data to do final calculations
    for key in data_list:
        data_list[author]["TOTAL"] = data_list[author]["ADDED"] - data_list[author]["REMOVED"]
        data_list[author]["MODIFIED"] = data_list[author]["ADDED"] + data_list[author]["REMOVED"]
        average = get_commit_average(
            data_list[key]["MODIFIED"], data_list[key]["COMMITS"]
        )
        data_list[key]["RATIO"] = average
        formats = get_file_formats(data_list[key]["FILES"])
        data_list[key]["FORMAT"] = formats
    return data_list

# NOTE: for printing the data please use the file print_table.py


if __name__ == "__main__":
    REPO_PATH = input("Enter the path to the repo : ")
    # JSON_NAME = input("Enter the name of the json file : ")
    JSON_NAME = "contributor_data_template"
    add_data_to_json(REPO_PATH, JSON_NAME)
