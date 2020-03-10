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
    "input_file",
    ["data/token.txt"],
)
def test_retrieve_token_with_tokenfile(input_file):
    """Test to ensure the retrieval of the user token."""
    try:
        # Arbitrary Check
        file = open(input_file).read()
        file = "BLANK"
    except FileNotFoundError:
        pytest.skip()

    assert data_collection.retrieve_token("data/token.txt") != None


@pytest.mark.parametrize(
    "input_token,repository_name",
    [(data_collection.retrieve_token("data/token.txt"), "GatorCogitate/cogitate_tool")],
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
            data_collection.retrieve_token("data/token.txt"),
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

    # Sets default status to false.

    contributor_found = False

    # Iterates through contributers in a repository.
    for username in contributor_data:
        # Iterates through issues a user has opened. Asserts that it is associating
        # with the correct user by checking username against username data stored
        # in the issue.
        for issue_id in contributor_data[username]["issues_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            assert repository.get_issue(number=issue_id).user.login == username

        # Iterates through how many issues a user has commented on, does not count
        # individual comments.
        for issue_id in contributor_data[username]["issues_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            # Unnecessary declaration but doesn't hurt anything.
            contributor_found = False
            # Iterates through comments in a particular issue, until it finds
            # the username it is searching for, in which case it breaks.
            # Has the potential to run forever but this is unlikely.
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True

        # Iterates through pull requets opened by a user.
        # Checks that user hsa opened at least one, and that the username is stored
        # the same in the pull request data is the user being checked.
        for issue_id in contributor_data[username]["pull_requests_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            assert repository.get_issue(number=issue_id).user.login == username

        # Checks how many comments a username has on a pull request.
        for issue_id in contributor_data[username]["pull_requests_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            contributor_found = False
            # Loops until it finds at least a comment by the username.
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True
