""" Command Line Interface for interacting with Github repository info. """
# from data_collection import collect_commits
from driller import find_repositories
from pprint import pprint
import argparse


def team():
    """calls all team-based funtions"""
    pass


def individual():
    """calls all individual functions"""
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--link", help="Cogitate a\
     repo by the url of the repo.")
    args = parser.parse_args()
    pprint(find_repositories(args.link))
