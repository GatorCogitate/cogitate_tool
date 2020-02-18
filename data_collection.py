from pydriller import RepositoryMining
import pprint

author_dict = {}

repo_path = "https://github.com/GatorCogitate/cogitate_tool"
for commit in RepositoryMining(repo_path).traverse_commits():
    if commit.author.email not in author_dict.keys():
        author_dict[commit.author.email] = [commit]
    else:
        author_dict[commit.author.email].append(commit)

# pprint.pprint(commit_lst)
# for commit in commit_lst:
#    if commit["author"] not in author_dict.keys():
#        author_dict[commit["author"]] = [commit["commit"]]
#    else:
#        author_dict[commit["author"]].append(commit["commit"])

pprint.pprint(author_dict)

# for commit in author_dict["cklima616"]:
#    print(commit.committer.email)
#    print(commit.committer.name)
