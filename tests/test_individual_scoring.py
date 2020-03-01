"""
A file for testing the scoring on an individual basis based on gathered

data from a Github repository.
"""

import pytest
import operator
import math

from src import individual_scoring

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
    ],
)
def test_percentage(input_username, input_category, expected_percentage):
    """Function to determine the correctness of percent of overall branches."""
    test_current_user = individual_scoring.individual_commitmnet(
        input_username, input_category
    )
    test_sum_value = individual_scoring.sum_value(input_category)

    test_percentage = round(
        individual_scoring.percentage_score(test_current_user, test_sum_value)
    )

    assert (test_percentage) == expected_percentage
    assert (test_percentage) != -1
    assert len(test_percentage) != 0


def test_sum_value():
    """Function to determine the correctness of the values in branch per key."""


def test_individual_commitnet():
    """Function to determine the correctness of the return value for a key."""
