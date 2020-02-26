"""Count the number of lines changed by an indvividual."""

# from git import Repo
from pydriller import RepositoryMining

# from pydriller.domain.commit import ModificationType


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
        if "noreply.github.com" in dictionary[key]["EMAIL"]:
            # adds the key to issues list
            name_issues.append(key)
            # send email to parsing function
            new_name = parse_email(dictionary[key]["EMAIL"])
            if new_name in dictionary:
                print(new_name, " name to be merged with ", key)
                dictionary[new_name]["COMMITS"] += dictionary[key]["COMMITS"]
                dictionary[new_name]["ADDED"] += dictionary[key]["ADDED"]
                dictionary[new_name]["REMOVED"] += dictionary[key]["REMOVED"]
                dictionary[new_name]["TOTAL"] += dictionary[key]["TOTAL"]
                keys_to_delete.append(key)
            else:
                print(new_name, " not found in data")

    dictionary = delete_duplicates(dictionary, keys_to_delete)
    return dictionary


def get_commit_average(lines, commits):
    """Find average lines modified per commit."""
    # Loop through the dictionary and calculate the average lines per commits
    # formula for average: (added + deleted)/number_of_commits
    if commits != 0:
        average = lines / commits
        return (int)(average)
    return 0


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


def get_author_name(commit):
    """Accept a commit Pydriller object and retruns the name of its author."""
    return commit.author.name


def get_author_email(commit):
    """Accept a commit Pydriller object and retruns the email of its author."""
    return commit.author.email


def get_commit_date(commit):
    """Accept a commit Pydriller object and retruns the date it's commited."""
    return commit.committer_date


def get_added_lines(dictionary, key, file):
    """Accept dictionary, key and Pydriller file object. Returns a dictionary.

    that includes a key and the added lines.
    """
    if "ADDED" not in dictionary[key].keys():
        return {"ADDED": file.added}
    new_total = dictionary[key]["ADDED"] + file.added
    return {"ADDED": new_total}


def get_removed_lines(dictionary, key, file):
    """Accept dictionary, key, and Pydriller file object. Returns a dictionary.

    that includes a key and the removed lines.
    """
    if "REMOVED" not in dictionary[key].keys():
        return {"REMOVED": file.removed}
    new_total = dictionary[key]["REMOVED"] + file.removed
    return {"REMOVED": new_total}


def get_total_lines(dictionary, key, file):
    """Accept dictionary, key and Pydriller file object. Returns a dictionary.

    that includes a key and the total lines.
    """
    total_lines = file.added - file.removed
    if "TOTAL" not in dictionary[key].keys():
        return {"TOTAL": total_lines}
    new_total = dictionary[key]["TOTAL"] + total_lines
    return {"TOTAL": new_total}


def get_modified_lines(dictionary, key, file):
    """Accept dictionary, key and Pydriller file object. Returns a dictionary.

    that includes a key and the modified lines.
    """
    total_lines = file.added + file.removed
    if "MODIFIED" not in dictionary[key].keys():
        return {"MODIFIED": total_lines}
    new_total = dictionary[key]["MODIFIED"] + total_lines
    return {"MODIFIED": new_total}


def get_commit_data(repo_path):
    """Create a dictionary of retreived data from the repository."""
    # creates a hashmap where the key is the authors username
    data_list = {}
    # goes through all the commits in the current branch of the repo
    for commit in RepositoryMining(repo_path).traverse_commits():
        author = get_author_name(commit)
        email = get_author_email(commit)
        date = get_commit_date(commit)
        # check if the key already in in the dicitionary
        if author in data_list:
            # condition passed, adds one to the number of commits
            data_list[author]["COMMITS"] += 1
        else:
            # condition fails, creates a new key and adds empty data
            data_list[author] = {
                "EMAIL": email,
                "COMMITS": 1,
                "ADDED": 0,
                "REMOVED": 0,
                "TOTAL": 0,
                "MODIFIED": 0,
                "RATIO": 0,
                "FILES": [],
                "FORMAT": [],
                "COMMITDATE": [],
            }
        # goes through the files in the current commit
        for file in commit.modifications:
            # retreive data using Pydriller API
            current_file = file.filename
            # use getter methods to add to the existing dictionary
            data_list[author].update(get_added_lines(data_list, author, file))
            data_list[author].update(get_removed_lines(data_list, author, file))
            data_list[author].update(get_total_lines(data_list, author, file))
            data_list[author].update(get_modified_lines(data_list, author, file))
            # TODO iterate through the dates and add to table with .append
            # check if the explored file is not in the list in index seven
            if current_file not in data_list[author]["FILES"]:
                # the name of the file is appended to the list
                data_list[author]["FILES"].append(current_file)
    # iterate through the data to do final calculations
    for key in data_list:
        average = get_commit_average(
            data_list[key]["MODIFIED"], data_list[key]["COMMITS"]
        )
        data_list[key]["RATIO"] = average
        formats = get_file_formats(data_list[key]["FILES"])
        data_list[key]["FORMAT"] = formats
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


# NOTE: for printing the data please use the file print_table.py
