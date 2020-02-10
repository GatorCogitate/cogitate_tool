"""FastAPI Demo designed to accept user cedentials and display GitHub info."""
from fastapi import FastAPI
from github import Github

# First create a Github instance using an access token
app = FastAPI()
current_user_token = "Error Not Available"
current_user_account = Github()


@app.get("/create_user")
def create_user(user_token):
    """Take token input from user and creates global GitHub object."""
    # pylint: disable=global-statement
    global current_user_token
    current_user_token = user_token
    # pylint: disable=global-statement
    global current_user_account
    current_user_account = Github(user_token)
    user = current_user_account.get_user()
    statement = user.login + " created successfully!"
    return statement


@app.get("/repo_list")
def get_repo_list():
    """List the users repositories' names."""
    # user_token = input("Enter your github token: ")
    # g = Github(user_token)
    repo_list = []
    count = 0
    # pylint: disable=global-statement
    global current_user_account
    for repo in current_user_account.get_user().get_repos():
        print("[" + str(count) + "]" + repo.name)
        count = count + 1
        repo_list.append(repo.name)
    print("This user has " + str(count) + " repos")
    return repo_list


@app.get("/branches_list")
def get_repo_info(repo_index):
    """Please enter the repository number to show information."""
    # pylint: disable=global-statement
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


def main_method():
    """Use to call previous functions in case of running through terminal."""
    userToken = str(input("Please enter your GitHub token: "))
    print(create_user(userToken))
    get_repo_list()
    repoIndex = int(input("Please enter an index number to show information:"))
    print(get_repo_info(repoIndex))


choice = input("call main? (y = yes/ n = no)")
if choice == "y":
    main_method()
