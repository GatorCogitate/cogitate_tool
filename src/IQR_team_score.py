# This import fixes a linting error with old division.
from __future__ import division
import numpy as np

commit_data = []
added_data = []
removed_data = []
modified_data = []
commits_score = 0
added_score = 0
removed_score = 0
modified_score = 0
average_score = 0

# fake data
github_data = {
    "noorbuchi": {"COMMITS": 28, "ADDED": 349, "REMOVED": 70, "MODIFIED": 419},
    "bagashvilit": {"COMMITS": 22, "ADDED": 355, "REMOVED": 56, "MODIFIED": 411},
    "Jordan-A": {"COMMITS": 23, "ADDED": 375, "REMOVED": 43, "MODIFIED": 418},
    "WonjoonC": {"COMMITS": 27, "ADDED": 365, "REMOVED": 67, "MODIFIED": 432},
    "Hannah Schultz": {"COMMITS": 25, "ADDED": 315, "REMOVED": 75, "MODIFIED": 390},
    "Alexander_Hamilton": {"COMMITS": 41, "ADDED": 350, "REMOVED": 54, "MODIFIED": 404},
    "Karl_Marx": {"COMMITS": 0, "ADDED": 0, "REMOVED": 0, "MODIFIED": 0},
    "Julius_Caesar": {"COMMITS": 25, "ADDED": 363, "REMOVED": 35, "MODIFIED": 398},
    "Napoleon_Bonaparte": {"COMMITS": 24, "ADDED": 540, "REMOVED": 2, "MODIFIED": 542},
    "Alexander_the_Great": {
        "COMMITS": 42,
        "ADDED": 355,
        "REMOVED": 50,
        "MODIFIED": 405,
    },
}


def calculate_iqr_score(data_list):
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

    # print(below_amount, above_amount, within_amount)
    # calculate all areas with their weight measurement
    weighted_below = round(0.05 * below_fraction, 2)
    weighted_above = round(0.20 * above_fraction, 2)
    weighted_within = round(0.75 * within_fraction, 2)
    # add weighted scores together to calcuate overall team score as percentage
    team_score = (weighted_below + weighted_above + weighted_within) * 100

    return team_score
    # print(weighted_below, weighted_above, weighted_within, team_score)


def determine_datasets(dictionary):
    # iterate through nested dictionary
    for username, data in github_data.items():
        # for each key in the dictionary its values to a list
        for key in data:
            if key == "COMMITS":
                commit_data.append(data[key])
            if key == "ADDED":
                added_data.append(data[key])
            if key == "REMOVED":
                removed_data.append(data[key])
            if key == "MODIFIED":
                modified_data.append(data[key])

    # print(commit_data)


def calculate_average(dictionary):
    # import lists from calculate_datasets function
    determine_datasets(dictionary)
    # print(commit_data)
    # calculate the team score for each list of data
    commits_score = calculate_iqr_score(commit_data)
    added_score = calculate_iqr_score(added_data)
    removed_score = calculate_iqr_score(removed_data)
    modified_score = calculate_iqr_score(modified_data)

    # find the average team score for all of the categories
    average_score = (commits_score + added_score + removed_score + modified_score) / 4

    return average_score


if __name__ == "__main__":
    print(calculate_average(github_data), "%")
