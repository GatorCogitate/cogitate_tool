from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType

path = input("Enter the path to the repo : ")

for commit in RepositoryMining(path).traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " added to {}".format(m.filename),
            "lines of code {}".format(m.added)
        )

print("")

for commit in RepositoryMining(path).traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " removed from {}".format(m.filename),
            "lines of code {}".format(m.removed)
        )
