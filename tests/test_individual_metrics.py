"""Ensure that the functions to count the lines

of code program are correct.
"""

import pytest

from src import individual_metrics
from src import print_table


# TODO fix test case
def test_get_commit_lines_populates_data_0():
    """Checks that the size of the input variable is correct."""
    data_list = {}
    # pylint: disable=len-as-condition
    assert len(data_list) == 0
    data_list = individual_metrics.calculate_individual_metrics("")
    assert len(data_list) != 0


# TODO implement test case
def test_get_commit_data():
    """Checks that the function correctly gets data."""


# TODO implement test case
def test_print_table():
    """Checks that the module outputs the data table."""
    data = individual_metrics.calculate_individual_metrics("")
    # print_table.print_in_table(data)


# TODO additional test cases needed


@pytest.mark.parametrize(
    "input_lines,input_commits,expected_output", [(50, 50, 1), (1, 1, 1), (0, 1, 0)],
)
def test_get_commit_average(input_lines, input_commits, expected_output):
    """Checks that the function correctly calculates the ratio."""
    assert (
        individual_metrics.get_commit_average(input_lines, input_commits)
    ) == expected_output
