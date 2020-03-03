"""Ensure that the functions to count the lines

of code program are correct.
"""

import pytest

from src import individual_metrics
from src import print_table
from src import json_handler


def test_raw_data_exists_in_testfile():
    """Checks the existence of the key RAW_DATA in individual_metrics_testfile."""
    test_dict = json_handler.get_dict_from_json_file("individual_metrics_testfile")
    assert "RAW_DATA" in test_dict.keys()


def test_calculate_individual_metrics_populates_data():
    """Checks that the function retruns a populated dictionary."""
    test_dict = {}
    # pylint: disable=len-as-condition
    assert len(test_dict) == 0
    test_dict = individual_metrics.calculate_individual_metrics(
        "individual_metrics_testfile"
    )
    assert len(test_dict) != 0
    assert "INDIVIDUAL_METRICS" in test_dict.keys()


def test_get_individual_metrics_accuracy():
    """Checks that individual_metrics data outputs correct values."""
    test_dict = individual_metrics.calculate_individual_metrics(
        "individual_metrics_testfile"
    )
    expected_dict = {
        "EMAIL": "buchin@allegheny.edu",
        "COMMITS": 1,
        "ADDED": 694,
        "REMOVED": 0,
        "TOTAL": 694,
        "MODIFIED": 694,
        "RATIO": 694,
        "FILES": ["Pipfile", "Pipfile.lock", "UsingPyGithub.py", "lint.sh", "test.sh"],
        "FORMAT": [".lock", ".py", ".sh", "Pipfile"],
    }
    assert test_dict["INDIVIDUAL_METRICS"]["noorbuchi"] == expected_dict


# TODO additional test cases needed


@pytest.mark.parametrize(
    "input_lines,input_commits,expected_output", [(50, 50, 1), (1, 1, 1), (0, 1, 0)],
)
def test_get_commit_average(input_lines, input_commits, expected_output):
    """Checks that the function correctly calculates the ratio."""
    assert (
        individual_metrics.get_commit_average(input_lines, input_commits)
    ) == expected_output
