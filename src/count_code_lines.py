from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType


def print_in_table(dictionary):
    # print headings
    print("Username", "\t +", "\t -", "\t Total")
    # prints hashmap content
    for key in dictionary:
        print(key, "\t", dictionary[key][0], "\t", dictionary[key][1], "\t", dictionary[key][2],)

data_list = {}
def get_commit_lines(repo_path):
    # creates a hashmap where the key is the authors username
    # goes through all the commits in the current branch of the repo
    for commit in RepositoryMining(repo_path).traverse_commits():
        author = commit.author.name
        # goes through the files in the current commit
        for m in commit.modifications:
            added_lines = m.added
            removed_lines = m.removed
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
path = input("Enter the path to the repo : ")
data = get_commit_lines(path)
print_in_table(data)
