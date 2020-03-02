""" Collects commit data for contributors of the master branch of a repo."""
from pydriller import RepositoryMining
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
    Create a list of dictionaries that contains commit info.

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
            "author_date": commit.author_date.date(),
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
