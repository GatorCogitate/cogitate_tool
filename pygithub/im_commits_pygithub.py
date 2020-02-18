"""Demo designed to find and store information about PyGithub."""
from github import Github

test_dict = {}


def print_dictionary(dictionary):
    """Method to print out the hash map."""
    # print headings
    print("Branch", "\t Author", "\t Time", "\t Files", "\t Message")
    # prints hashmap content
    # for key in dictionary:

    for key, _ in dictionary.items():
        print(key)
        for items in dictionary[key]:
            for item in items:
                print("\t" + str(item) + "\t")
            # print("\t" + str(item))


def get_repo_commits_pygithub(user):
    """Method to get commit information using pygithub"""

    username = user.get_user().login
    print(username)
    repo = user.get_repo("GatorCogitate/cogitate_tool")
    all_branches = repo.get_branches()

    branches = {}

    for branch in all_branches:
        # Create an empty list.
        data_list = list()
        all_commits = repo.get_commits()
        all_comments = repo.get_comments()
        print(branch)
        for commit in all_commits:
            commit_info = (
                branch.name,
                commit.commit.author,
                commit.commit.author.date,
                commit.files,
                commit.commit.message,
            )
            data_list.append(commit_info)

        branches[branch.name] = data_list
    return branches


if __name__ == "__main__":
    user_token = input("Enter User Token: ")
    user = Github(user_token)

    dictionary = get_repo_commits_pygithub(user)
    output_hash_map(dictionary)
