"""Contains the test case(s) for retrieve_issue_data in data_collection."""

import os
import pytest
from github import Github
from github import GithubException
from src import data_collection
from src import json_handler


def test_retireve_token_with_travis():
    """Test to ensure the retrieval of the Travis token."""
    assert os.environ.get("PYGITHUB_TOKEN") == data_collection.retrieve_token()


@pytest.mark.parametrize(
    "input_token,repository_name",
    # Toggle the cases below to switch from a hard-coded to Travis key
    # [("REDACTED","GatorCogitate/cogitate_tool")],
    [(data_collection.retrieve_token(), "GatorCogitate/cogitate_tool")],
)
def test_authenticate_repository_authenticates(input_token, repository_name):
    """Test to ensure the establishment of a repository."""
    repository = data_collection.authenticate_repository(input_token, repository_name)

    if repository == "INVALID":
        pytest.skip("Rate Limit Exceeded.")

    assert repository is not None


@pytest.mark.parametrize(
    "input_token,repository_name,state,contributor_data",
    [
        (
            # Toggle the inputs below to switch from a hard-coded to Travis key
            # "REDACTED",
            data_collection.retrieve_token(),
            "GatorCogitate/cogitate_tool",
            "all",
            json_handler.get_dict_from_json_file("contributor_data_template"),
        )
    ],
)
def test_retrieve_issue_data_retrieves_issues(
    # pylint: disable=bad-continuation
    input_token,
    repository_name,
    state,
    contributor_data,
):
    """Test to ensure all issues are associated with the correct contributor."""
    try:
        ghub = Github(input_token)
        repository = ghub.get_repo(repository_name)

        contributor_data = data_collection.retrieve_issue_data(
            repository, state, contributor_data
        )
    except GithubException:
        pytest.skip("Rate Limit Exceeded.")

    contributor_found = False

    for username in contributor_data:

        for issue_id in contributor_data[username]["issues_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            assert repository.get_issue(number=issue_id).user.login == username

        for issue_id in contributor_data[username]["issues_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True

        for issue_id in contributor_data[username]["pull_requests_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            assert repository.get_issue(number=issue_id).user.login == username

        for issue_id in contributor_data[username]["pull_requests_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True
