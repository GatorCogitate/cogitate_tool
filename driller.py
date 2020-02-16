from git import Repo
from pydriller import RepositoryMining

# method to receive a URL from user
print("Please enter the URL of your terminal:\n")
repo = input()
miner = RepositoryMining(path_to_repo=repo)
# method to use user-given URL to list branches
