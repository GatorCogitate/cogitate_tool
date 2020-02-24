# python file created


from pydriller import RepositoryMining, GitRepository  # import necessary libraries

def get_repo_authors(user_repo):
    """Accesses the remote repo and puts author names in a list."""

    # accesses users
    commit_author_list = []
    # accesses github repo to calculate users commits
    for commit in RepositoryMining(user_repo).traverse_commits():
        if commit.author.name not in commit_author_list:
            commit_author_list.append(commit.author.name)
            print("Adding author,", commit.author.name)
        else:
            pass

    print("-- Repo Authors:")
    for author_name in commit_author_list:
        print(author_name)

    return commit_author_list



def main():
    """Driver function. Runs all other necessary functions."""

    user_repo = input("Enter the link to your chosen GitHub repository: ")

main()  # call the main function; run the program
