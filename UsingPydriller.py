from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType

path = input("Enter the path to the repo : ")
data_list = {"keys":["+", "-", "Total"]}
# print(data_list)
# appended_list = ["Noor", 7, 9, 10]
# data_list.append(appended_list)
# appended_list = ["Elian", 10, 16, 22]
# data_list.append(appended_list)
# # print(data_list)
# # print(len(data_list))
# for i in range(len(data_list)):
#     for j in range(len(data_list[0])):
#         print(data_list[i][j], "\t", end="", flush=True)
#     print("")



for commit in RepositoryMining(path).traverse_commits():
    author = commit.author.name
    print(author)
    for m in commit.modifications:
        added_lines = m.added
        removed_lines = m.removed
        total_lines = added_lines - removed_lines
        if author in data_list:
        # "Author {}".format(commit.author.name),
        # " added to {}".format(m.filename),
            data_list[author][0] += added_lines
            data_list[author][1] += removed_lines
            data_list[author][2] += total_lines
        else:
            data_list[author] = [added_lines, removed_lines, total_lines]
print(data_list)
# print("")

# for commit in RepositoryMining(path).traverse_commits():
#     for m in commit.modifications:
#         print(
#             "Author {}".format(commit.author.name),
#             " removed from {}".format(m.filename),
#             "lines of code {}".format(m.removed)
#         )
