"""Command Line Interface for the Cogitate tool."""
# from data_collection import collect_commits
# from web_interface import web_interface
from driller import find_repositories
from pprint import pprint
import data_collection
import json_handler
import argparse
import re


def main():
    """Execute the CLI."""
    args = retrieve_arguments()

    # Currently only validates the PyGithub repository
    repository = data_collection.authenticate_repository(args["token"], args["repo"])

    # Temporary structure given issue retrieval is the only function
    contributor_data = data_collection.initialize_contributor_data(
        "contributor_data_template"
    )
    contributor_data = data_collection.retrieve_issue_data(
        repository, args["state"], contributor_data
    )
    commit_list = data_collection.collect_commits_hash(args["link"])
    pprint(commit_list)
    # Intermediate between data_miner and data_processor
    json_handler.write_dict_to_json_file(contributor_data, "contributor_data")
    # gives the user the option to use  the web interface
    to_web = True
    while to_web == True:
        to_webinterface = input("Would you like to view the data on the web?(y/n)")
        # print(web_interface.web_interface())


def retrieve_arguments():
    """Retrieve the user arguments and return the args dictionary."""
    # As no other functions exist in master as of this pull request, the args
    # below are written to accomadate issual retrieval in data_collection.py

    a_parse = argparse.ArgumentParser()
    a_parse.add_argument("-l", "--link", help="Cogitate a repo by the url of the repo")
    a_parse.add_argument(
        "-t", "--token", required=True, type=str, help="Github User Token"
    )
    a_parse.add_argument(
        "-r", "--repo", required=True, type=str, help="User's Repository"
    )
    a_parse.add_argument(
        "-s", "--state", required=True, type=str, help="State of the Issue"
    )

    args = vars(a_parse.parse_args())

    # pprint(find_repositories(args["link"]))

    return args


def team():
    """calls all team-based funtions"""
    pass


def individual():
    """calls all individual functions"""
    pass


def link_validator(url_str):
    """Validates if an url is a real link"""
    url_pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    if re.match(regex, url_str) is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
