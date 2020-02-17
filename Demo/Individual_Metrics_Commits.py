"""FastAPI Demo designed to accept user credentials and display GitHub info."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI

# First create a Github instance using an access token

user_token = input("Enter User Token: ")
user = Github(user_token)
print(user.get_user().login)
username = user.get_user().login
repo = user.get_repo("GatorCogitate/cogitate_tool")
allcommits = repo.get_commits()
all_branches = repo.get_branches()
for branch in all_branches:
    print(branch)
    all_commits = repo.get_commits()
    for commit in all_commits:
        print(commit.commit.author)
        print("")
        print("")


def get_repo_commits():
    """Function to get repository commits information."""
    path = input("Enter the path to the repo : ")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " added to {}".format(m.filename),
            )

    print("")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " removed from {}".format(m.filename),
            )


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    # get_repo_list()
    repoIndex = int(input("Please enter an index number to show information:"))
    # print(get_repo_info(repoIndex))

    get_repo_commits()


main_method()
