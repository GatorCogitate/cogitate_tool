"""Demo designed to find and store information about PyGithub."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI


def output_hash_map(dictionary):
    """Method to print out the hash map."""
    # print headings
    print("Branch", "\t Author", "\t Time", "\t Files", "\t Message")
    # prints hashmap content
    # for key in dictionary:


    for key, _ in dictionary.items():
        print(key)
        for item in dictionary[key]:
            # print("\t" + str(item))
            print("\t" + str(item) + "\t")

def get_repo_commits_py_github():
    """Method to get commit information using pygithub"""
    user_token = input("Enter User Token: ")
    user = Github(user_token)
    print(user.get_user().login)
    username = user.get_user().login
    repo = user.get_repo("GatorCogitate/cogitate_tool")
    allcommits = repo.get_commits()
    all_branches = repo.get_branches()

    branches = {}

    for branch in all_branches:
        # Create hash map.
        data_list = list()
        all_commits = repo.get_commits()
        all_comments = repo.get_comments()
        print(branch)
        for commit in all_commits:
            # commit_info = ()
            commit_info = (
                branch.name,
                commit.commit.author,
                commit.commit.author.date,
                commit.files,
                commit.commit.message,
            )
            data_list.append(commit_info)

        branches[branch.name] = data_list
    return branches


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    dictionary = get_repo_commits_py_github()

    output_hash_map(dictionary)


main_method()
