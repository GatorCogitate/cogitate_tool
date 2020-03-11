"""A file for calculating how well a team works together using the interquartile range.

and calculate the individual contribution as a percentage of overall contribution
"""

# This import fixes a linting error with old division.
from __future__ import division
import numpy as np
import data_collection
from collections import defaultdict
import pandas as pd




def iterate_nested_dictionary(dictionary):
    """Iterate through the nested dictionary and create new dictionary."""
    # iterate through nested dictionary and add to new dictionary
    category_scores = {}
    amount = 0
    for user in dictionary.keys():
        for metric in dictionary[user]:
            # disregard any instances of strings in dictionary
            if not isinstance(dictionary[user][metric], str):
                # if list, add the length of the list to new dictionary
                if isinstance(dictionary[user][metric], list):
                    amount = len(dictionary[user][metric])
                    # print(amount)
                    if metric not in category_scores:
                        category_scores[metric] = [amount]
                    else:
                        category_scores[metric].append(amount)
                # if not list, add values to new dictionary
                else:
                    if metric not in category_scores:
                        category_scores[metric] = [dictionary[user][metric]]
                    else:
                        category_scores[metric].append(dictionary[user][metric])

    # return the new dictionary
    return category_scores


def calculate_iqr_score(data_list, below_weight, above_weight, within_weight):
    """Calculate a team score with interquartile range."""
    below_amount = 0
    above_amount = 0
    within_amount = 0
    dataset = data_list
    # calculate the size of the dataset
    size = len(dataset)
    # sort the dataset in ascending order
    sorted(dataset)
    # determine the first and third quartiles
    q1, q3 = np.percentile(dataset, [25, 75])
    # calculate the interquartile range (q3-q1)
    iqr = q3 - q1
    # calculate the lower bound of the IQR
    lower_bound = q1 - (1.5 * iqr)
    # calculate the upper bound of the IQR
    upper_bound = q3 + (1.5 * iqr)
    # for any value above, below or within the IQR add to the total
    for d in dataset:
        if d < lower_bound:
            below_amount = below_amount + 1
        if d > upper_bound:
            above_amount = above_amount + 1
        if lower_bound <= d <= upper_bound:
            within_amount = within_amount + 1
    # create factions of above, below, and within IQR amounts (divide by size) and round
    # pylint: disable=round-builtin
    below_fraction = round(below_amount / size, 2)
    above_fraction = round(above_amount / size, 2)
    within_fraction = round(within_amount / size, 2)
    # calculate all areas with their weight measurement
    weighted_below = round(below_weight * below_fraction, 2)
    weighted_above = round(above_weight * above_fraction, 2)
    weighted_within = round(within_weight * within_fraction, 2)
    # add weighted scores together to calcuate overall team score as percentage
    category_score = (weighted_below + weighted_above + weighted_within) * 100

    return category_score


def calculate_team_score(dictionary, below_weight, above_weight, within_weight):
    """Calculate the average team score."""
    # create a new dictionary and assign it to the dictionary iteration
    metrics_dictionary = iterate_nested_dictionary(dictionary)
    total_score = 0
    count = 0
    average_team_score = 0

    # iterate through the dictionary and calculate the category score for each list
    for metric, values_list in metrics_dictionary.items():
        if not isinstance(values_list, str):
            total_score += calculate_iqr_score(
                values_list, below_weight, above_weight, within_weight
            )
            count += 1

    average_team_score = total_score / count

    return average_team_score

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
