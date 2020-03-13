"""
Test suite for JSON processing.

The test case will take the data repository.

Unless that path variable is changed.
"""
import os
import pytest
from src import json_handler


@pytest.mark.parametrize(
    "test_dictionary,json_name",
    [
        ({"username": "test_data"}, "testfile"),
        ({"username": "test_data"}, "testfile.json"),
    ],
)
def test_write_dict_to_json(test_dictionary, json_name):
    """Ensure a dictionary is written to a specified file."""
    json_handler.write_dict_to_json_file(test_dictionary, json_name)
    if ".json" in json_name:
        assert json_name in os.listdir("./data/")  # file is created
        assert json_name + ".json" not in os.listdir("./data/")
        # Input handling created correct file
    else:
        assert json_name + ".json" in os.listdir("./data/")  # file is created
        assert json_name + ".json.json" not in os.listdir("./data/")
    with open("./data/testfile.json") as file:
        file_contents = file.read()
        assert "username" in file_contents
        assert "test_data" in file_contents


@pytest.mark.parametrize(
    "json_name,expected_contents",
    [
        ("individual_metrics_testfile", ["stephensonc", "koscinskic", "schultzh"]),
        ("individual_metrics_testfile.json", ["stephensonc", "koscinskic", "schultzh"]),
    ],
)
def test_get_dict_from_json(json_name, expected_contents):
    """Ensure data is correctly pulled from a json file."""
    if ".json" in json_name:
        assert json_name in os.listdir("./data/")  # file is created
        assert json_name + ".json" not in os.listdir("./data/")
        # Input handling created correct file
    else:
        assert json_name + ".json" in os.listdir("./data/")  # file is created
        assert json_name + ".json.json" not in os.listdir("./data/")
    # file to test exists
    test_dictionary = json_handler.get_dict_from_json_file(json_name)
    for user in expected_contents:
        assert user in test_dictionary.keys()
    # dictionary was populated correctly


# Checks that method correctly appends user to the test_dictionary.
def test_add_user_to_users_dictionary():
    """Ensure users can be added to a json file."""
    test_dictionary = {"username": "test_data"}
    user_to_add = {"new_user": "test_data"}
    json_handler.add_user_to_users_dictionary(test_dictionary, user_to_add)
    assert "new_user" in test_dictionary.keys()
    assert "test_data" in test_dictionary["new_user"]
