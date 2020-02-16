from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType

for commit in RepositoryMining('/home/teona/Documents/CS203/labs/cogitate_tool').traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " added to {}".format(m.filename),
            "lines of code {}".format(m.added)
        )

for commit in RepositoryMining('/home/teona/Documents/CS203/labs/cogitate_tool').traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " removed from {}".format(m.filename),
            "lines of code {}".format(m.removed)
        )
