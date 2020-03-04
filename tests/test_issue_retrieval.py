"""
Contains the test case(s) for retrieve_issue_data in data_miner.

The test case will take the current repository.

Unless that path variable is changed.
"""

import pytest
from github import Github
from src import data_collection
from src import json_handler

# As of the current state, this test requires a token to function
#
# This requirement should be amended within the week after successful team
# collaboration provides a Travis Environment Variable

# Below marked as xfail due to token absence; passes with token


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_token,repository_name,state,contributor_data",
    [
        (
            "REDACTED",
            "GatorCogitate/cogitate_tool",
            "all",
            json_handler.get_dict_from_json_file("contributor_data_template"),
        )
    ],
)
def test_retrieve_issue_data_retrieves_issues(
    input_token, repository_name, state, contributor_data
):
    """Test to ensure all issues are associated with the correct contributor"""
    # PyGithub Object creation.
    ghub = Github(input_token)
    repository = ghub.get_repo(repository_name)

    contributor_data = data_miner.retrieve_issue_data(
        repository, state, contributor_data
    )
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
