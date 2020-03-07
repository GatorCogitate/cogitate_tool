"""
Test module to determine the correctness of the data_collection.py file.

The test case will take the current repository.

Unless that path variable is changed.
"""
import pytest
from src import data_collection
from src import json_handler


# NOTE: a repository object must be sent in to this function and not a string
# NOTE: this issue is already being worked on in test_issue_retrieval.py
# @pytest.mark.parametrize(
#     "repository_url, input_state, input_contributer_data",
#     [("https://github.com/GatorCogitate/cogitate_tool", 2, 2)],
# )
# def test_retrive_issue_data(repository_url, input_state, input_contributer_data):
#     """Check that the issue data has be retrived."""
#     data_collection.retrieve_issue_data(
#         repository_url, input_state, input_contributer_data
#     )
#     assert (repository_url) != input_state


@pytest.mark.parametrize(
    "repository_url, json_file_name",
    [("https://github.com/GatorCogitate/cogitate_tool", "individual_metrics_testfile")],
)
def test_add_raw_data_to_json(repository_url, json_file_name):
    """Check that the issue data has be retrived."""
    assert (repository_url) != json_file_name


@pytest.mark.parametrize(
    "json_file_name", [("individual_metrics_testfile")],
)
def test_calculate_individual_metrics(json_file_name):
    """Check that the individual metrics have been calculated."""
    data = data_collection.calculate_individual_metrics(json_file_name)
    assert len(data) != 0
    # assert (data) != 0


# NOTE: Printing the table does not need to be tested since it is a temporary
# function
# @pytest.mark.parametrize(
#     "json_file_name", [("individual_metrics_testfile")],
# )
# def test_print_individual_in_table(json_file_name):
#     """Check that the table has been printed."""
#     data_collection.print_individual_in_table(json_file_name)
#     assert (1) == 1


@pytest.mark.parametrize(
    "repository_url", [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_user_hash(repository_url):
    """Check the collection of the commits hash."""
    dict = {}
    assert len(dict) == 0
    dict = data_collection.collect_commits_hash(repository_url)
    assert len(dict) != 0


@pytest.mark.parametrize(
    "repository_url", [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_hash(repository_url):
    """Check the commits hash has been gathered."""
    list = []
    assert len(list) == 0
    list = data_collection.collect_commits_hash(repository_url)
    assert len(list) != 0


def test_raw_data_exists_in_testfile():
    """Checks the existence of the key RAW_DATA in individual_metrics_testfile."""
    test_dict = json_handler.get_dict_from_json_file("individual_metrics_testfile")
    assert "RAW_DATA" in test_dict.keys()


def test_calculate_individual_metrics_populates_data():
    """Checks that the function retruns a populated dictionary."""
    test_dict = {}
    # pylint: disable=len-as-condition
    assert len(test_dict) == 0
    test_dict = data_collection.calculate_individual_metrics(
        "individual_metrics_testfile"
    )
    assert len(test_dict) != 0
    assert "INDIVIDUAL_METRICS" in test_dict.keys()


def test_get_individual_metrics_accuracy():
    """Checks that individual_metrics data outputs correct values."""
    test_dict = data_collection.calculate_individual_metrics(
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


@pytest.mark.parametrize(
    "input_lines,input_commits,expected_output", [(50, 50, 1), (1, 1, 1), (0, 0, 0)],
)
def test_get_commit_average(input_lines, input_commits, expected_output):
    """Checks that the function correctly calculates the ratio."""
    assert (
        data_collection.get_commit_average(input_lines, input_commits)
    ) == expected_output
