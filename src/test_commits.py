from datetime import datetime
from pydriller import RepositoryMining, GitRepository
#from pydriller.domain.commit import ModificationType

dt1 = datetime(2016,2,1)
dt2 = datetime.now()


for commit in RepositoryMining("https://github.com/lussierc/simplePerformanceExperimentsJava").traverse_commits():
    print("COMMIT:")
    print("--- Commit Tag: ", commit.hash)
    print("--- Commit Author: ", commit.author.name)
    print("--- Commit Date: ", commit.author_date)

    for modified_file in commit.modifications:
        print("--- File Modified: ", modified_file.new_path)
    # for modified_file in commit.modifications:
    #     print(commit.has + "Modified file" + modified_file.filename)
