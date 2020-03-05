""" Gather data nad write it to JSON file.
Collects commit data for contributors of the master branch of a repo, then
writes it to the raw_repository_data.json."""

import json
import os
from pydriller import RepositoryMining
from github import Github


def get_dict_from_json_file(json_name, data_path="./data/"):
    """Populate and return a dictionary of all the data in a specified json file.
    Arguments:
    - json_file_name: The name of the file to open.
    - data_path: Default/optional argument that stores the relative path
      to the directory containing the file.
    """

    with open(os.path.join(data_path, json_name + ".json"), "r") as json_file:
        # In the open() function, "r" specifies read-only access
        user_data_dict = json.load(json_file)
        # json.load() converts a json file into a python dictionary
    return user_data_dict


def write_dict_to_json_file(user_data_dict, file_name ="raw_repository_data", data_path="./data/"):
    """Overwrite specified json file with data from a given dictionary.

    Arguments:
    -- user_data_dict: Raw repository data to be written to json file.
    -- additional_name: Enables the user to label the json
         file with the repository, or date that data has been collected, or
         other specification. Additional name preferably entered
         with a "_" to maintain file naming convention(optional)
    -- data_path: Argument that stores the relative path
         to the directory containing the file. (optional)
    """
    with open(os.path.join(data_path, file_name + ".json"), "w") as json_file:
        # In the open() function, "w" specifies write access
        json.dump(user_data_dict, json_file, indent=4)
        # json.dump() converts a dictionary into a json-formatted string.
        # Specifying an indent does not alter the data itself, it only
        # increases readability in the json file.


def add_user_to_users_dictionary(user_data_dict, to_add):
    """Append data to the users dictionary."""
    user_data_dict.update(to_add)


def authenticate_repository(user_token, repository_name):
    """Authenticate the Github repository using provided credentials."""

    # Credentials for PyGithub functions and methods
    ghub = Github(user_token)
    repository = ghub.get_repo(repository_name)

    return repository


def retrieve_issue_data(repository, state, contributor_data):
    """Retrieve contributor's involvement based upon issues and pull request threads."""

    issues = repository.get_issues(state=state)

    for issue in issues:
        for comment in issue.get_comments():
            if comment.user.login in contributor_data.keys():
                if issue.pull_request is None:
                    contributor_data[comment.user.login][
                        "issues_commented"
                    ].append(issue.number)
                else:
                    contributor_data[comment.user.login][
                        "pull_requests_commented"
                    ].append(issue.number)
        if issue.user.login in contributor_data.keys():
            if issue.pull_request is None:
                contributor_data[issue.user.login]["issues_opened"].append(
                    issue.number
                )
            else:
                contributor_data[issue.user.login]["pull_requests_opened"].append(
                    issue.number
                )

    return contributor_data


def collect_commits_hash(repo):
    """
    Creates a list of dictionaries that contains commit info.

    hash (str): hash of the commit
    msg (str): commit message
    author_name (str): commit author name
    author_email (str): commit author email
    author_date (datetime): authored date
    merge (Bool): True if the commit is a merge commit
    added: number of lines added
    removed: number of lines removed
    nloc: Lines Of Code (LOC) of the file
    complexity: Cyclomatic Complexity of the file
    methods: list of methods of the file.
    filename: files modified by commit.
    filepath: filepaths of files modified by commit.
    """

    commit_list = []

    for commit in RepositoryMining(repo).traverse_commits():

        line_added = 0
        line_removed = 0
        line_of_code = 0
        complexity = 0
        methods = []
        filename = []
        filepath = []

        for item in commit.modifications:
            # modifications is a list of files and its changes
            line_added += item.added
            line_removed += item.removed
            if item.nloc is not None:
                line_of_code += item.nloc
            if item.complexity is not None:
                complexity += item.complexity

            for method in item.methods:
                methods.append(method.name)
            filename.append(item.filename)
            filepath.append(item.new_path)

        single_commit_dict = {
            "hash": commit.hash,
            "author_msg": commit.msg,
            "author_name": commit.author.name,
            "author_email": commit.author.email,
            "author_date": str(commit.author_date.date()),
            "merge": commit.merge,
            "line_added": line_added,
            "line_removed": line_removed,
            "lines_of_code": line_of_code,
            "complexity": complexity,
            "methods": methods,
            "filename": filename,
            "filepath": filepath,
        }

        commit_list.append(single_commit_dict)

    return commit_list
