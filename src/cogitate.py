"""Command Line Interface for interacting with Github repository info."""
# from data_collection import collect_commits
import argparse
from pprint import pprint
from src import json_handler
from src import data_collection
from driller import find_repositories


def main():
    """Execute the Command Line Interface."""
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

    # Intermediate between data_miner and data_processor
    json_handler.write_dict_to_json_file(contributor_data, "contributor_data")


def retrieve_arguments():
    """Retrieve the user arguments and return the args dictionary."""
    # As no other functions exist in master as of this pull request, the args
    # below are written to accomadate issual retrieval in data_miner.py

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
    a_parse.add_argument("-u", "--update", required=True, help="Update Cogitate data")
    args = vars(a_parse.parse_args())

    pprint(find_repositories(args["link"]))

    return args


def team():
    """Call all team-based funtions."""


def individual():
    """Call all individual functions."""


if __name__ == "__main__":
    main()
