"""
Test module to determine the correctness of the data_collection.py file.

The test case will take the current repository.

Unless that path variable is changed.
"""
import pytest
import os
from src import data_collection
from src import json_handler


@pytest.mark.parametrize(
    "input_dict,kept_entry,removed_entry,expected_dict",
    [
        (
            {
                "Noor Buchi": {
                    "EMAIL": "",
                    "COMMITS": 7,
                    "ADDED": 60,
                    "REMOVED": 3,
                    "FILES": ["README.md", "settings.json", "travis.yml", "Pipfile",],
                    "issues_commented": [30, 30],
                    "issues_opened": [25, 57],
                    "pull_requests_commented": [58, 58, 58, 58],
                    "pull_requests_opened": [],
                    "COMMITS_TO_TESTING": 5,
                    "COMMITS_ELSEWHERE": 5,
                },
                "noorbuchi": {
                    "EMAIL": "",
                    "COMMITS": 3,
                    "ADDED": 40,
                    "REMOVED": 7,
                    "FILES": ["README.md", "settings.json", "travis.yml"],
                    "issues_commented": [63, 53],
                    "issues_opened": [16],
                    "pull_requests_commented": [58, 58, 58, 58],
                    "pull_requests_opened": [58, 17],
                    "COMMITS_TO_TESTING": 10,
                    "COMMITS_ELSEWHERE": 10,
                },
            },
            "noorbuchi",
            "Noor Buchi",
            {
                "noorbuchi": {
                    "EMAIL": "",
                    "COMMITS": 10,
                    "ADDED": 100,
                    "REMOVED": 10,
                    "FILES": ["Pipfile", "README.md", "settings.json", "travis.yml"],
                    "issues_commented": [63, 53, 30, 30],
                    "issues_opened": [16, 25, 57],
                    "pull_requests_commented": [58, 58, 58, 58, 58, 58, 58, 58],
                    "pull_requests_opened": [58, 17],
                    "COMMITS_TO_TESTING": 15,
                    "COMMITS_ELSEWHERE": 15,
                }
            },
        )
    ],
)
def test_merge_duplicate_usernames(
    input_dict, kept_entry, removed_entry, expected_dict
):
    """Use parametrized testing to ensure entries are merged correctly and.

    Unwanted entry is discarded.
    """
    actual_dict = data_collection.merge_duplicate_usernames(
        input_dict, kept_entry, removed_entry
    )
    assert actual_dict == expected_dict


@pytest.mark.parametrize(
    "metrics_dict,issues_dict,expected_dict",
    [
        (
            {
                "schultzh": {
                    "EMAIL": "",
                    "COMMITS": 7,
                    "ADDED": 60,
                    "REMOVED": 3,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": ["README.md", "settings.json", "travis.yml"],
                    "FORMAT": [],
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                }
            },
            {
                "schultzh": {
                    "issues_commented": [63, 53, 30, 30, 30,],
                    "issues_opened": [16],
                    "pull_requests_commented": [58, 58, 58, 58,],
                    "pull_requests_opened": [58, 17],
                }
            },
            {
                "schultzh": {
                    "EMAIL": "",
                    "COMMITS": 7,
                    "ADDED": 60,
                    "REMOVED": 3,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": ["README.md", "settings.json", "travis.yml"],
                    "FORMAT": [],
                    "issues_commented": [63, 53, 30, 30, 30,],
                    "issues_opened": [16],
                    "pull_requests_commented": [58, 58, 58, 58,],
                    "pull_requests_opened": [58, 17],
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                }
            },
        ),
        (
            {
                "noorbuchi": {
                    "EMAIL": "",
                    "COMMITS": 7,
                    "ADDED": 60,
                    "REMOVED": 3,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": ["README.md", "settings.json", "travis.yml"],
                    "FORMAT": [],
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                }
            },
            {
                "schultzh": {
                    "issues_commented": [63, 53, 30, 30, 30,],
                    "issues_opened": [16],
                    "pull_requests_commented": [58, 58, 58, 58,],
                    "pull_requests_opened": [58, 17],
                }
            },
            {
                "noorbuchi": {
                    "EMAIL": "",
                    "COMMITS": 7,
                    "ADDED": 60,
                    "REMOVED": 3,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": ["README.md", "settings.json", "travis.yml"],
                    "FORMAT": [],
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                },
                "schultzh": {
                    "EMAIL": "N/A",
                    "COMMITS": 0,
                    "ADDED": 0,
                    "REMOVED": 0,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": [],
                    "FORMAT": [],
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                    "issues_commented": [63, 53, 30, 30, 30,],
                    "issues_opened": [16],
                    "pull_requests_commented": [58, 58, 58, 58,],
                    "pull_requests_opened": [58, 17],
                },
            },
        ),
    ],
)
def test_merge_metric_and_issue_dicts_already_exists(
    metrics_dict, issues_dict, expected_dict
):
    """Uses parametrized testing to make sure merging funciton is working properly"""
    actual_dict = data_collection.merge_metric_and_issue_dicts(
        metrics_dict, issues_dict
    )
    assert actual_dict == expected_dict


@pytest.mark.parametrize(
    "file_list,expected_list",
    [
        (["data_collection.py", "data_collection.py", "data_collection.py"], [".py"]),
        (["data_collection.py", "data_collection.py", "json_handler.py"], [".py"]),
        (["data_collection.py", "lint.sh", "travis.yml"], [".py", ".sh", ".yml"]),
    ],
)
def test_get_file_formats(file_list, expected_list):
    """Use parametrized testing to check duplicates are eliminated."""
    actual_list = data_collection.get_file_formats(file_list)
    assert actual_list == expected_list


@pytest.mark.parametrize(
    "file_name,expected_type",
    [("Pipfile", "Pipfile"), ("test.sh", ".sh"), (".travis.yml", ".yml")],
)
def test_parse_for_type(file_name, expected_type):
    """Use parametrized testing to check the file being parsed correctly."""
    actual_name = data_collection.parse_for_type(file_name)
    assert actual_name == expected_type


def test_initialize_contributor_data():
    """Check that the function returns a valid dictionary."""
    data = data_collection.initialize_contributor_data("individual_metrics_testfile")
    assert not len(data) == 0
    assert "RAW_DATA" in data.keys()


def test_collect_and_add_raw_data_to_json(tmp_path):
    """Check that raw data was collected from the repository and was written."""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "raw_data_testfile.json"
    entry = '"Keep this file empty" : []'
    p1.write_text("{" + entry + "}")
    # retreive the dictionary from the test file
    data_from_file = json_handler.get_dict_from_json_file("raw_data_testfile", d)
    # Makes sure that the default key is in the dicitionary
    # The key is called "Keep this file empty"
    assert "Keep this file empty" in data_from_file
    repository = "https://github.com/GatorCogitate/cogitate_tool"
    # Call collect and write funciton
    data_collection.collect_and_add_raw_data_to_json(
        repository, "raw_data_testfile", d, overwrite=True
    )
    # Update dicitionary from the new data in the file
    data_from_file = json_handler.get_dict_from_json_file("raw_data_testfile", d)
    # Make sure the correct key is added
    assert "RAW_DATA" in data_from_file


def test_collect_and_add_raw_data_to_json_no_overwrite(tmp_path):
    """Check that raw data was collected from the repository and was written."""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "raw_data_testfile_no_overwrite.json"
    entry = '"Keep this file empty" : []'
    p1.write_text("{" + entry + "}")
    # retreive the dictionary from the test file
    data_from_file = json_handler.get_dict_from_json_file(
        "raw_data_testfile_no_overwrite", d
    )
    # Makes sure that the default key is in the dicitionary
    # The key is called "Keep this file empty"
    assert "Keep this file empty" in data_from_file
    repository = "https://github.com/GatorCogitate/cogitate_tool"
    # Call collect and write funciton
    data_collection.collect_and_add_raw_data_to_json(
        repository, "raw_data_testfile_no_overwrite", d, overwrite=False
    )
    # Update dicitionary from the new data in the file
    data_from_file = json_handler.get_dict_from_json_file(
        "raw_data_testfile_no_overwrite", d
    )
    # Make sure the correct key is added
    assert "RAW_DATA" in data_from_file
    assert "Keep this file empty" in data_from_file


def test_collect_and_add_individual_metrics_to_json(tmp_path):
    """Check that calculated data was collected from the repository and was written."""
    read_test_file = "individual_metrics_testfile"
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "calculated_metrics_testfile.json"
    entry = '"Keep this file empty" : []'
    p1.write_text("{" + entry + "}")
    # retreive the dictionaries from the test file
    calculated_data_from_file = json_handler.get_dict_from_json_file(
        "calculated_metrics_testfile", d
    )
    raw_data_from_file = json_handler.get_dict_from_json_file(read_test_file)
    # Makes sure that the default values are in the dicitionaries
    # The key is called "Keep this file empty"
    assert "Keep this file empty" in calculated_data_from_file
    # makes sure RAW_DATA is a key in the individual_metrics_testfile
    assert "RAW_DATA" in raw_data_from_file
    # Call collect and write funciton
    data_collection.collect_and_add_individual_metrics_to_json(
        read_test_file, "calculated_metrics_testfile", d, overwrite=True
    )
    # Update dicitionary from the new data in the file
    calculated_data_from_file = json_handler.get_dict_from_json_file(
        "calculated_metrics_testfile", d
    )
    # Make sure the correct keys are added
    expected_keys = [
        "schultzh",
        "WonjoonC",
        "Jordan-A",
        "noorbuchi",
        "Chris Stephenson",
    ]
    actual_keys = list(calculated_data_from_file.keys())
    assert actual_keys == expected_keys


def test_collect_and_add_individual_metrics_to_json_no_overwrite(tmp_path):
    """Check that calculated data was collected from the repository and was written."""
    read_test_file = "individual_metrics_testfile"
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "calculated_metrics_testfile.json"
    entry = '"Keep this file empty" : []'
    p1.write_text("{" + entry + "}")
    # retreive the dictionaries from the test file
    calculated_data_from_file = json_handler.get_dict_from_json_file(
        "calculated_metrics_testfile", d
    )
    raw_data_from_file = json_handler.get_dict_from_json_file(read_test_file)
    # Makes sure that the default values are in the dicitionaries
    # The key is called "Keep this file empty"
    assert "Keep this file empty" in calculated_data_from_file
    # makes sure RAW_DATA is a key in the individual_metrics_testfile
    assert "RAW_DATA" in raw_data_from_file
    # Call collect and write funciton
    data_collection.collect_and_add_individual_metrics_to_json(
        read_test_file, "calculated_metrics_testfile", d, overwrite=False
    )
    # Update dicitionary from the new data in the file
    calculated_data_from_file = json_handler.get_dict_from_json_file(
        "calculated_metrics_testfile", d
    )
    # Make sure the correct keys are added
    expected_keys = [
        "Keep this file empty",
        "schultzh",
        "WonjoonC",
        "Jordan-A",
        "noorbuchi",
        "Chris Stephenson",
    ]
    actual_keys = list(calculated_data_from_file.keys())
    assert actual_keys == expected_keys


def test_raw_data_exists_in_testfile():
    """Checks the existence of the key RAW_DATA in individual_metrics_testfile."""
    test_dict = json_handler.get_dict_from_json_file("individual_metrics_testfile")
    assert "RAW_DATA" in test_dict.keys()


@pytest.mark.parametrize(
    "json_file_name", [("individual_metrics_testfile")],
)
def test_calculate_individual_metrics_full(json_file_name):
    """Check that the individual metrics have been calculated."""
    data = data_collection.calculate_individual_metrics(json_file_name)
    assert not len(data) == 0


def test_calculate_individual_metrics_empty(tmp_path):
    """Check that the individual metrics have been calculated."""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "metrics_testfile.json"
    p1.write_text("{}")
    data = data_collection.calculate_individual_metrics("metrics_testfile", d)
    assert len(data) == 0


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
        "MODIFIED": 0,
        "RATIO": 0,
        "FILES": ["Pipfile", "Pipfile.lock", "UsingPyGithub.py", "lint.sh", "test.sh"],
        "FORMAT": [],
        "issues_commented": [],
        "issues_opened": [],
        "pull_requests_commented": [],
        "pull_requests_opened": [],
        "COMMITS_TO_TESTING": 1,
        "COMMITS_ELSEWHERE": 0,
    }
    assert test_dict["noorbuchi"] == expected_dict


def test_get_individual_metrics_populates_keys():
    """Checks that individual_metrics data hass correct keys."""
    test_dict = data_collection.calculate_individual_metrics(
        "individual_metrics_testfile"
    )
    expected_keys = [
        "schultzh",
        "WonjoonC",
        "Jordan-A",
        "noorbuchi",
        "Chris Stephenson",
    ]
    internal_keys = list(test_dict.keys())
    assert internal_keys == expected_keys


# The following two test cases use Pydriller to collect actual data from
# Cogitate tool repository
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


@pytest.mark.parametrize(
    "input_lines,input_commits,expected_output", [(50, 50, 1), (1, 1, 1), (0, 0, 0)],
)
def test_get_commit_average(input_lines, input_commits, expected_output):
    """Checks that the function correctly calculates the ratio."""
    assert (
        data_collection.get_commit_average(input_lines, input_commits)
    ) == expected_output
