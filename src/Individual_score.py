"""
This module's purpose is to calculate the individual contribution of software.

developers in a Github repository. It will calculate a developer's contribution
based on a data set gathered previously in a different module.
"""

# This import fixes a linting error with old division.
from __future__ import division
from collections import defaultdict
import pandas as pd
import data_collection


# pylint: disable=round-builtin
def percent_calculator(individual, overal_branch):
    """Calculate the percentage."""
    return round(individual * 100 / overal_branch)


def sum_metrics_int(key, dictionary):
    """Sum up all the int type values in metrics per key."""
    return sum(d[key] for d in dictionary.values())


def sum_metrics_list(key, dictionary):
    """Sum up all the list type values in metrics per key."""
    return sum(len(d[key]) for d in dictionary.values())

def add_new_metrics(dictionary):
    """Use existing metrics to calculate additional metrics and populate the dictionary.

    with new values
    """
    for key in dictionary:
        dictionary[key]["TOTAL"] = (
            dictionary[key]["ADDED"] - dictionary[key]["REMOVED"]
        )
        dictionary[key]["MODIFIED"] = (
            dictionary[key]["ADDED"] + dictionary[key]["REMOVED"]
        )
        average = data_collection.get_commit_average(
            dictionary[key]["MODIFIED"], dictionary[key]["COMMITS"]
        )
        dictionary[key]["RATIO"] = average
        formats = data_collection.get_file_formats(dictionary[key]["FILES"])
        dictionary[key]["FORMAT"] = formats
    return dictionary

def individual_contribution(dictionary):
    """Calculate the percentage of indivudual contribution."""
    contributor_data = {}
    # use default dictionary to provide default value for a nonexistent key
    contributor_data = defaultdict(dict)
    for username, data in dictionary.items():
        for metrics, value in data.items():
            # if data type is int use the appropriate function to sum up the values
            if isinstance(value, int):
                contributor_data[username][metrics] = percent_calculator(
                    value, sum_metrics_int(metrics, dictionary))
            # if data type is list use the appropriate function to sum up the values
            if isinstance(value, list):
                contributor_data[username][metrics] = percent_calculator(
                    len(value), sum_metrics_list(metrics, dictionary)), value
    return contributor_data


# NOTE:This part of the program is for demonstration and debugging puproses and will
# not be merged into the master branch
if __name__ == "__main__":

    DATA = data_collection.calculate_individual_metrics()
    new_dict  = add_new_metrics(DATA)
    # if statement will check if raw data was collected
    if DATA == {}:
        # pylint: disable=input-builtin
        REPO_PATH = input("Enter the path to the repo : ")
        # This call will use default options for file and overwrite condition
        data_collection.collect_and_add_raw_data_to_json(REPO_PATH)

    # display the dictionary of individual contributions
    print(pd.DataFrame.from_dict(individual_contribution(new_dict)).T)
