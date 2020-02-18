from git import Repo
from pydriller import RepositoryMining

# method to receive a URL from user
print("Please enter the URL of your terminal:")
repo = input()
# use URL input as parameter for RepositoryMining
miner = RepositoryMining(path_to_repo=repo)
