"""Demo designed to find and store information about PyGithub."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI


def get_repo_commits_py_github():
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
        all_comments = repo.get_comments()
        for commit in all_commits:
            print(commit.commit.author)
            print(commit.commit.author.date)
            print(commit.files)
            print(commit.commit.message)
            print("")
            print("")


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    get_repo_commits_py_github()
    get_repo_commits_py_driller()


main_method()
