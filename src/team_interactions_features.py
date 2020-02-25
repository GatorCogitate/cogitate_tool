""" Features to measure code hoarding and common collaborations in branches. """

# Definition of shared dictionary
repo_name = "Cogitate"
branch_1 = ["user1", "user2", "user3", "user4"]
branch_2 = ["user1", "user2", "user4"]
branch_3 = ["user4"]
branch_4 = ["user3", "user1"]
branch_5 = ["user2"]
branch_dict = {
    "branch1": branch_1,
    "branch2": branch_2,
    "branch3": branch_3,
    "branch4": branch_4,
    "branch5": branch_5,
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
    "user1": b1_user1,
    "user2": b1_user2,
    "user3": b1_user3,
    "user4": b1_user4
}

commit_branch_2 = {
    "user1": b2_user1,
    "user2": b2_user2,
    "user3": b2_user3,
    "user4": b2_user4
}

commit_branch_3 = {
    "user1": b3_user1,
    "user2": b3_user2,
    "user3": b3_user3,
    "user4": b3_user4
}

commit_branch_4 = {
    "user1": b4_user1,
    "user2": b4_user2,
    "user3": b4_user3,
    "user4": b4_user4
}

commit_branch_5 = {
    "user1": b5_user1,
    "user2": b5_user2,
    "user3": b5_user3,
    "user4": b5_user4
}

commit_branch_dict = {
    "branch1": commit_branch_1,
    "branch2": commit_branch_2,
    "branch3": commit_branch_3,
    "branch4": commit_branch_4,
    "branch5": commit_branch_5,
}


def code_hoarders(b_dict=branch_dict):
    """ Method to determine code hoarders. """
    code_hoarder_list = ["Repo: " + repo_name]
    for branch_name, user_list in branch_dict.items():
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
    return code_hoarder_list


c_h_list = code_hoarders()
for value in c_h_list:
    print(value)


def collaborators():
    """ Method to determine frequent collaborators in a team project. """
    collaborator_list = []
    col_max = 5
    for branch_name, user_list in branch_dict.items():
        if len(user_list) > 1:
            collaborator_list.append(branch_name)
