"""A file for testing the functions in data_processor.py."""

import pytest
import data_processor as dp


@pytest.mark.parametrize(
    "input_dictionary, expected_dictionary",
    [
        (
            {
                "Noor Buchi": {
                    "EMAIL": "",
                    "COMMITS": 10,
                    "ADDED": 100,
                    "REMOVED": 10,
                    "FILES": ["Pipfile", "README.md", "settings.json", "travis.yml"],
                    "issues_commented": [63, 53, 30, 30],
                    "issues_opened": [16, 25, 57],
                    "pull_requests_commented": [58, 58, 58, 58, 58, 58, 58, 58],
                    "pull_requests_opened": [58, 17],
                    "MODIFIED": 0,
                    "FORMAT": [],
                    "RATIO": 0,
                },
            },
            {
                "Noor Buchi": {
                    "EMAIL": "",
                    "COMMITS": 10,
                    "ADDED": 100,
                    "REMOVED": 10,
                    "FILES": ["Pipfile", "README.md", "settings.json", "travis.yml"],
                    "issues_commented": [63, 53, 30, 30],
                    "issues_opened": [16, 25, 57],
                    "pull_requests_commented": [58, 58, 58, 58, 58, 58, 58, 58],
                    "pull_requests_opened": [58, 17],
                    "MODIFIED": 110,
                    "FORMAT": [".json", ".md", ".yml", "Pipfile"],
                    "RATIO": 11,
                }
            },
        )
    ],
)
def test_add_new_metrics(input_dictionary, expected_dictionary):
    """Test that calculated metrics are done correctly"""
    input_dictionary = dp.add_new_metrics(input_dictionary)
    # print(input_dictionary)
    assert input_dictionary == expected_dictionary


@pytest.mark.parametrize(
    "input_dictionary, expected_dictionary",
    [
        (
            {
                "noorbuchi": {
                    "email": "email",
                    "COMMITS": 0,
                    "ADDED": 349,
                    "REMOVED": 70,
                    "files": ["sting", "strings"],
                    "issues": [],
                },
                "bagashvilit": {
                    "email": "email",
                    "COMMITS": 0,
                    "ADDED": 355,
                    "REMOVED": 56,
                    "files": ["sting", "strings"],
                    "issues": [],
                },
            },
            {
                "noorbuchi": {
                    "COMMITS": 0,
                    "ADDED": 50,
                    "REMOVED": 56,
                    "files": (50, ["sting", "strings"]),
                    "issues": 0,
                },
                "bagashvilit": {
                    "COMMITS": 0,
                    "ADDED": 50,
                    "REMOVED": 44,
                    "files": (50, ["sting", "strings"]),
                    "issues": 0,
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
            {"COMMITS": [28, 22], "ADDED": [349, 355], "REMOVED": [70, 56],},
        ),
    ],
)
def test_iterate_nested_dictionary(input_dictionary, expected_dictionary):
    """Determine if nested dictionary iteration creates correct new dictionary."""
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
            {"FORMAT": [2, 3], "ISSUES": [4, 2],},
        ),
    ],
)
def test_iterate_dictionary_with_lists(input_dictionary, expected_dictionary):
    """Determine that dictionary with lists adds length to new dictionary values."""
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
                    "REMOVED": 63,
                },
            },
            60.0,
        ),
    ],
)
def test_calculate_team_score(input_dictionary, expected_score):
    """Determine that team score is calculated with category average."""
    team_score = dp.calculate_team_score(input_dictionary, 0.2, 0.2, 0.6)
    assert team_score == expected_score
