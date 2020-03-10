"""A file for testing the scoring of a team based on data retrieved from GitHub
   and using the interquartile range."""

import pytest
import IQR_team_score


@pytest.mark.parametrize(
    "input_list, expected_score",
    [([32, 37, 34, 35, 33, 35, 33, 32, 4, 2, 55, 74, 102], 45.0),],
)
def test_calculate_iqr_score(input_list, expected_score):
    """Function to determine the accuracy of an iqr score for a certain category."""
    score = IQR_team_score.calculate_iqr_score(input_list)
    assert score == expected_score


# @pytest.mark.parametrize(
#     "input_dictionary, expected_list",
#     [
#         ({"noorbuchi": {"COMMITS": 28}, "bagashvilit": {"COMMITS": 22}}, [28, 22]),
#     ]
# )
# def test_determine_datasets(input_dictionary, expected_list):
#     """Function to determine the accuracy of list creation from a dictionary."""
#     IQR_team_score.commit_data = []
#     IQR_team_score.determine_datasets(input_dictionary)
#     actual_list = IQR_team_score.commit_data
#     assert actual_list == expected_list

# def test_calculate_team_average(input_dictionary):
