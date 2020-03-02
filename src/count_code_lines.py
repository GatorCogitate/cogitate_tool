"""
This module is intended to run after all data has been collected and added.

to the .json file. The purpose is to create a dictionary where the username is.

the key and other calculated metrics are the values.
"""
from __future__ import division
import json_handler
import data_collection

# from pydriller.domain.commit import ModificationType


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
def add_raw_data_to_json(path_to_repo, json_file_name):
    """Check if raw data is in .json file and collects it if not."""
    # get the data from .json file
    current_data = json_handler.get_dict_from_json_file(json_file_name)
    # check if data has not been collected and do so if it was not
    if "RAW_DATA" not in current_data.keys():
        print("Raw data has not been collected, collecting it now...")
        # collects data from data_collection
        raw_data = {"RAW_DATA": data_collection.collect_commits_hash(path_to_repo)}
        # Write raw data to .json file
        json_handler.add_entry(raw_data, json_file_name)
        print("Data collected")


def calculate_individual_metrics(json_file_name):
    """Retrieve the data from .json file and create a dictionary keyed by user."""
    current_data = json_handler.get_dict_from_json_file(json_file_name)
    # creates a hashmap where the key is the authors username
    data_list = {}
    # Check if RAW_DATA is in json
    if "RAW_DATA" in current_data.keys():
        for key in current_data["RAW_DATA"]:
            author = key["author_name"]
            email = key["author_email"]
            # TODO check date compatibility with json
            # date = "N/A"
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
            # add the current_files to the user files list without duplicates
            data_list[author]["FILES"] = list(
                set(data_list[author]["FILES"]) | set(current_files)
            )
        # iterate through the data to do final calculations
        for key in data_list:
            data_list[key]["TOTAL"] = (
                data_list[key]["ADDED"] - data_list[key]["REMOVED"]
            )
            data_list[key]["MODIFIED"] = (
                data_list[key]["ADDED"] + data_list[key]["REMOVED"]
            )
            average = get_commit_average(
                data_list[key]["MODIFIED"], data_list[key]["COMMITS"]
            )
            data_list[key]["RATIO"] = average
            formats = get_file_formats(data_list[key]["FILES"])
            data_list[key]["FORMAT"] = formats
        # Reformat the dictionary as a value of the key INDIVIDUAL_METRICS
        indvividual_metrics_dict = {"INDIVIDUAL_METRICS": data_list}
        return indvividual_metrics_dict
    print("Raw data has not been collected, please run the collection function")
    return {}
    # NOTE: for printing the data please use the file print_table.py
