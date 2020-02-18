"""Test to ensure that the functions to count the lines of code program are correct."""

from src import count_code_lines


def test_get_commit_lines_populates_data_0():
    """Checks that the size of the input variable is correct."""
    # pylint: disable=len-as-condition
    assert len(count_code_lines.DATA_LINES) != 0
    count_code_lines.get_commit_lines(count_code_lines.PATH_REPO)
    assert len(count_code_lines.DATA_LINES) != 0
