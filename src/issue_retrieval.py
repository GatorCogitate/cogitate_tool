# Use the following command for demonstration purposes:
# python src/issue_retrieval.py --repo "REPO HERE" --state "STATE HERE" --token "TOKEN HERE"

import os
import sys

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)) + "/../")

import argparse
from json_interaction import json_handler
from github import Github


def main():
    """Retrieve contributor list and populate conversation fields."""

    # Argument retrieval
    args = retrieve_arguments()

    # Github data retrieval
    ghub = Github(args["token"])
    repository = ghub.get_repo(args["repo"])
    issues = repository.get_issues(state = args["state"])

    # Data structure setup
    contributor_data = json_handler.get_dict_from_json_file("contributor_data")

    # Data collection
    contributor_data = retrieve_issue_data(issues, contributor_data)

    # Data submission
    json_handler.write_dict_to_json_file(contributor_data, "demo_data")


def retrieve_arguments():
    """Retrieve the arguments based upon the format listed in this file."""

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--token", required = True, type = str, help = "Github User Token")
    ap.add_argument("-r", "--repo", required = True, type = str, help = "User's Repository")
    ap.add_argument("-s", "--state", required = True, type = str, help = "State of the Issue")
    args = vars(ap.parse_args())
    return args


def retrieve_issue_data(issues, contributor_data):
    """Retrieve a contributor's involvement based upon issues and pull request threads."""

    for issue in issues:
        for comment in issue.get_comments():
            if comment.user.login in contributor_data.keys():
                if (issue.pull_request == None):
                    contributor_data[comment.user.login]["issues_commented"].append(issue.number)
                else:
                    contributor_data[comment.user.login]["pull_requests_commented"].append(issue.number)
        if issue.user.login in contributor_data.keys():
            if (issue.pull_request == None):
                contributor_data[issue.user.login]["issues_opened"].append(issue.number)
            else:
                contributor_data[issue.user.login]["pull_requests_opened"].append(issue.number)

    return contributor_data


if __name__ == "__main__":
    main()
