"""Contains the test case(s) for retrieve_issue_data in data_miner."""

import pytest
from github import Github

# TODO linter issue: data_miner is not in src folder
from src import data_miner
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

    ghub = Github(input_token)
    repository = ghub.get_repo(repository_name)

    contributor_data = data_miner.retrieve_issue_data(
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
