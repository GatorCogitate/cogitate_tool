"""Contains the test case(s) for retrieve_issue_data in data_collection."""

import pytest
from github import Github
from src import data_collection
from src import json_handler


def test_retrieve_travis_token_retrieves_token():
    """Test to ensure the retrieval of a Travis token."""
    token = data_collection.retrieve_travis_token()
    assert token != "INVALID" or None


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_token,repository_name",
    # Enable the case below to check using a user token
    # [("REDACTED","GatorCogitate/cogitate_tool")],
    [(data_collection.retrieve_travis_token(), "GatorCogitate/cogitate_tool")],
)
def test_authenticate_repository_authenticates(input_token, repository_name):
    """Test to ensure the validity of the travis token."""
    assert (
        data_collection.authenticate_repository(input_token, repository_name)
        != "INVALID"
    )


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_token,repository_name,state,contributor_data",
    [
        (
            data_collection.retrieve_travis_token(),
            "GatorCogitate/cogitate_tool",
            "all",
            json_handler.get_dict_from_json_file("contributor_data_template"),
        )
    ],
)
def test_retrieve_issue_data_retrieves_issues(
    # pylint: disable=bad-continuation
    input_token, repository_name, state, contributor_data
):
    """Test to ensure all issues are associated with the correct contributor."""
    ghub = Github(input_token)
    repository = ghub.get_repo(repository_name)

    contributor_data = data_collection.retrieve_issue_data(
        repository, state, contributor_data
    )

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
