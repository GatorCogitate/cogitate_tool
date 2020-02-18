# Use the following command for demonstration purposes:
# python src_issue_retrieval/issue_retrieval.py --repo "REPO HERE" --state "STATE HERE" --token "TOKEN HERE"

import os
import sys

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)) + "/../")

import argparse
# This branch is currently experiencing issues with python path insertion, and
# json_demo cannot be accessed in the demo folder
# Please leave json_demo_alt under src until this is resolved
from demo import json_handler
from github import Github


def main():
    """Retrieve contributor list and populate conversation fields."""

    # Github data retrieval
    args = retrieve_arguments()
    ghub = authenticate_user(retrieve_user_token(args))
    repository = authenticate_repository(retrieve_repository_name(args), ghub)
    issues = retrieve_issues(retrieve_issue_status(args), repository)

    # Data structure setup
    contributor_database = retrieve_contributor_database("demofile")
    issues_contribution = link_contributors(contributor_database)
    pr_contribution = link_contributors(contributor_database)

    # Data collection
    issues_contribution = retrieve_issue_data(issues, issues_contribution)
    pr_contribution = retrieve_pr_data(issues, pr_contribution)

    # Data submission
    submit_contribution("issues", issues_contribution, contributor_database, "demofile_2")
    # If "demofile_2" is changed, this method call will also push the issue data
    # as it has already been written to contributor_database
    submit_contribution(
        "pull_requests", pr_contribution, contributor_database,"demofile_2"
        )


def retrieve_arguments():
    """Retrieve the arguments based upon the format listed in this file."""

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--token", required = True, help = "Github User Token")
    ap.add_argument("-r", "--repo", required = True, help = "User's Repository")
    ap.add_argument("-s", "--state", required = True, help = "State of the Issue")
    args = vars(ap.parse_args())
    return args


def retrieve_user_token(args):
    """Retrieve the Github user token from the arguments."""

    user_token = str(args["token"])
    return user_token


def authenticate_user(user_token):
    """Validate the Github User Token."""

    ghub = Github(user_token)
    return ghub


def retrieve_repository_name(args):
    """Retrieve the Github repository from the arguments."""

    repository_name = str(args["repo"])
    return repository_name


def authenticate_repository(repository_name, ghub):
    """Validate the Github Repository."""

    repository = ghub.get_repo(repository_name)
    return repository


def retrieve_issue_status(args):
    """Retrieve the type of issue to retrieve from the arguments."""

    issue_state = str(args["state"])
    return issue_state


def retrieve_issues(state, repository):
    """Retrieve the list of issues based on a specific issue status."""

    issues = repository.get_issues(state = state)
    return issues

def retrieve_issue_data(issues, issues_contribution):
    """Retrieve a contributor's involvement based upon messages in issues."""

    for issue in issues:
        # Only collect if the issue is not a pull request
        if (issue.pull_request == None):
            for comment in issue.get_comments():
                if comment.user.login in issues_contribution.keys():
                    issues_contribution[comment.user.login].append(issue.number)
            # We are counting the issuer of the issue as being involved in the conversation
            if issue.user.login in issues_contribution.keys():
                issues_contribution[issue.user.login].append(issue.number)

    return issues_contribution


def retrieve_pr_data(issues, pr_contribution):
    """Retrieve a contributor's involvement based upon messages in pull requests."""

    for issue in issues:
        # Only collect if the issue is a pull request
        if (issue.pull_request != None):
            for comment in issue.get_comments():
                if comment.user.login in pr_contribution.keys():
                    pr_contribution[comment.user.login].append(issue.number)
            # We are counting the issuer of the pr as being involved in the conversation
            if issue.user.login in pr_contribution.keys():
                pr_contribution[issue.user.login].append(issue.number)

    return pr_contribution


def retrieve_contributor_database(json_file_name):
    """Retrieve the .json containing a list of contributors"""

    contributor_database = json_handler.get_dict_from_json_file(json_file_name)
    return contributor_database


def link_contributors(contributor_database):
    """Populate a contribution list with contributors from the original database"""

    contribution_list = {}
    for username in contributor_database:
        contribution_list[username] = []
    return contribution_list


def submit_contribution(
    contribution_type, contribution_list, contributor_database, json_file_name
    ):
    """Submit the given contribution data to the .json"""

    for username in contributor_database:
        contributor_database[username][contribution_type] = contribution_list[username]

    json_handler.write_dict_to_json_file(contributor_database, json_file_name)


if __name__ == "__main__":
    main()
