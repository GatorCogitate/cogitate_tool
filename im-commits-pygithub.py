"""Demo designed to find and store information about PyGithub."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI


def output_hash_map():
    """Method to print out the hash map."""


def get_repo_commits_py_github():
    """Method to get commit information using pygithub"""
    user_token = input("Enter User Token: ")
    user = Github(user_token)
    print(user.get_user().login)
    username = user.get_user().login
    repo = user.get_repo("GatorCogitate/cogitate_tool")
    allcommits = repo.get_commits()
    all_branches = repo.get_branches()

    for branch in all_branches:
        # Create hash map.
        data_list = {}
        all_commits = repo.get_commits()
        all_comments = repo.get_comments()
        print(branch)

        for commit in all_commits:
            print(commit.commit.author)
            print(commit.commit.author.date)
            print(commit.files)
            print(commit.commit.message)
            print("")

            data_list[commit] = [
                branch.name,
                commit.commit.author,
                commit.commit.author.date,
                commit.files,
                commit.commit.message,
            ]

            data_list[commit][0] += branch.name
            data_list[commit][1] += commit.commit.author
            data_list[commit][2] += commit.commit.author.date
            data_list[commit][3] += commit.files
            data_list[commit][4] += commit.commit.message

    return data_list


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    get_repo_commits_py_github()
    print(data_list)


main_method()
