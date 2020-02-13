from datetime import datetime
from pydriller import RepositoryMining, GitRepository
#from pydriller.domain.commit import ModificationType

dt1 = datetime(2016,2,1)
dt2 = datetime.now()

for commit in RepositoryMining("https://github.com/GatorCogitate/cogitate_tool").traverse_commits():
    print(commit.hash)


    for modified_file in commit.modifications:
        print(modified_file.filename)

    # for modified_file in commit.modifications:
    #     print(commit.has + "Modified file" + modified_file.filename)
