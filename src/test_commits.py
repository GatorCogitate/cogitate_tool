from datetime import datetime
from pydriller import RepositoryMining, GitRepository
from array import *
#from pydriller.domain.commit import ModificationType

dt1 = datetime(2016,2,1)
dt2 = datetime.now()
c = 0
s = 0 
d = 0

for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
    print("COMMIT:")
    print("--- Commit Tag: ", commit.hash)
    print("--- Commit Author: ", commit.author.name)
    print("--- Commit Date: ", commit.author_date)
    if 'clussier' in commit.author.name:
        c = c + 1
    if 'Spencer Huang' in commit.author.name:
        s = s + 1
    if 'Devin Ho' in commit.author.name:
        d = d + 1

    for modified_file in commit.modifications:
        print("--- File Modified: ", modified_file.new_path)
    # for modified_file in commit.modifications:
    #     print(commit.has + "Modified file" + modified_file.filename)

print()
print("clussier total commits: ", c)
print()
print("Spencer Huang total commits: ", s)
print()
print("Devin Ho total commits: ", d)
