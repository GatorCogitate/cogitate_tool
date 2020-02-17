from datetime import datetime
from pydriller import RepositoryMining, GitRepository
from array import *
#from pydriller.domain.commit import ModificationType

dt1 = datetime(2016,2,1)
dt2 = datetime.now()
list = ["clussier", "Spencer Huang", "Devin Ho", "Christian Lussier", "Lancaster Wu", "Juncheng Wu", "Gregory M. Kapfhammer"]
# Class Roster: Caden Hinckley, Devin Spitalny, Tyler Pham, Cory Wiard,
# Jordan Wilson, Anthony Baldeosingh, Caden Koscinski, Christopher Stephenson
# Danny Reid, Jordan Byrne, Madelyn Kapfhammer, Megan Munzek,
for i in list:
    b = 0
    c = 0
    for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
        if commit.author.name in i:
            b = b + 1
        # print("COMMIT:")
        # print("--- Commit Tag: ", commit.hash)
        # print("--- Commit Author: ", commit.author.name)
        # print("--- Commit Date: ", commit.author_date)
        if commit.author.name in list:
            c = c + 1
    print(i, b)


    for modified_file in commit.modifications:
        print("--- File Modified: ", modified_file.new_path)
    # for modified_file in commit.modifications:
    #     print(commit.has + "Modified file" + modified_file.filename)

print()
print("total commits: ", c)
