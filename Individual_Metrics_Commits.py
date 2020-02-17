"""FastAPI Demo designed to accept user credentials and display GitHub info."""
from github import Github
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from fastapi import FastAPI

# First create a Github instance using an access token

user_token = input("Enter User Token: ")
user = Github(user_token)
print(user.get_user().login)
username = user.get_user().login
repo = user.get_repo("GatorCogitate/cogitate_tool")
allcommits = repo.get_commits()
for commit in allcommits:
    print(commit.author)


# First create a Github instance using an access token
app = FastAPI()
current_user_token = "Error Not Available"
current_user_account = Github()


@app.get("/create_user")
def create_user(user_token):
    # pylint: disable=global-statement
    """Take token input from user and creates global GitHub object."""
    global current_user_token
    current_user_token = user_token
    global current_user_account
    current_user_account = Github(user_token)
    user = current_user_account.get_user()
    statement = user.login + " created successfully!"
    return statement


@app.get("/repo_list")
def get_repo_list():
    """List the users repositories' names."""
    # pylint: disable=global-statement
    repo_list = []
    count = 0
    global current_user_account
    for repo in current_user_account.get_user().get_repos():
        print("[" + str(count) + "]" + repo.name)
        count = count + 1
        repo_list.append(repo.name)
    print("This user has " + str(count) + " repos")
    return repo_list


@app.get("/branches_list")
def get_repo_info(repo_index):
    # pylint: disable=global-statement
    """Please enter the number of the repository from the previous list to show information."""
    global current_user_account
    current_repo = current_user_account.get_user().get_repos()[int(repo_index)]
    # branches_list = current_repo.get_branches()
    branches_list = current_repo.get_branches()
    branches_names = []
    count = 0
    for branch in branches_list:
        # print(branch.name)
        count = count + 1
        branches_names.append(branch.name)
    print(
        "This user has "
        + str(count)
        + " branches in the "
        + current_repo.name
        + " repository"
    )
    return branches_names


def get_repo_commits():
    """ """
    path = input("Enter the path to the repo : ")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " added to {}".format(m.filename),
                "lines of code {}".format(m.added),
            )

    print("")

    for commit in RepositoryMining(path).traverse_commits():
        for m in commit.modifications:
            print(
                "Author {}".format(commit.author.name),
                " removed from {}".format(m.filename),
                "lines of code {}".format(m.removed),
            )


def main_method():
    # pylint: disable=input-builtin
    """Use to call previous functions in case of running through terminal."""

    # get_repo_list()
    repoIndex = int(input("Please enter an index number to show information:"))
    # print(get_repo_info(repoIndex))

    get_repo_commits()


choice = input("call main? (y = yes/ n = no)")
if choice == "y":
    main_method()
