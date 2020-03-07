"""
This module's purpose is to calculate the individual scoring of software.
developers in a Github repository. It will calculate a developer's score
based on a data set gathered previously in a different module.
"""

# This import fixes a linting error with old division.
from __future__ import division
import data_collection

# import operator
# import math

# For 3/3/2020:
# TODO Fake data - start with dictionary - Madelyn *
# TODO function for commit score - Teona *
# TODO function for added lines score - Teona *
# TODO function for deleted lines - Wonjoon *
# TODO lines modified score - Madelyn *
# TODO lines per commit score - Wonjoon *
# TODO amount of files modified overall score - Madelyn *
# TODO file for printing the individual score - Teona *
# TODO average of all scores - Everyone, once other features are finished

# Possible other features or scoring metrics:
# TODO amount of files per commit score
# TODO talk about using PyGithub to retrieve issue data
# TODO amount of comments in lines of code score - research tools for parsing
# TODO date distribution score
# TODO average overall score and individual score to produce new individual score
# TODO give notification of duplicate username if there is one, or the possibility
# TODO User inputs the weight for each category for finding total individual score

# Helpful reminders:
# Use pipeline programming style
# Implement test cases as functions are written in the test_individual_scoring.py file
# Scoring will be done first as percentages ((individual contribution/total branch)*100)

# Add fake data that corresponds to overall-eval-analyzing-metrics branch
# github_data uses the pattern ["username", commit_total, lines_added,
# lines_deleted, total_lines, modified_lines, lines_per_commit, files_changed]


# NOTE This is the fake data, it does not have key for the email for now, for tesing purposes
github_data = {
    "noorbuchi": {"COMMITS": 28, "ADDED": 349, "REMOVED": 70},
    "bagashvilit": {"COMMITS": 22, "ADDED": 355, "REMOVED": 56},
    "Jordan-A": {"COMMITS": 23, "ADDED": 375, "REMOVED": 43},
    "WonjoonC": {"COMMITS": 27, "ADDED": 365, "REMOVED": 67},
    "Hannah Schultz": {"COMMITS": 25, "ADDED": 315, "REMOVED": 75},
    "Alexander_Hamilton": {"COMMITS": 41, "ADDED": 350, "REMOVED": 54},
    "Karl_Marx": {"COMMITS": 0, "ADDED": 0, "REMOVED": 0},
    "Julius_Caesar": {"COMMITS": 25, "ADDED": 363, "REMOVED": 35},
    "Napoleon_Bonaparte": {"COMMITS": 24, "ADDED": 540, "REMOVED": 2},
    "Alexander_the_Great": {"COMMITS": 42, "ADDED": 355, "REMOVED": 50},
}

# NOTE: The following code block still needs to be fixed in terms of variable
# names and docstrings.

data_collection.calculate_individual_metrics("individual_metrics_testfile")
# pylint: disable=round-builtin
def percentage_score(individual, overal_branch):
    """Calculate the individual contribution percentage."""
    return round(individual * 100 / overal_branch)


def sum_value(key):
    """Sum up all the values in branch per key."""
    return sum(d[key] for d in github_data.values() if d)


def individual_commitmnet(username, category):
    """Get and send value for key."""
    return github_data[username][category]

def average_score():
    """Calculate the average score using all previously calculated metrics."""

# weights = {
# "COMMITS": 0.2,
# "ADDED": 0.4,
# "REMOVED": 0.4 }

# def get_weighted(User):
#     user=github_data[User]
#
#     weighted={User: {k:(round(user[k]*weights[k])) for k in user.keys()}}
#     return weighted


#Print usename and percentage of their contribution for each category
def print_data():
    """Print out github_data scores."""
    for username, data in github_data.items():
        print("\n", username)
        for category in data:
            print(
                category,
                percentage_score(
                    individual_commitmnet(username, category), sum_value(category)
                ),
                "%",
            )



if __name__ == "__main__":

    # for username in github_data:
    #     print (get_weighted(username))
    print(data_collection.calculate_individual_metrics("individual_metrics_testfile"))
    print_data()
