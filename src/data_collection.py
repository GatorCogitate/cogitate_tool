""" Collects commit data for a single user. """
from pydriller import RepositoryMining

import pprint


# indicate path for repository by pluggin in the URL of repo (must be public)
repo_path = "https://github.com/GatorCogitate/cogitate_tool"


def collect_commits_user_email_key(repo):
    # TODO: edit the method to take in the URL for the repo
    """ Creates a dictionary of commit objects for a single user. """
    # holds email of repo members as keys, contents of commit object as values
    author_dict = {}


    # loop to turn the each Commits object into the values of the dictionary `author_dict`
    for commit in RepositoryMining(repo).traverse_commits():
        if commit.author.email not in author_dict.keys():
            author_dict[commit.author.email] = [commit]
        else:
            author_dict[commit.author.email].append(commit)
    return author_dict


def collect_commits_hash(repo):

    commit_list = []

    for commit in RepositoryMining(repo).traverse_commits():

        line_added = 0
        line_removed = 0
        line_of_code = 0
        complexity = 0
        methods = []
        filename = []

        for item in commit.modifications:

            line_added += item.added
            line_removed += item.removed
            if item.nloc is not None:
                line_of_code += item.nloc
            if item.complexity is not None:
                complexity += item.complexity
            # methods.append([method.name for method in item.methods])

            for method in item.methods:
                methods.append(method.name)
            filename.append(item.filename)

        single_commit_dict = {
        "hash":commit.hash,
        "author_msg":commit.msg,
        "author_name":commit.author.name,
        "author_email":commit.author.email,
        "author_date":commit.author_date.date(),
        "merge":commit.merge,
        "line_added":line_added,
        "line_removed":line_removed,
        "lines_of_code":line_of_code,
        "complexity":complexity,
        "methods":methods,
        "filename":filename
        }
        commit_list.append(single_commit_dict)



        print(commit_list)


collect_commits_hash(repo_path)
#     return commit_list
#
# pprint.pprint(collect_commits_hash(repo_path))
#
# def new_f(repo):
#     for commit in RepositoryMining(repo).traverse_commits():
        # print(commit.modifications)
        #print(' '.join([str(elem) for elem in commit.modifications]))
        # print("----------------------------")
        # for item in commit.modifications:
        #     print(item.nloc)

# new_f(repo_path)
