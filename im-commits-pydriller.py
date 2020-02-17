"""Demo designed to show information about Github repositories using PyDriller."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI


def get_repo_commits_py_driller():
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

    get_repo_commits_py_driller()


main_method()
