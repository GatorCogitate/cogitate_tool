"""FastAPI Demo designed to accept user cedentials and display GitHub info."""
from fastapi import FastAPI
from github import Github

print("Welcome to the FastAPI Demo!")
# First create a Github instance using an access token
app = FastAPI()
current_user_token = "Error Not Available"
current_user_account = Github()


@app.get("/create_user")
def create_user(user_token):
    """Take token input from user and creates global GitHub object."""
    # pylint: disable=global-statement
    print("Creating a Github object from the user token...")
    # Establishes the current_user_token variable as a global variable
    global current_user_token
    # Sets the user token to the value passed to the method
    current_user_token = user_token
    # Establishes user account as a global variable
    global current_user_account
    # Sets the current user account to the value passed to GitHub()
    current_user_account = Github(user_token)
    # Sets the variable user equal to current_user_account
    user = current_user_account.get_user()
    # Creates a statement to be thrown indicating the succesful creation of a user_token
    statement = user.login + " created successfully!"
    print("User token added!")
    return statement


@app.get("/repo_list")
def get_repo_list():
    """Initializes list the users repositories' names and counts the number of them."""
    # pylint: disable=global-statement
    print("Creating list of the user's repositories...")
    repo_list = []
    count = 0
    global current_user_account
    # Iterates through the user's repositories and populates them into a list
    for repo in current_user_account.get_user().get_repos():
        print("[" + str(count) + "]" + repo.name)
        count = count + 1
        repo_list.append(repo.name)
    # Display's the number of repositories in the user's GitHub account
    print("This user has " + str(count) + " repos")
    return repo_list


@app.get("/org_repo_list")
def get_org_repo_list(repo_index):
    """Initializes list the users repositories' names and counts the number of them."""
    # pylint: disable=global-statement
    global current_user_account
    # current_repo = current_user_account.get_user().get_repos()[int(repo_index)]
    # commit_list = []
    # count = 0
    # Iterates through the user's repositories and populates them into a list
    my_commit = (
        current_user_account.get_user()
        .get_repos()[int(repo_index)]
        .get_branch("master")
        .commit.sha
    )
    # print("[" + str(count) + "]" + commits.sha)
    # count = count + 1
    # commit_list.append(commits.sha)
    # Display's the number of repositories in the user's GitHub account
    # print("This user has " + str(count) + " repos")
    return my_commit


@app.get("/branches_list")
def get_repo_info(repo_index):
    """Please enter the number of the repository from the previous list to show information."""
    # pylint: disable=global-statement
    print("Finding the number of branches in the repository and their names...")
    global current_user_account
    # isolates a single repo in the user's Github to find the branches
    current_repo = current_user_account.get_user().get_repos()[int(repo_index)]
    # adds all of the branches in the repo to a list
    branches_list = current_repo.get_branches()
    branches_names = []
    count = 0
    # counts the number of branches in the repo, adds each branch name to a list
    for branch in branches_list:
        # print(branch.name)
        count = count + 1
        branches_names.append(branch.name)
    # displays the number of branches in the repo in the terminal
    print(
        "This user has "
        + str(count)
        + " branches in the "
        + current_repo.name
        + " repository"
    )
    # returns the list of the branch names
    return branches_names


def main_method():
    """Use to call previous functions in case of running through terminal."""
    # pylint: disable=input-builtin
    print("Running the main method...")
    userToken = str(input("Please enter your GitHub token: "))
    print("Creating a user token based on user-entered credentials...")
    print(create_user(userToken))
    print("Getting the list of repositories from GitHub...")
    get_repo_list()
    repoIndex = int(input("Please enter an index number to show information:"))
    print("Accessing repository index based on user-provided value...")
    print("Printing the repository information based on the user-provided value...")
    print(get_repo_info(repoIndex))


# pylint: disable=input-builtin
choice = input("call main? (y = yes/ n = no)")
if choice == "y":
    main_method()
