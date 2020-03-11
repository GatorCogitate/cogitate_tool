"""
A file for testing the individual contribution based on gathered
data from a Github repository.
"""

import pytest
import operator
import math

from src import Individual_score


@pytest.mark.parametrize(
    "input_dictionary, expected_dictionary",
    [
        (
            {
                "noorbuchi": {
                    "email": "email",
                    "COMMITS": 28,
                    "ADDED": 349,
                    "REMOVED": 70,
                    "files": ["sting", "strings"],
                },
                "bagashvilit": {
                    "email": "email",
                    "COMMITS": 22,
                    "ADDED": 355,
                    "REMOVED": 56,
                    "files": ["sting", "strings"],
                },
            },
            {
                "noorbuchi": {
                    "COMMITS": 56,
                    "ADDED": 50,
                    "REMOVED": 56,
                    "files": (50, ["sting", "strings"]),
                },
                "bagashvilit": {
                    "COMMITS": 44,
                    "ADDED": 50,
                    "REMOVED": 44,
                    "files": (50, ["sting", "strings"]),
                },
            },
        ),
    ],
)
def test_individual_contribution(input_dictionary, expected_dictionary):
    """Function to determine the accuracy of individual contribution calculations."""
    dictionary = Individual_score.individual_contribution(input_dictionary)
    assert dictionary == expected_dictionary
