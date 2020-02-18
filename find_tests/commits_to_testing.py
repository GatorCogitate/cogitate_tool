# Class Roster: Caden Hinckley, Devin Spitalny, Tyler Pham, Cory Wiard,
# Jordan Wilson, Anthony Baldeosingh, Caden Koscinski, Christopher Stephenson
# Danny Reid, Jordan Byrne, Madelyn Kapfhammer, Megan Munzek, Pedro Carmo,
# Hannah Schultz, Xingbang Liu, Devin Ho, Spencer Huang, Christian Lussier,
# Jacob Stringer, Marisol Santa Cruz, Thomas Cassidy, Wonjoon Cho,
# Teona Bagashvili, Claire Johns, Collin McNulty

from datetime import datetime
from pydriller import RepositoryMining, GitRepository

commit_author_list = []

def find_testing_commits():
    global commit_author_list
    global total_commit_count

    for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
        if commit.author.name not in commit_author_list:
            commit_author_list.append(commit.author.name)
            print("Adding author,", commit.author.name)
        else:
            pass

    for author_name in commit_author_list:
        author_commit_count = 0
        total_commit_count = 0
        total_test_commit_count = 0
        for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
            count = 0
            if commit.author.name in author_name:
                author_commit_count = author_commit_count + 1
                for modified_file in commit.modifications:
                    file_path = modified_file.new_path
                    if count is 0:
                        if file_path:
                            if "test" in file_path:
                                print("Found someone who modified tests in file", commit.author.name, file_path, commit.hash)
                                total_test_commit_count += 1
                                count = 1
                            else:
                                pass
            if commit.author.name in commit_author_list:
                total_commit_count = total_commit_count + 1

        print(author_name, "'s Total commits: ", author_commit_count)
        print("-- Testing commits by", author_name, total_test_commit_count)
        percentage_covered = (total_test_commit_count / author_commit_count) * 100
        print("-- Percentage of Commits Going to Testing:", percentage_covered)

    print()
    print("total commits: ", total_commit_count)


if __name__ == "__main__":
    find_testing_commits()
