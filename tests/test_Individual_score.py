"""
A file for testing the scoring on an individual basis based on gathered
data from a Github repository.
"""

import pytest
import operator
import math

from src import Individual_score

# NOTE: These test case names and doc strings are not final due to the
# ongoing creation process of the individual_scoring.py file.


@pytest.mark.parametrize(
    "input_username, input_category, expected_percentage",
    [
        ("Julius_Caesar", "COMMITS", 10),
        ("Julius_Caesar", "ADDED", 11),
        ("Julius_Caesar", "REMOVED", 8),
        ("Napoleon_Bonaparte", "COMMITS", 9),
        ("Napoleon_Bonaparte", "ADDED", 16),
        ("Napoleon_Bonaparte", "REMOVED", 0),
        ("Alexander_the_Great", "COMMITS", 16),
        ("Alexander_the_Great", "ADDED", 11),
        ("Alexander_the_Great", "REMOVED", 11),
        ("Karl_Marx", "COMMITS", 0),
        ("Karl_Marx", "ADDED", 0),
        ("Karl_Marx", "REMOVED", 0),
        ("Alexander_Hamilton", "COMMITS", 16),
        ("Alexander_Hamilton", "ADDED", 10),
        ("Alexander_Hamilton", "REMOVED", 12),
    ],
)
def test_percentage(input_username, input_category, expected_percentage):
    """Function to determine the correctness of percent of overall branches."""
    test_current_user = Individual_score.individual_commitmnet(
        input_username, input_category
    )
    test_sum_value = Individual_score.sum_value(input_category)

    test_percentage = round(
        Individual_score.percentage_score(test_current_user, test_sum_value)
    )

    assert (test_percentage) == expected_percentage
    assert (test_percentage) != -1


@pytest.mark.parametrize(
    "input_username, input_category, amount_added",
    [
        ("Julius_Caesar", "COMMITS", 25),
        ("Julius_Caesar", "ADDED", 363),
        ("Julius_Caesar", "REMOVED", 35),
        ("Napoleon_Bonaparte", "COMMITS", 24),
        ("Napoleon_Bonaparte", "ADDED", 363),
        ("Napoleon_Bonaparte", "REMOVED", 35),
        ("Alexander_the_Great", "COMMITS", 42),
        ("Alexander_the_Great", "ADDED", 355),
        ("Alexander_the_Great", "REMOVED", 50),
        ("Karl_Marx", "COMMITS", 0),
        ("Karl_Marx", "ADDED", 0),
        ("Karl_Marx", "REMOVED", 0),
        ("Alexander_Hamilton", "COMMITS", 41),
        ("Alexander_Hamilton", "ADDED", 350),
        ("Alexander_Hamilton", "REMOVED", 452),
    ],
)
def test_sum_value(input_username, input_category, amount_added):
    """Function to determine the correctness of the values in branch per key."""
    test_sum_value = Individual_score.sum_value(input_category)
    # assert (amount_added) == test_sum_value


def test_individual_commitnet():
    """Function to determine the correctness of the return value for a key."""
