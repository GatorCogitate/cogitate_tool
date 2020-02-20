""" Uses Pydriller to extract information from Github."""
from git import Repo
from pydriller import RepositoryMining


def find_repositories(repo):
    """ Locates a Github repository with the URL provided by the user. """
    # ask the user for a URL of a Github repository
    miner = RepositoryMining(path_to_repo=repo)
    return miner
