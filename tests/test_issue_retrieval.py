"""Contains the test cases for issue_retrieval.py"""

import os
import sys
from github import Github

# __init__.py requires correction and does not add module folders to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")

# pylint: disable=import-error
# pylint: disable=wrong-import-position
from src import issue_retrieval
from json_interaction import json_handler

# As of the current state, these tests require a token to function
#
# This requirement will be amended within the week after successful team
# collaboration provided an alternative test procedure is possible
#
# Remove your token from this file after demonstration
TOKEN = "REDACTED"
REPOSITORY_NAME = "GatorCogitate/cogitate_tool"
CONTRIBUTOR_DATA = json_handler.get_dict_from_json_file("contributor_data_template")


def test_retrieve_issue_data_retrieves_issues():
    """Test to ensure all issues are associated with the correct contributor"""

    # Refer to concerns above regarding future development
    # pylint: disable=global-statement
    global TOKEN
    global REPOSITORY_NAME
    global CONTRIBUTOR_DATA
    ghub = Github(TOKEN)
    repository = ghub.get_repo(REPOSITORY_NAME)
    issues = repository.get_issues(state="all")

    CONTRIBUTOR_DATA = issue_retrieval.retrieve_issue_data(issues, CONTRIBUTOR_DATA)

    contributor_found = False

    for username in CONTRIBUTOR_DATA:

        for issue_id in CONTRIBUTOR_DATA[username]["issues_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            assert repository.get_issue(number=issue_id).user.login == username

        for issue_id in CONTRIBUTOR_DATA[username]["issues_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True

        for issue_id in CONTRIBUTOR_DATA[username]["pull_requests_opened"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            assert repository.get_issue(number=issue_id).user.login == username

        for issue_id in CONTRIBUTOR_DATA[username]["pull_requests_commented"]:
            assert repository.get_issue(number=issue_id).pull_request is not None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issue_id).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True
