from src import count_code_lines

def test_get_commit_lines_populates_data_0():
    """Checks that the size of the input variable is correct."""
    # pylint: disable=len-as-condition
    assert len(count_code_lines.data) != 0
    count_code_lines.get_commit_lines(count_code_lines.path)
    assert len(count_code_lines.data) != 0
