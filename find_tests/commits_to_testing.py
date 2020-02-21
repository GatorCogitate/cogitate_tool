"""Determines frequency of a GitHub repo author's commits to testing."""

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


def get_commit_info(commit_author_list, user_repo):
    """Retrieves information from the repostory relating to commits to testing."""

    # Calculates the total commits like author, test and general and connecting
    # to the chosen repo
    for author_name in commit_author_list:
        author_commit_count = 0
        total_commit_count = 0
        total_test_commit_count = 0
        for commit in RepositoryMining(
            user_repo, only_authors=commit_author_list
        ).traverse_commits():
            count = 0
            # Connects the author name to the amount of commits made by user the
            # clear path to the repo
            if commit.author.name in author_name:
                author_commit_count = author_commit_count + 1
                for modified_file in commit.modifications:
                    file_path = modified_file.new_path
                    if count is 0:
                        if file_path:
                            if "test" in file_path:  # sees if the commit was to testing
                                # print(
                                #     "Found someone who modified tests: ",
                                #     # will calculate the modifications to the test
                                #     commit.author.name,
                                #     file_path,
                                #     commit.hash,
                                # )
                                total_test_commit_count += 1
                                count = 1
                            else:
                                pass
            if commit.author.name in commit_author_list:
                total_commit_count = total_commit_count + 1
        # Print statements that release the calculations of the declared variables
        print(author_name, "'s Total commits: ", author_commit_count)
        print("-- Testing commits by", author_name, ":", total_test_commit_count)
        try:
            percentage_covered = (total_test_commit_count / author_commit_count) * 100
        except:
            percentage_covered = 0
        print("-- Percentage of Commits Going to Testing:", percentage_covered, "%")
        print("\n\n")


def main():
    """Driver function. Runs all other necessary functions."""

    user_repo = input("Enter the link to your chosen GitHub repository: ")
    commit_author_list = get_repo_authors(user_repo)
    commit_author_list = single_multi_author_choice(commit_author_list)
    get_commit_info(commit_author_list, user_repo)


main()  # call the main function; run the program
