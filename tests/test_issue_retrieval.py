from src import issue_retrieval
from json_interaction import json_handler
from github import Github

# As of the current state, these tests require a token to function
#
# This requirement will be amended within the week after successful team
# collaboration provided an alternative test procedure is possible
#
# Remove your token from this file after demonstration
token = "9fd3989585322606a5107412bb9c2ffa82ad25ee"
repository_name = "GatorCogitate/cogitate_tool"
contributor_data = json_handler.get_dict_from_json_file("contributor_data")


def test_retrieve_issue_data_retrieves_issues():
    """Test to ensure all issues are associated with the correct contributor"""

    # Refer to concerns above regarding future development
    global token
    global repository
    global contributor_data
    ghub = Github(token)
    repository = ghub.get_repo(repository_name)
    issues = repository.get_issues(state="all")

    contributor_data = issue_retrieval.retrieve_issue_data(issues, contributor_data)

    contributor_found = False

    for username in contributor_data:

        for issueID in contributor_data[username]["issues_opened"]:
            assert repository.get_issue(number=issueID).pull_request == None
            assert repository.get_issue(number=issueID).user.login == username

        for issueID in contributor_data[username]["issues_commented"]:
            assert repository.get_issue(number=issueID).pull_request == None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issueID).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True

        for issueID in contributor_data[username]["pull_requests_opened"]:
            assert repository.get_issue(number=issueID).pull_request != None
            assert repository.get_issue(number=issueID).user.login == username

        for issueID in contributor_data[username]["pull_requests_commented"]:
            assert repository.get_issue(number=issueID).pull_request != None
            contributor_found = False
            while contributor_found is False:
                for comment in repository.get_issue(number=issueID).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True
