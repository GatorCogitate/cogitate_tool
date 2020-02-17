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
for commit in allcommits:
    print(commit.author)


def get_repo_commits():
    """ """
    path = input("Enter the path to the repo : ")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " added to {}".format(m.filename),
                "lines of code {}".format(m.added),
            )

    print("")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " removed from {}".format(m.filename),
                "lines of code {}".format(m.removed),
            )


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    # get_repo_list()
    repoIndex = int(input("Please enter an index number to show information:"))
    # print(get_repo_info(repoIndex))

    get_repo_commits()


choice = input("call main? (y = yes/ n = no)")
if choice == "y":
    main_method()
