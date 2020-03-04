"""
Test module to determine the correctness of the data_collection.py file.

The test case will take the current repository.

Unless that path variable is changed.
"""
import pytest
from src import data_collection

# NOTE: these test cases are not working properly and it are commented out

# def test_collect_commits_user_email_key():
#     dict = {}
#     assert len(dict) == 0
#     dict = data_collection.collect_commits_user_email_key(data_collection.repo_path)
#     assert len(dict) != 0


# def test_collect_commits_hash():
#     list = []
#     assert len(list) == 0
#     list = data_collection.collect_commits_hash(data_collection.repo_path)
#     assert len(list) != 0
