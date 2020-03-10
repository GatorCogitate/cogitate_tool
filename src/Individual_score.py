"""
This module's purpose is to calculate the individual scoring of software.
developers in a Github repository. It will calculate a developer's score
based on a data set gathered previously in a different module.
"""

# This import fixes a linting error with old division.
from __future__ import division
from collections import defaultdict
import pandas as pd
import data_collection


def percent_calculator(individual, overal_branch):
    """Calculate the individual contribution percentage."""
    return round(individual * 100 / overal_branch)


def sum_metrics_values(key,dictionary):
    """Sum up all the values in metrics per key."""
    return sum(d[key] for d in dictionary.values())


def individual_contribution(dictionary):
    contributor_data = {}
    contributor_data = defaultdict(dict)
    for username, data in dictionary.items():
        for metrics,value in data.items():
            if isinstance(value, int):
                contributor_data[username][metrics] = percent_calculator(
                    value, sum_metrics_values(metrics,dictionary)),"%"
            if isinstance(value, list):
                contributor_data[username][metrics] = len(value), value
    return contributor_data


if __name__ == "__main__":

    DATA = data_collection.calculate_individual_metrics()
    # if statement will check if raw data was collected
    if DATA == {}:
        REPO_PATH = input("Enter the path to the repo : ")
        # This call will use default options for file and overwrite condition
        data_collection.collect_and_add_raw_data_to_json(REPO_PATH)
    print("Adding processed data to selected json file...")

    print(pd.DataFrame.from_dict(individual_contribution(DATA)))
