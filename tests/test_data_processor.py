"""A file for testing the functions in data_processor.py."""

import pytest
import data_processor as dp


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
    dictionary = dp.individual_contribution(input_dictionary)
    assert dictionary == expected_dictionary


@pytest.mark.parametrize(
    "input_list, expected_score",
    [([32, 37, 34, 35, 33, 35, 33, 32, 4, 2, 55, 74, 102], 45.0)],
)
def test_calculate_iqr_score(input_list, expected_score):
    """Function to determine the accuracy of an iqr score for a certain category."""
    score = dp.calculate_iqr_score(input_list, 0.2, 0.2, 0.6)
    assert score == expected_score


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
                },
                "bagashvilit": {
                    "email": "email",
                    "COMMITS": 22,
                    "ADDED": 355,
                    "REMOVED": 56,
                },
            },
            {"COMMITS": [28, 22], "ADDED": [349, 355], "REMOVED": [70, 56], },
        ),
    ],
)
def test_iterate_nested_dictionary(input_dictionary, expected_dictionary):
    new_dictionary = dp.iterate_nested_dictionary(input_dictionary)
    assert new_dictionary == expected_dictionary


@pytest.mark.parametrize(
    "input_dictionary, expected_dictionary",
    [
        (
            {
                "noorbuchi": {
                    "email": "email",
                    "FORMAT": [".py", ".test"],
                    "ISSUES": ["A", "B", "C", "D"],
                },
                "bagashvilit": {
                    "email": "email",
                    "FORMAT": [".py", ".test", ".md"],
                    "ISSUES": ["A", "B"],
                },
            },
            {"FORMAT": [2, 3], "ISSUES": [4, 2], },
        ),
    ],
)
def test_iterate_dictionary_with_lists(input_dictionary, expected_dictionary):
    new_dictionary = dp.iterate_nested_dictionary(input_dictionary)
    assert new_dictionary == expected_dictionary


@pytest.mark.parametrize(
    "input_dictionary, expected_score",
    [
        (
            {
                "noorbuchi": {
                    "email": "email",
                    "COMMITS": 28,
                    "ADDED": 349,
                    "REMOVED": 70,
                },
                "bagashvilit": {
                    "email": "email",
                    "COMMITS": 22,
                    "ADDED": 355,
                    "REMOVED": 56,
                },
                "MaddyKapfhammer": {
                    "email": "email",
                    "COMMITS": 26,
                    "ADDED": 350,
                    "REMOVED": 63
                }
            },
            60.0
        ),
    ],
)
def test_calculate_team_score(input_dictionary, expected_score):
    team_score = dp.calculate_team_score(input_dictionary, 0.2, 0.2, 0.6)
    assert team_score == expected_score
