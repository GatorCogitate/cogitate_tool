"""
Test suite for JSON processing.

The test case will take the current repository.

Unless that path variable is changed.
"""
import os
import pytest
from src import json_handler

# Checks if the method creates the JSON file.
def test_write_dict_to_json():
    """Ensure a dictionary is written to a specified file."""
    test_dictionary = {"username": "test_data"}
    json_handler.write_dict_to_json_file(test_dictionary, "testfile")
    assert "testfile.json" in os.listdir("./data/")  # file is created
    with open("./data/testfile.json") as file:
        file_contents = file.read()
        assert "username" in file_contents
        assert "test_data" in file_contents


@pytest.mark.parametrize(
    "json_file,expected_contents",
    [("contributor_data_template", ["stephensonc", "koscinskic", "schultzh"])],
)
def test_get_dict_from_json(json_file, expected_contents):
    """Ensure data is correctly pulled from a json file."""
    assert json_file + ".json" in os.listdir("./data/")
    # demofile exists
    test_dictionary = json_handler.get_dict_from_json_file("contributor_data_template")
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
