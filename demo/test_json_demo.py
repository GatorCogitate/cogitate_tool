
import json_demo
import os


def test_write_dict_to_json():
    """Ensure a dictionary is written to a specified file."""
    test_dictionary = {"username": "test_data"}
    json_string = json_demo.write_dict_to_json_file(test_dictionary, "testfile")
    for key in test_dictionary.keys():
        assert key in json_string  # every expected user is in output
    assert "testfile.json" in os.listdir("./data/")  # file is created
    with open("./data/testfile.json") as file:
        file_contents = file.read()
        assert "username" in file_contents
        assert "test_data" in file_contents


def test_get_dict_from_json():
    """Ensure data is correctly pulled from a json file."""
    assert "demofile.json" in os.listdir("./data/")  # demofile exists
    test_dictionary = json_demo.get_dict_from_json_file("demofile")
    assert "testuser" in test_dictionary.keys()  # dictionary was populated correctly


def test_add_user_to_json():
    """Ensure users can be added to a json file."""
    test_dictionary = {"username": "test_data"}
    user_to_add = {"new_user": "test_data"}
    json_string = json_demo.add_user_to_json(test_dictionary,
                                             user_to_add,
                                             "new_user",
                                             "testfile")
    assert "testfile.json" in os.listdir("./data/")  # testfile exists
    assert "new_user" in json_string  # added user in output
    with open("./data/testfile.json") as file:
        file_contents = file.read()
        for key in test_dictionary.keys():
            assert key in file_contents  # every expected user in output
        assert "new_user" in file_contents  # added user in file
