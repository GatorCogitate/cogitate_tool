""" Features to measure code hoarding and common collaborations in branches. """

# Definition of shared dictionary
repo_name = "Cogitate"
branch_1 = ["user 1", "user 2", "user 3", "user 4"]
branch_2 = ["user 1", "user 2", "user 4"]
branch_3 = ["user 4"]
branch_4 = ["user 3", "user 1"]
branch_5 = ["user 2"]
branch_dict = {
    "branch 1": branch_1,
    "branch 2": branch_2,
    "branch 3": branch_3,
    "branch 4": branch_4,
    "branch 5": branch_5,
}
# branch one commits by user
b1_user1 = [27, 28]
b1_user2 = [8, 5, 7, 6]
b1_user3 = [3, 4, 2, 4]
b1_user4 = [8, 2, 2]
# branch 2
b2_user1 = [12, 8, 10]
b2_user2 = [7, 5, 9, 5]
b2_user3 = [0]
b2_user4 = [6, 15, 8, 4]
# branch 3
b3_user1 = [0]
b3_user2 = [0]
b3_user3 = [0]
b3_user4 = [6, 18, 8]
# branch 4
b4_user1 = [22, 25, 18]
b4_user2 = [0]
b4_user3 = [12, 9, 14]
b4_user4 = [0]
# branch 5
b5_user1 = [0]
b5_user2 = [8, 4, 7, 8, 1]
b5_user3 = [0]
b5_user4 = [0]

commit_branch_1 = {
    "user 1": b1_user1,
    "user 2": b1_user2,
    "user 3": b1_user3,
    "user 4": b1_user4
}

commit_branch_2 = {
    "user 1": b2_user1,
    "user 2": b2_user2,
    "user 3": b2_user3,
    "user 4": b2_user4
}

commit_branch_3 = {
    "user 1": b3_user1,
    "user 2": b3_user2,
    "user 3": b3_user3,
    "user 4": b3_user4
}

commit_branch_4 = {
    "user 1": b4_user1,
    "user 2": b4_user2,
    "user 3": b4_user3,
    "user 4": b4_user4
}

commit_branch_5 = {
    "user 1": b5_user1,
    "user 2": b5_user2,
    "user 3": b5_user3,
    "user 4": b5_user4
}

commit_branch_dict = {
    "branch 1": commit_branch_1,
    "branch 2": commit_branch_2,
    "branch 3": commit_branch_3,
    "branch 4": commit_branch_4,
    "branch 5": commit_branch_5,
}


def code_hoarders(b_dict=branch_dict, avg_lines_per_commit=12):
    """ Method to determine code hoarders. """
    # add repo name to list to be printed.
    code_hoarder_list = []
    commit_lines = []
    # iterate through the branch dictionary
    for branch_name, user_list in branch_dict.items():
        # when there is only on user committing to a branch, label them a code
        # hoarder
        if len(user_list) == 1:
            code_hoarder_list.append(
                user_list[0]
                + " is a code hoarder,"
                + " since they were the only "
                + "contributor to: "
                + branch_name
            )
        else:
            pass
    # end of for branch_name, user_list in branch_dict.items()

    # Iterate through the branch dit
    for branch_name, branch in commit_branch_dict.items():
        for user_name, commit_list in branch.items():
            for commit in commit_list:
                if commit > (avg_lines_per_commit +
                             (avg_lines_per_commit/3)):
                    commit_lines.append(commit)
                else:
                    pass
            # end of "for commit in commit_list"
            if len(commit_lines) > 1:
                code_hoarder_list.append(
                    user_name
                    + " is a code hoarder,"
                    + " as their commits were often too long "
                    + "when contributing to: "
                    + branch_name
                )
                commit_lines.clear()
            else:
                commit_lines.clear()
        # end of for user_name, commit_list in branch.items()
    # end of branch_name, branch in commit_branch_dict.items()
    return code_hoarder_list


c_h_list = code_hoarders()
print("Repo: " + repo_name)
for value in c_h_list:
    print(value)


def collaborators():
    """ Method to determine frequent collaborators in a team project. """
    collaborator_list = []
    col_max = 5
    for branch_name, user_list in branch_dict.items():
        if len(user_list) > 1:
            collaborator_list.append(branch_name)
