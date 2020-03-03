import pytest
from src import data_collection


@pytest.mark.xfail
def test_collect_commits_user_email_key():
    dict = {}
    assert len(dict) == 0
    dict = data_collection.collect_commits_user_email_key(data_collection.repo_path)
    assert len(dict) != 0


@pytest.mark.xfail
def test_collect_commits_hash():
    list = []
    assert len(list) == 0
    list = data_collection.collect_commits_hash(data_collection.repo_path)
    assert len(list) != 0
