"""Test cases to check the functionality of data_collection"""
# TODO: possible change to docstring
import pytest
from src import data_collection


def test_collect_commits_user_email_key():
    """Check if function fills the dictionary."""
    dictionary = {}
    assert len(dictionary) == 0
    # TODO: linter error Module 'src.data_collection'
    # has no 'collect_commits_user_email_key' member
    dictionary = data_collection.collect_commits_user_email_key(
        # TODO: linter error Module 'src.data_collection' has no 'repo_path' member
        data_collection.repo_path
    )
    assert len(dictionary) != 0


def test_collect_commits_hash():
    """Check if function fills the list."""
    test_list = []
    assert len(test_list) == 0
    # TODO: linter error Module 'src.data_collection' has no 'repo_path' member
    test_list = data_collection.collect_commits_hash(data_collection.repo_path)
    assert len(test_list) != 0
