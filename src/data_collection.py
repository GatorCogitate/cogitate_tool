"""
Collects repository data for contributors of the master branch of a repo.

Writes the data to a .json file.

Calculates statistics based on the data from Github.
"""
from __future__ import division
import os
from pydriller import RepositoryMining
from prettytable import PrettyTable
from github import Github
import json_handler


def authenticate_repository(user_token, repository_name):
    """Authenticate the Github repository using provided credentials."""
    # Credentials for PyGithub functions and methods
    ghub = Github(user_token)
    repository = ghub.get_repo(repository_name)

    return repository


# Written as a temporary pass-through in case this variable is converted to a global
# variable, in which case that process would occur here. Pass-through will be eliminated
# during refactoring.
def initialize_contributor_data(file_path):
    """Load a dictionary based upon the given .json file."""
    contributor_data = json_handler.get_dict_from_json_file(file_path)

    return contributor_data


def retrieve_issue_data(repository, state, contributor_data):
    """Retrieve a contributor's involvement based upon issues and pull request threads."""
    issues = repository.get_issues(state=state)

    for issue in issues:
        for comment in issue.get_comments():
            if comment.user.login in contributor_data.keys():
                if issue.pull_request is None:
                    contributor_data[comment.user.login]["issues_commented"].append(
                        issue.number
                    )
                else:
                    contributor_data[comment.user.login][
                        "pull_requests_commented"
                    ].append(issue.number)
        if issue.user.login in contributor_data.keys():
            if issue.pull_request is None:
                contributor_data[issue.user.login]["issues_opened"].append(issue.number)
            else:
                contributor_data[issue.user.login]["pull_requests_opened"].append(
                    issue.number
                )

    return contributor_data


def collect_commits_hash(repo):
    """Create a list of dictionaries that contains commit info.

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
            # "author_date": commit.author_date,
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
        file_type, name = os.path.splitext(name)
        file_type += ""
        return name
    return name


def get_file_formats(files):
    """Create a list of unique file formats."""
    formats = []
    for file in files:
        current_format = parse_for_type(file)
        if current_format not in formats:
            formats.append(current_format)
    # sort data to ensure consistency for test
    formats = sorted(formats)
    return formats


# NOTE: this function is temporary to test get_individual_metrics considering
# there is not a main module that connects eerything yet
def add_raw_data_to_json(path_to_repo, json_file_name):
    """Check if raw data is in .json file and collects it if not."""
    # get the data from .json file
    current_data = json_handler.get_dict_from_json_file(json_file_name)
    # check if data has not been collected and do so if it was not
    if "RAW_DATA" not in current_data.keys():
        print("Raw data has not been collected, collecting it now...")
        # collects data from data_collection
        raw_data = {"RAW_DATA": collect_commits_hash(path_to_repo)}
        # Write raw data to .json file
        json_handler.add_entry(raw_data, json_file_name)
        print("Data collected")


def calculate_individual_metrics(json_file_name):
    """Retrieve the data from .json file and create a dictionary keyed by user."""
    current_data = json_handler.get_dict_from_json_file(json_file_name)
    # creates a hashmap where the key is the authors username
    data_dict = {}
    # Check if RAW_DATA is in json
    if "RAW_DATA" in current_data.keys():
        for key in current_data["RAW_DATA"]:
            author = key["author_name"]
            email = key["author_email"]
            # NOTE check date compatibility with json
            # date = "N/A"
            # check if the key already in in the dicitionary
            if author in data_dict:
                # condition passed, adds one to the number of commits
                data_dict[author]["COMMITS"] += 1
            else:
                # condition fails, creates a new key and adds empty data
                data_dict[author] = {
                    "EMAIL": email,
                    "COMMITS": 1,
                    "ADDED": 0,
                    "REMOVED": 0,
                    "TOTAL": 0,
                    "MODIFIED": 0,
                    "RATIO": 0,
                    "FILES": [],
                    "FORMAT": [],
                }

            data_dict[author]["ADDED"] += key["line_added"]
            data_dict[author]["REMOVED"] += key["line_removed"]
            # NOTE: consider adding lines of code from data
            # check if the explored file is not in the list in index seven
            current_files = key["filename"]
            # add the current_files to the user files list without duplicates
            data_dict[author]["FILES"] = list(
                set(data_dict[author]["FILES"]) | set(current_files)
            )
            # Sort list to ensure consistency when testing
            data_dict[author]["FILES"] = sorted(data_dict[author]["FILES"])
        # iterate through the data to do final calculations
        for key in data_dict:
            data_dict[key]["TOTAL"] = (
                data_dict[key]["ADDED"] - data_dict[key]["REMOVED"]
            )
            data_dict[key]["MODIFIED"] = (
                data_dict[key]["ADDED"] + data_dict[key]["REMOVED"]
            )
            average = get_commit_average(
                data_dict[key]["MODIFIED"], data_dict[key]["COMMITS"]
            )
            data_dict[key]["RATIO"] = average
            formats = get_file_formats(data_dict[key]["FILES"])
            data_dict[key]["FORMAT"] = formats
        # Reformat the dictionary as a value of the key INDIVIDUAL_METRICS
        indvividual_metrics_dict = {"INDIVIDUAL_METRICS": data_dict}
        return indvividual_metrics_dict
    return {}
    # NOTE: for printing the data please use the file print_table.py


def find_repositories(repo):
    """Locates a Github repository with the URL provided by the user."""
    # ask the user for a URL of a Github repository
    miner = RepositoryMining(path_to_repo=repo)
    return miner


def print_individual_in_table(file_name):
    """Create and print the table using prettytable."""
    data_table = PrettyTable()
    current_data = json_handler.get_dict_from_json_file(file_name)
    dictionary = current_data["INDIVIDUAL_METRICS"]
    headings = [
        "Username",
        "Email",
        "Commits",
        "+",
        "-",
        "Total",
        "Modified Lines",
        "Lines/Commit",
        "File Types",
    ]
    data_table.field_names = headings
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key]["EMAIL"],
                dictionary[key]["COMMITS"],
                dictionary[key]["ADDED"],
                dictionary[key]["REMOVED"],
                dictionary[key]["TOTAL"],
                dictionary[key]["MODIFIED"],
                dictionary[key]["RATIO"],
                dictionary[key]["FORMAT"],
            ]
        )

    print(data_table)


def get_testing_commit_info(json_file_name):
    """Get repo info about commits to or not to testing."""
    current_data = json_handler.get_dict_from_json_file(json_file_name)
    # creates a hashmap where the key is the authors username
    data_dict = {}
    # Check if RAW_DATA is in json
    if "RAW_DATA" in current_data.keys():
        for key in current_data["RAW_DATA"]:
            author = key["author_name"]
            filepaths = key["filepath"]  # get filepaths of file modified

            # NOTE check date compatibility with json
            # date = "N/A"
            # check if the key already in in the dicitionary
            if author in data_dict:
                # condition passed, adds one to the number of commits
                data_dict[author]["COMMITS"] += 1
            else:
                # condition fails, creates a new key and adds empty data
                data_dict[author] = {
                    "COMMITS": 1,
                    "COMMITS_TO_TESTING": 0,
                    "COMMITS_ELSEWHERE": 0,
                    "PERCENT_TO_TESTING": 0,
                    "PERCENT_NOT_TO_TESTING": 0,
                }

            count = 0  # when 0 the current commit has no changes to tests
            for filepath in filepaths:
                # when count == 0, current commit no testing changes
                # if not 0, this commit already had testing changes
                if count == 0:
                    if filepath and "test" in filepath:
                        data_dict[author][
                            "COMMITS_TO_TESTING"
                        ] += 1  # the current commit has a change to testing
                        count = 1  # found a change to testing for this commit
                    else:
                        pass
                else:
                    pass
            # Sort list to ensure consistency when testing
        # iterate through the data to do final calculations
        for key in data_dict:
            data_dict[key]["PERCENT_TO_TESTING"] = (
                data_dict[key]["COMMITS_TO_TESTING"] / data_dict[key]["COMMITS"]
            ) * 100

            data_dict[key]["COMMITS_ELSEWHERE"] = (
                data_dict[key]["COMMITS"] - data_dict[key]["COMMITS_TO_TESTING"]
            )

            data_dict[key]["PERCENT_NOT_TO_TESTING"] = (
                data_dict[key]["COMMITS_ELSEWHERE"] / data_dict[key]["COMMITS"]
            ) * 100
        # Reformat the dictionary as a value of the key INDIVIDUAL_METRICS
        testing_dict = {"TESTING_DICT": data_dict}
        return testing_dict
    return {}


def print_testing_in_table(file_name):
    """Create and print the table of testing data using prettytable."""
    data_table = PrettyTable()
    current_data = json_handler.get_dict_from_json_file(file_name)
    dictionary = current_data["TESTING_DICT"]
    headings = [
        "Username",
        "Commits",
        "Commits to Testing",
        "Commits Elsewhere",
        "Percent of Commits to Testing",
        "Percent of Commits not to Testing",
    ]
    data_table.field_names = headings
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key]["COMMITS"],
                dictionary[key]["COMMITS_TO_TESTING"],
                dictionary[key]["COMMITS_ELSEWHERE"],
                dictionary[key]["PERCENT_TO_TESTING"],
                dictionary[key]["PERCENT_NOT_TO_TESTING"],
            ]
        )
    print(data_table)


# NOTE: For the purposes of testing and demo

# Steps to run data_collection.py and display the data table:

# Must be in the repository folder
# Run the python file using `pipenv run python src/data_collection.py`
# Enter the name of the json file you want the data to be written to
# If prompted, due to data not being collected previously, enter the URL
# or path of the Repository you would like to analyze
# If the current repository is the one you would like to analyze, simply
# hit enter wihtout typing anything.

if __name__ == "__main__":
    # NOTE: this supression needs to be resolved
    # pylint: disable=input-builtin
    FILE_NAME = input("Enter the name of the file : ")
    # FILE_NAME = "contributor_data_template"
    DATA = calculate_individual_metrics(FILE_NAME)
    if DATA == {}:
        REPO_PATH = input("Enter the path to the repo : ")
        add_raw_data_to_json(REPO_PATH, FILE_NAME)
        print("processing data again")
        DATA = calculate_individual_metrics(FILE_NAME)
    print("Adding processed data to selected json file...")
    # Write reformatted dictionary to json
    json_handler.add_entry(DATA, FILE_NAME)
    print_individual_in_table(FILE_NAME)

    DATA = get_testing_commit_info(FILE_NAME)
    if DATA == {}:
        add_raw_data_to_json(REPO_PATH, FILE_NAME)
        print("processing data again")
        DATA = get_testing_commit_info(FILE_NAME)
    print("Adding processed data to selected json file...")
    # Write reformatted dictionary to json
    json_handler.add_entry(DATA, FILE_NAME)
    print_testing_in_table(FILE_NAME)
