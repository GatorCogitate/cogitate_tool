# python file created


from pydriller import RepositoryMining, GitRepository  # import necessary libraries

def get_repo_authors(user_repo):
    """Accesses the remote repo and puts author names in a list."""

    # Will we want to recreate all this like function 1 or call those functions
    # in
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

def single_multi_author_choice(commit_author_list):
    """Offers user the choice of looking at all or one specific author(s)."""

    user_author_choice = int(
        input(
            "-- Would you like to look at (1) all authors or a (2) specific author?: "
        )
    )
    if user_author_choice == 1:
        pass
    elif user_author_choice == 2:
        # Looks for specific author contributions
        specific_author = input("-- Enter author name:")
        if specific_author in commit_author_list:
            commit_author_list = [specific_author]
    else:
        print("Invalid choice!")

    return commit_author_list



def main():
    """Driver function. Runs all other necessary functions."""

    user_repo = input("Enter the link to your chosen GitHub repository: ")
    commit_author_list = get_repo_authors(user_repo)
    commit_author_list = single_multi_author_choice(commit_author_list)

main()  # call the main function; run the program
