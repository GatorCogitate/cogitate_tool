"""Program to count the number of lines added and deleted by an indvividual"""

# from git import Repo
from pydriller import RepositoryMining

# from pydriller.domain.commit import ModificationType


def print_in_table(dictionary):
    """Create the table"""
    # print headings
    print("Username", "\t +", "\t -", "\t Total")
    # prints hashmap content
    for key in dictionary:
        print(
            key,
            "\t",
            dictionary[key][0],
            "\t",
            dictionary[key][1],
            "\t",
            dictionary[key][2],
        )


def get_commit_lines(repo_path):
    """method to obtain the number of lines that were added or deleted"""
    data_list = {}
    # creates a hashmap where the key is the authors username
    # goes through all the commits in the current branch of the repo
    for commit in RepositoryMining(repo_path).traverse_commits():
        author = commit.author.name
        # goes through the files in the current commit
        for file in commit.modifications:
            added_lines = file.added
            removed_lines = file.removed
            total_lines = added_lines - removed_lines
            # checks if the author is already in the list
            if author in data_list:
                # adds the current information to the existing ones
                data_list[author][0] += added_lines
                data_list[author][1] += removed_lines
                data_list[author][2] += total_lines
            else:
                # creates a new kay and add the data
                data_list[author] = [added_lines, removed_lines, total_lines]
    return data_list


# takes input for the repository local path OR URL
PATH_REPO = input("Enter the path to the repo : ")
DATA_LINES = get_commit_lines(PATH_REPO)
print_in_table(DATA_LINES)
