""" Features to measure code hoarding and common collaborations in branches. """

# Definition of shared dictionary
repo_name = "cogitate"
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


def code_hoarders():
    """ Method to determine code hoarders. """
    code_hoarder_list = []
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
            collaborator_list.append(user_list[0])
