''' Uses Pydriller to extract information from Github.'''
from git import Repo
from pydriller import RepositoryMining

def find_repositories():
    ''' Recieves a URL from the user to locate a Github repository. '''
    print("Please enter the URL of your terminal:")
    repo = input()
    # use URL input as parameter for RepositoryMining
    miner = RepositoryMining(path_to_repo=repo)
