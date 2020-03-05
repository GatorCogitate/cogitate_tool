"""Contains the test case(s) for retrieve_issue_data in data_to_json."""

import os
import pytest
from github import Github
from src import data_to_json


# As of the current state, this test requires a token to function


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_token,repository_name,state,contributor_data",
    [
        (
            os.environ.get("PYGITHUB_TOKEN"),
            "GatorCogitate/cogitate_tool",
            "all",
            data_to_json.get_dict_from_json_file("contributor_data_template"),
        )
    ],
)
def test_retrieve_issue_data_retrieves_issues(
    input_token, repository_name, state, contributor_data
):
    """Test to ensure all issues are associated with the correct contributor"""

    ghub = Github(input_token)
    repository = ghub.get_repo(repository_name)

    contributor_data = data_to_json.retrieve_issue_data(
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
