"""
This module's purpose is to calculate the individual scoring of software.
developers in a Github repository. It will calculate a developer's score
based on a data set gathered previously in a different module.
"""

# This import fixes a linting error with old division.
from __future__ import division
import data_collection

# Helpful reminders:
# Use pipeline programming style
# Implement test cases as functions are written in the test_individual_scoring.py file
# Scoring will be done first as percentages ((individual contribution/total branch)*100)

# Add fake data that corresponds to overall-eval-analyzing-metrics branch
# github_data uses the pattern ["username", commit_total, lines_added,
# lines_deleted, total_lines, modified_lines, lines_per_commit, files_changed]


# NOTE This is the fake data, it does not have key for the email for now, for tesing purposes
github_data = {
    "noorbuchi": {"email": "email", "COMMITS": 28, "ADDED": 349, "REMOVED": 70},
    "bagashvilit": {"email": "email","COMMITS": 22, "ADDED": 355, "REMOVED": 56},
    "Jordan-A": {"email": "email","COMMITS": 23, "ADDED": 375, "REMOVED": 43},
    "WonjoonC": {"email": "email","COMMITS": 27, "ADDED": 365, "REMOVED": 67},
    "Hannah Schultz": {"email": "email","COMMITS": 25, "ADDED": 315, "REMOVED": 75},
    "Alexander_Hamilton": {"email": "email","COMMITS": 41, "ADDED": 350, "REMOVED": 54},
    "Karl_Marx": {"email": "email","COMMITS": 0, "ADDED": 0, "REMOVED": 0},
    "Julius_Caesar": {"email": "email","COMMITS": 25, "ADDED": 363, "REMOVED": 35},
    "Napoleon_Bonaparte": {"email": "email","COMMITS": 24, "ADDED": 540, "REMOVED": 2},
    "Alexander_the_Great": {"email": "email","COMMITS": 42, "ADDED": 355, "REMOVED": 50},
}

# NOTE: The following code block still needs to be fixed in terms of variable
# names and docstrings.

#github_data = data_collection.calculate_individual_metrics("individual_metrics_testfile")
# pylint: disable=round-builtin
data_collection.add_raw_data_to_json("/home/teona/Documents/CS203/project/cogitate_tool", "individual_score_test")
github_data = data_collection.calculate_individual_metrics("individual_score_test")
def percentage_contribution(individual, overal_branch):
    """Calculate the individual contribution percentage."""
    return round(individual * 100 / overal_branch)


def sum_value(key):
    """Sum up all the values in branch per key."""
    return sum(d[key] for d in github_data.values() if d)


#Print usename and percentage of their contribution for each category
def print_data():
    """Print out github_data scores."""
    for username, data in github_data.items():
        print("\n", username)
        for category,value in data.items():
            if isinstance(value, int):
                print(
                    category,
                    percentage_contribution(
                        value, sum_value(category)
                        ),
                        "%",
                        )



if __name__ == "__main__":

    # for username in github_data:
    #     print (get_weighted(username))
    #print(data_collection.calculate_individual_metrics("individual_metrics_testfile"))
    print_data()

    # def individual_commitmnet(username, category):
    #     """Get and send value for key."""
    #     return github_data.get(username).get(category)

    # weights = {
    # "COMMITS": 0.2,
    # "ADDED": 0.4,
    # "REMOVED": 0.4 }

    # def get_weighted(User):
    #     user=github_data[User]
    #
    #     weighted={User: {k:(round(user[k]*weights[k])) for k in user.keys()}}
    #     return weighted
