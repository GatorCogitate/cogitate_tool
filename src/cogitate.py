""" Command Line Interface for interacting with Github repository info. """
# from data_collection import collect_commits
# from web_interface import team_visuals
# from web_interface import individual_visuals
from driller import find_repositories
from pprint import pprint
import argparse
import re


def main():
    """Execute the CLI."""

    args = retrieve_arguments()

    # Currently only validates the PyGithub repository
    repository = data_miner.authenticate_repository(args["token"], args["repo"])

    # Temporary structure given issue retrieval is the only function
    contributor_data = data_miner.initialize_contributor_data(
        "contributor_data_template"
    )
    contributor_data = data_miner.retrieve_issue_data(
        repository, args["state"], contributor_data
    )

    # Intermediate between data_miner and data_processor
    json_handler.write_dict_to_json_file(contributor_data, "contributor_data")

    # ask the user where they want view the data; command-line or web-interface
    print("If you want to view this data on the web, click the following link")
    print("'link to web-interface'")


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
    args = vars(a_parse.parse_args())

    pprint(find_repositories(args["link"]))

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
