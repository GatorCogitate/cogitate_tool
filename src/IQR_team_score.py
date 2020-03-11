"""A file for calculating how well a team works together using the interquartile range."""

# This import fixes a linting error with old division.
from __future__ import division
import numpy as np
import data_collection


github_data = data_collection.calculate_individual_metrics()

# github_data = {
#     "noorbuchi": {"COMMITS": 28, "ADDED": 349, "REMOVED": 70},
#     "bagashvilit": {"COMMITS": 22, "ADDED": 355, "REMOVED": 56},
#     "Jordan-A": {"COMMITS": 23, "ADDED": 375, "REMOVED": 43},
#     "WonjoonC": {"COMMITS": 27, "ADDED": 365, "REMOVED": 67},
#     "Hannah Schultz": {"COMMITS": 25, "ADDED": 315, "REMOVED": 75},
#     "Alexander_Hamilton": {"COMMITS": 41, "ADDED": 350, "REMOVED": 54},
#     "Karl_Marx": {"COMMITS": 0, "ADDED": 0, "REMOVED": 0},
#     "Julius_Caesar": {"COMMITS": 25, "ADDED": 363, "REMOVED": 35},
#     "Napoleon_Bonaparte": {"COMMITS": 24, "ADDED": 540, "REMOVED": 2},
#     "Alexander_the_Great": {"COMMITS": 42, "ADDED": 355, "REMOVED": 50},
# }


def iterate_nested_dictionary():
    """Iterate through the nested dictionary and access metrics and their values to add to a list."""
    # iterate through nested dictionary and add to new dictionary
    category_scores = {}
    amount = 0
    for user in github_data.keys():
        for metric in github_data[user]:
            # disregard any instances of strings in dictionary
            if isinstance(github_data[user][metric], str):
                category_scores = category_scores
            else:
                # if list, add the length of the list to new dictionary
                if isinstance(github_data[user][metric], list):
                    amount = len(github_data[user][metric])
                    # print(amount)
                    if metric not in category_scores:
                        category_scores[metric] = [amount]
                    else:
                        category_scores[metric].append(amount)
                # if not list, add values to new dictionary
                else:
                    if metric not in category_scores:
                        category_scores[metric] = [github_data[user][metric]]
                    else:
                        category_scores[metric].append(github_data[user][metric])

    # return the new dictionary
    return category_scores


def calculate_iqr_score(data_list, below_weight, above_weight, within_weight):
    """Calculate a team score for a data set according to outliers calculated with the interquartile range."""
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
    """Calculate the average team score by totaling the team scores for each dataset and dividing by amount of datasets."""
    # create a new dictionary and assign it to the dictionary iteration
    metrics_dictionary = iterate_nested_dictionary()
    total_score = 0
    count = 0
    average_team_score = 0

    # iterate through the dictionary and calculate the category score for each list
    for metric, values_list in metrics_dictionary.items():
        if isinstance(values_list, str):
            total_score
        else:
            total_score += calculate_iqr_score(
                values_list, below_weight, above_weight, within_weight
            )
            count += 1

    average_team_score = total_score / count

    return average_team_score


if __name__ == "__main__":
    # print(github_data)
    # print(iterate_nested_dictionary(github_data))
    print(calculate_team_score(github_data, 0.2, 0.2, 0.6))
