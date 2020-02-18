from datetime import datetime
from pydriller import RepositoryMining, GitRepository
from array import *
#from pydriller.domain.commit import ModificationType

commit_list = []
commit_author_list = []

for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
    if commit.author.name not in commit_author_list:
        commit_author_list.append(commit.author.name)
        print("Adding author,", commit.author.name)
    else:
        pass

# Class Roster: Caden Hinckley, Devin Spitalny, Tyler Pham, Cory Wiard,
# Jordan Wilson, Anthony Baldeosingh, Caden Koscinski, Christopher Stephenson
# Danny Reid, Jordan Byrne, Madelyn Kapfhammer, Megan Munzek,
for i in commit_author_list:
    b = 0
    c = 0
    d = 0
    for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
        count = 0
        if commit.author.name in i:
            b = b + 1
            for modified_file in commit.modifications:
                file_path = modified_file.new_path
                if count is 0:
                    if file_path:
                        if "test" in file_path:
                            print("Found someone who modified tests in file", commit.author.name, file_path, commit.hash)
                            d += 1
                            count = 1
                        else:
                            pass
        if commit.author.name in commit_author_list:
            c = c + 1

    print(i, b)
    print("-- Testing commits by", i, d)

print()
print("total commits: ", c)
