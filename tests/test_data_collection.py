"""
Test module to determine the correctness of the data_collection.py file.

The test case will take the current repository.

Unless that path variable is changed.
"""
import pytest
from src import data_collection
from src import json_handler


def test_authenticate_repository():
    """Determine that the repository has been authenticated."""


def test_retrive_issue_data():
    """Check that the issue data has be retrived."""


def test_add_raw_data_to_json():
    """Check that the issue data has be retrived."""


def test_calculate_individual_metrics():
    """Check that the individual metrics have been calculated."""


def test_find_repositories():
    """Check that the repositories have been found."""


def test_print_individual_in_table():
    """Check that the table has been printed."""


@pytest.mark.xfail
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
