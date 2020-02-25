"""Checks that the compute_tf_monolith.py produces the expected output."""

from pydriller import RepositoryMining, GitRepository  # import necessary libraries

import shlex
import subprocess
import sys


def get_repo_authors(user_repo):
    """Accesses the remote repo and puts author names in a list."""

    # accesses users
    commit_author_list = []
    # accesses github repo to calculate users commits
    for commit in RepositoryMining(user_repo).traverse_commits():
        if commit.author.name not in commit_author_list:
            commit_author_list.append(commit.author.name)
            print("Adding author,", commit.author.name)
        else:
            pass

    print("-- Repo Authors:")
    for author_name in commit_author_list:
        print(author_name)

    return commit_author_list


def single_multi_author_choice(commit_author_list):
    """Offers user the choice of looking at all or one specific author(s)."""

    user_author_choice = int(
        input(
            "-- Would you like to look at (1) all authors or a (2) specific author?: "
        )
    )
    if user_author_choice == 1:
        pass
    elif user_author_choice == 2:
        # Looks for specific author contributions
        specific_author = input("-- Enter author name:")
        if specific_author in commit_author_list:
            commit_author_list = [specific_author]
    else:
        print("Invalid choice!")

    return commit_author_list

if __name__ == "__main__":
    user_repo = input("Specify your local repo: ")
    #user_repo = "~/cs203s2020/labs/cogitate_tool"
    authors = get_repo_authors(user_repo)
    commit_author_list = single_multi_author_choice(authors)
    # assume that all of the checks run correctly and prove otherwise
    exit_code = 0
    # defines the command that will call the check_compute_tf_monolith.py
    for author in commit_author_list:
        print("AUTHOR", author)
        author_name = author
        base_command = 'dml gstats authorchurnmeta --author '
        quote = '"'
        command = base_command + quote + author_name + quote
        try:
            # tokenize this command so that subprocess can accept each of its parts
            tokenized_command = shlex.split(command)
            print("Tokenized command to execute: " + str(tokenized_command))
            print()
            # run the tokenized command and display the output as a byte string
            result = subprocess.run(tokenized_command, stdout=subprocess.PIPE, check=True)
            # Display the standard output variable inside of the result from the subprocess
            # decode the byte string using UTF-8
            decoded_stdout = str(result.stdout.decode("utf-8"))
            print("Decoded output of executed command: \n" + decoded_stdout)
        except:
            print("Invalid author")
