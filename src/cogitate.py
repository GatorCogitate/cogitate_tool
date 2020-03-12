"""Command Line Interface for interacting with Github repository info."""

# from data_collection import collect_commits
import argparse

# from pprint import pprint

# from driller import find_repositories

from src import data_collection
from src import json_handler


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

    # Intermediate between data_collection and data_processor
    json_handler.write_dict_to_json_file(contributor_data, "contributor_data")


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
        "-r",
        "--repo",
        required=True,
        type=str,
        help="User's Repository name, start with root dirctory (user or organization name)",
    )
    a_parse.add_argument(
        "-rm",
        "--endmerge",
        required=True,
        type=str,
        help="Starts the process of merging usernames.",
    )
    a_parse.add_argument(
        "-b", "--below", required=True, type=float, help="Determines lower weight.",
    )
    a_parse.add_argument(
        "-a", "--above", required=True, type=float, help="Determines higher weight.",
    )
    a_parse.add_argument(
        "-wi",
        "--within",
        required=True,
        type=float,
        help="Determines value within weight.",
    )
    a_parse.add_argument(
        "-s",
        "--state",
        required=False,
        type=str,
        default="all",
        help="State of the Issue; open, closed, or all",
    )
    a_parse.add_argument(
        "-w",
        "--web",
        required=False,
        type=bool_validator,
        default=False,
        help="Whether to show the detailed result in web interface.",
    )
    a_parse.add_argument(
        "-m",
        "--metric",
        required=False,
        type=str,
        default="both",
        help="Invokes calculation of team or individual metrics. If not specified, both are run.",
    )

    args = vars(a_parse.parse_args())

    # pprint(find_repositories(args["link"]))

    return args


if __name__ == "__main__":
    main()
