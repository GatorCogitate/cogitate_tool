"""Test suite for JSON processing."""
import os
import pytest
from src import data_to_json


def test_write_dict_to_json():
    """Ensure a dictionary is written to a specified file."""
    test_dictionary = {"username": "test_data"}
    data_to_json.write_dict_to_json_file(test_dictionary, "testfile")
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
    test_dictionary = data_to_json.get_dict_from_json_file("contributor_data_template")
    for user in expected_contents:
        assert user in test_dictionary.keys()
    # dictionary was populated correctly


def test_add_user_to_users_dictionary():
    """Ensure users can be added to a json file."""
    test_dictionary = {"username": "test_data"}
    user_to_add = {"new_user": "test_data"}
    data_to_json.add_user_to_users_dictionary(test_dictionary, user_to_add)
    assert "new_user" in test_dictionary.keys()
    assert "test_data" in test_dictionary["new_user"]


@pytest.mark.xfail
@pytest.mark.parametrize(
    "repository_url",
    [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_user_email_key(repository_url):
    dict = {}
    assert len(dict) == 0
    dict = data_to_json.collect_commits_user_email_key(repository_url)
    assert len(dict) != 0


@pytest.mark.parametrize(
    "repository_url",
    [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_hash(repository_url):
    list = []
    assert len(list) == 0
    list = data_to_json.collect_commits_hash(repository_url)
    assert len(list) != 0
