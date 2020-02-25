"""Count the number of lines changed by an indvividual."""

# from git import Repo
from pydriller import RepositoryMining
a
# from pydriller.domain.commit import ModificationType

# Keys for the dicitionary indeces
EMAILS = 0
COMMITS = 1
ADDED = 2
REMOVED = 3
TOTAL = 4
MODIFIED = 5
RATIO = 6
FILES = 7
FORMAT = 8
DATES = 9


# TODO go over this function
def delete_duplicates(data, keys_to_delete):
    """Delete keys from dictionary, keys are sent in a list."""
    dictionary = data
    for key in keys_to_delete:
        print(dictionary[key], " will be removed")
        del dictionary[key]
        print(key in dictionary)
    return dictionary


# TODO go over this function
def parse_email(email):
    """Locate @ and + sign in email and returns the string between them."""
    # find the index of @ sign
    plus_index = email.find("+")
    # find the index of + sign
    at_index = email.find("@")
    # slices string accordingly
    revised_email = email[(plus_index + 1) : at_index]
    return revised_email


# NOTE: there are issues with this function, calls have been commented out
# TODO go over this function
def check_emails(data):
    """Remove @github email from users and merges data with duplicates."""
    dictionary = data
    # list intended to gather keys with issues
    name_issues = []
    # gather keys that have issues and duplicates in dictionary
    keys_to_delete = []
    # loop through the data and add keys that have @github email to name_issues
    for key in dictionary:
        # checks if the email is a github email
        if "noreply.github.com" in dictionary[key][EMAILS]:
            # adds the key to issues list
            name_issues.append(key)
            # send email to parsing function
            new_name = parse_email(dictionary[key][EMAILS])
            if new_name in dictionary:
                print(new_name, " name to be merged with ", key)
                dictionary[new_name][COMMITS] += dictionary[key][COMMITS]
                dictionary[new_name][ADDED] += dictionary[key][ADDED]
                dictionary[new_name][REMOVED] += dictionary[key][REMOVED]
                dictionary[new_name][TOTAL] += dictionary[key][TOTAL]
                keys_to_delete.append(key)
            else:
                print(new_name, " not found in data")

    dictionary = delete_duplicates(dictionary, keys_to_delete)
    return dictionary


def get_commit_average(lines, commits):
    """Find average lines modified per commit."""
    # Loop through the dictionary and calculate the average lines per commits
    # formula for average: (added + deleted)/number_of_commits
    average = lines / commits
    return (int)(average)


def parse_for_type(name):
    """Parse through file name and returns its format."""
    if "." in name:
        dot_index = name.find(".")
        return name[dot_index:]
    return name


def get_file_formats(files):
    """Create a list of unique file formats."""
    formats = []
    for file in files:
        current_format = parse_for_type(file)
        if current_format not in formats:
            formats.append(current_format)
    return formats


def get_commit_data(repo_path):
    """Create a dictionary of retreived data from the repository."""
    # creates a hashmap where the key is the authors username
    data_list = {}
    # goes through all the commits in the current branch of the repo
    for commit in RepositoryMining(repo_path).traverse_commits():
        author = commit.author.name
        email = commit.author.email
        date = commit.author_date
        # check if the key already in in the dicitionary
        if author in data_list:
            # condition passed, adds one to the number of commits
            data_list[author][COMMITS] += 1
        else:
            # condition fails, creates a new key and adds empty data
            data_list[author] = [email, 1, 0, 0, 0, 0, 0, [], []]
        # goes through the files in the current commit
        for file in commit.modifications:
            # retreive data using Pydriller API
            added_lines = file.added
            removed_lines = file.removed
            current_file = file.filename
            # calculate total lines from previously retreived data
            total_lines = added_lines - removed_lines
            # calculate modified lines by combining added and removed
            modified_lines = added_lines + removed_lines
            # add retreived data to existing key
            data_list[author][ADDED] += added_lines
            data_list[author][REMOVED] += removed_lines
            data_list[author][TOTAL] += total_lines
            data_list[author][MODIFIED] += modified_lines
            data_list[author][DATES] += date
            # check if the explored file is not in the list in index seven
            if current_file not in data_list[author][FILES]:
                # the name of the file is appended to the list
                data_list[author][FILES].append(current_file)
    # iterate throug the data to do final calculations
    for key in data_list:
        average = get_commit_average(
            data_list[key][MODIFIED],
            data_list[key][COMMITS]
            )
        data_list[key][RATIO] = average
        formats = get_file_formats(data_list[key][FILES])
        data_list[key][FORMAT] = formats
    return data_list


# NOTE: this is a commented out method due to duplicative work

# def get_file_types(repo_path):
#     data_list = {}
#     change_file_type = []
#     author_name = []
#     author_email = []
#     comprehensive_list = []
#     dict = {}
#     for commit in RepositoryMining(repo_path).traverse_commits():
#         author = commit.author.name
#         for m in commit.modifications:
#             var = str(m.change_type.name)
#             var_test = "MODIFY"
#             if var in var_test:
#                 if author not in dict.keys():
#                     dict[author] = {}
#                 if var not in dict[author].keys():
#                     dict[author][var] = 1
#                 else:
#                     dict[author][var] += 1
#
#     print(dict)
#     return dict


# NOTE: for printing the data please use the file pint_table.py
