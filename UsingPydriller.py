from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType

for commit in RepositoryMining('/home/teona/Documents/CS203/labs/cs203-S2020-assessment').traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " modified {}".format(m.filename),
            "with adding lines of code {}".format(m.added)
        )
