from fastapi import FastAPI
from github import Github

# First create a Github instance using an access token
app = FastAPI()

@app.get("/")
def get_repo_list(user_token):
    # user_token = raw_input("Enter your github token: ")
    g = Github(user_token)
    repo_list = []
    count = 0
    for repo in g.get_user().get_repos():
        # print(repo.name)
        count = count + 1
        repo_list.append(repo.name)
    print("This user has ", count, " repos")
    return (repo_list, "This user has ", count, " repos")
