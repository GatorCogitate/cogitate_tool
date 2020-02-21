"""Program to count the number of lines added and deleted by an indvividual."""

# from git import Repo
from pydriller import RepositoryMining
from prettytable import PrettyTable

# from pydriller.domain.commit import ModificationType


def print_in_table(dictionary):
    """Create and print the table using prettytable."""
    data_table = PrettyTable()
    # headings = ["Username", "Commits", "+", "-" "Total"]
    data_table.field_names = ["Username", "Commits", "+", "-", "Total"]
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key][0],
                dictionary[key][1],
                dictionary[key][2],
                dictionary[key][3],
            ]
        )
    print(data_table)


def get_commit_lines(repo_path):
    """Return the number of lines that were added or deleted\
    as a dictionary."""
    data_list = {}
    # creates a hashmap where the key is the authors username
    # goes through all the commits in the current branch of the repo
    for commit in RepositoryMining(repo_path).traverse_commits():
        author = commit.author.name
        if author in data_list:
            data_list[author][0] += 1
        else:
            # creates a new kay and add the data
            data_list[author] = [1, 0, 0, 0]
        # goes through the files in the current commit
        for file in commit.modifications:
            added_lines = file.added
            removed_lines = file.removed
            total_lines = added_lines - removed_lines
            data_list[author][1] += added_lines
            data_list[author][2] += removed_lines
            data_list[author][3] += total_lines
    return data_list


def main():
    """Call other functions in this module asking for user input."""
    # takes input for the repository local path OR URL
    path_repo = input("Enter the path to the repo : ")
    data_lines = get_commit_lines(path_repo)
    print_in_table(data_lines)


if __name__ == "__main__":
    main()
