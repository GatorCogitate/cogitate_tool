"""Test to ensure that the functions to count the lines \
of code program are correct."""

from src import count_code_lines


def test_get_commit_lines_populates_data_0():
    """Checks that the size of the input variable is correct."""
    data_list = {}
    # pylint: disable=len-as-condition
    assert len(data_list) == 0
    data_list = count_code_lines.get_commit_lines("")
    assert len(data_list) != 0
