"""
Test module to determine the correctness of the data_collection.py file.

The test case will take the current repository.

Unless that path variable is changed.
"""
import pytest
from src import data_collection

@pytest.mark.xfail
@pytest.mark.parametrize(
    "repository_url",
    [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_user_email_key(repository_url):
    dict = {}
    assert len(dict) == 0
    dict = data_collection.collect_commits_user_email_key(repository_url)
    assert len(dict) != 0


@pytest.mark.parametrize(
    "repository_url",
    [("https://github.com/GatorCogitate/cogitate_tool")],
)
def test_collect_commits_hash(repository_url):
    list = []
    assert len(list) == 0
    list = data_collection.collect_commits_hash(repository_url)
    assert len(list) != 0
