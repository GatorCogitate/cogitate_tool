from src_issue_retrieval import issue_retrieval
from github import Github

# As of the current state, these tests require a token to function
#
# This requirement will be amended within the week after successful team
# collaboration provided an alternative test procedure is possible
#
# Remove your token from this file after demonstration
temp_token = "REDACTED"
temp_repo = "GatorCogitate/cogitate_tool"
temp_contributors = {"stephensonc": [], "koscinskic": [], "schultzh": []}


def test_retrieve_issue_data_retrieves_issues():
    """Test to ensure all issues are associated with the correct contributor"""

    # Refer to concerns above regarding future development
    global temp_token
    global temp_repo
    global temp_contributors
    ghub = Github(temp_token)
    repo = ghub.get_repo(temp_repo)

    # Establishing test parameters
    issues = repo.get_issues()
    issues_contribution = {}
    for username in temp_contributors:
        issues_contribution[username] = []
    issues_contribution = issue_retrieval.retrieve_issue_data(issues, issues_contribution)

    contributor_found = False

    for username in issues_contribution:
        for issueID in issues_contribution[username]:
            # We are only checking for non-pr issues
            assert repo.get_issue(number = issueID).pull_request == None
            contributor_found = False
            # No need to search comments if the contributer issued the issue
            if repo.get_issue(number = issueID).user.login == username:
                contributor_found = True
            while contributor_found is False:
                for comment in repo.get_issue(number = issueID).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True


def test_retrieve_pr_data_retrieves_prs():
    """Test to ensure all pull requests are associated with the correct contributor"""

    # Refer to concerns above regarding future development
    global temp_token
    global temp_repo
    global temp_contributors
    ghub = Github(temp_token)
    repo = ghub.get_repo(temp_repo)

    # Establishing test parameters
    issues = repo.get_issues()
    pr_contribution = {}
    for username in temp_contributors:
        pr_contribution[username] = []
    pr_contribution = issue_retrieval.retrieve_pr_data(issues, pr_contribution)

    contributor_found = False

    for username in pr_contribution:
        for issueID in pr_contribution[username]:
            # We are only checking for pull requests
            assert repo.get_issue(number = issueID).pull_request != None
            contributor_found = False
            # No need to search comments if the contributer issued the pull request
            if repo.get_issue(number = issueID).user.login == username:
                contributor_found = True
            while contributor_found is False:
                for comment in repo.get_issue(number = issueID).get_comments():
                    if comment.user.login == username:
                        contributor_found = True
            assert contributor_found is True
