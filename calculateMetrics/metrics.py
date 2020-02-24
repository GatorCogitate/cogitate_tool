"""Determine how the well the team worked together"""

import numpy as np

# github_data is a list containing sample data for our demo
# github_data uses the pattern ["username", commit_total, lines_added,
# lines_deleted, issues_opened]
github_data = [
    ["cassidyt2", 28, 355, 76, 2],
    ["johnSmith", 22, 349, 50, 4],
    ["janeDoe", 23, 375, 30, 3],
    ["Edgar_AllenPoe", 27, 315, 75, 7],
    ["George_Washington", 25, 360, 65, 10],
    ["Alexander_Hamilton", 41, 530, 100, 230],
    ["Karl_Marx", 0, 0, 0, 400],
    ["Julius_Caesar", 25, 310, 68, 1],
]
standard_deviations_list = []
values_list = []
# commits_list = []
# added_list = []
# removed_list = []
commits_overall_score = 0
added_overall_score = 0
removed_overall_score = 0
total_team_score = 0


def standard_deviations():
    """Function to calculate the standard_deviations of commits, lines added,
    and lines removed"""
    new_counter = 1
    holder_list = []
    global values_list
    github_data_counter = 0
    values_list_loop_terminator = 0
    global github_data
    # Finds the length of the 1st sublist (index[0]) in github_data
    for x in github_data:
        values_list_loop_terminator_max = (
            len(x) - 1
        )  # This is because new_counter always starts at index 1 of each sublist
        # print(values_list_loop_terminator_max)
        break
    while github_data_counter <= len(github_data):
        if github_data_counter == len(github_data):
            values_list.append(holder_list)
            # Resets the first index count and the holder_list
            holder_list = []
            github_data_counter = 0
        if values_list_loop_terminator == values_list_loop_terminator_max * len(
            github_data
        ):
            # return values_list
            break
        holder_list.append(github_data[github_data_counter][new_counter])
        github_data_counter += 1
        values_list_loop_terminator += 1
        if github_data_counter == len(github_data):
            new_counter += 1
    global standard_deviations_list
    standard_deviations_list = []
    standard_deviation_counter = 0
    while standard_deviation_counter <= len(values_list) - 1:
        standard_deviations_list.append(np.std(values_list[standard_deviation_counter]))
        standard_deviation_counter += 1


def commits_calculator():
    """This will determine how well the team worked together by analyzing the
    spread of commits"""
    global standard_deviations_list
    global values_list
    # global commits_list
    commits_list = values_list[0]
    # print("Commits average is: ", np.average(values_list[0]))
    # print("Commits standard deviation is: ", np.std(standard_deviations_list[0]))
    # Standard deviation of commits
    commits_sd = standard_deviations_list[0]
    commit_scores = []
    username_accesser = 0
    for ab in range(len(github_data)):
        # This if/else calculates the commits added to the standard deviation,
        # in order to grade the team.
        # print("Checking GitHub user: ", github_data[username_accesser][0])
        if github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 0.5
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 0.5
        ):
            # print("appending 5 to commit_scores list")
            commit_scores.append(5)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 1.0
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 1.0
        ):
            # print("appending 4 to commit_scores list")
            commit_scores.append(4)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 1.5
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 1.5
        ):
            # print("appending 3 to commit_scores list")
            commit_scores.append(3)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 2.0
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 2.0
        ):
            # print("appending 2 to commit_scores list")
            commit_scores.append(2)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 2.25
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 2.25
        ):
            # print("appending 1 to commit_scores list")
            commit_scores.append(1)
            username_accesser += 1
        else:
            # print("appending 0 to commit_scores list")
            commit_scores.append(0)
            username_accesser += 1
    global commits_overall_score
    commits_overall_score = np.average(commit_scores)
    # The "''...'_percent" variables calculate the percentage score the team received for this category. These print statments print out the scores for the amount of commits the team added
    commits_percent = commits_overall_score / 5
    commits_percent = np.around(commits_percent, decimals=2)
    print(
        "\nThe team earned a score of: [",
        np.average(commit_scores),
        "/ 5] for teamwork on lines removed, or: ",
        "{:.2%}".format(commits_percent),
        "\n",
    )


def added_calculator():
    """This will determine how well the team worked together by analyzing the
    spread of lines of code added"""
    global standard_deviations_list
    global values_list
    # global added_list
    added_list = values_list[1]
    # Standard deviation of lines added
    added_sd = standard_deviations_list[1]
    added_scores = []
    username_accesser = 0
    list_length = len(github_data)
    # for ab in range(len(github_data)):
    for cd in range(len(github_data)):
        # print("Checking GitHub user: ", github_data[username_accesser][0])
        # This if/else calculates the amount added to the standard deviation,
        # in order to grade the team.
        # This if statment will end if the user was within 0.5 of the standard
        # deviation.
        if github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 0.5
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 0.5
        ):
            # print("appending 5 to added_scores list")
            added_scores.append(5)
            username_accesser += 1
        # This if statment will end if the user was within 1.0 of the standard
        #  deviation.
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 1.0
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 1.0
        ):
            # print("appending 4 to added_scores list")
            added_scores.append(4)
            username_accesser += 1
        # This if statment will end if the user was within 1.5 of the standard
        # deviation.
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 1.5
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 1.5
        ):
            # print("appending 3 to added_scores list")
            added_scores.append(3)
            username_accesser += 1
        # This if statment will end if the user was within 2.0 of the standard
        # deviation.
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 2.0
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 2.0
        ):
            # print("appending 2 to added_scores list")
            added_scores.append(2)
            username_accesser += 1
        # This if statment will end if the user was within 2.25 of the standard
        # deviation.
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 2.25
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 2.25
        ):
            # print("appending 1 to added_scores list")
            added_scores.append(1)
            username_accesser += 1
        else:
            # print("appending 0 to added_scores list")
            added_scores.append(0)
            username_accesser += 1
    global added_overall_score
    added_overall_score = np.average(added_scores)
    # The "''...'_percent" variables calculate the percentage score the team received for this category. These print statments print out the scores for the amount of code the team added
    added_percent = added_overall_score / 5
    added_percent = np.around(added_percent, decimals=2)
    print(
        "\nThe team earned a score of: [",
        np.average(added_scores),
        "/ 5] for teamwork on lines removed, or: ",
        "{:.2%}".format(added_percent),
        "\n",
    )


def removed_calculator():
    """This will determine how well the team worked together by analyzing the
    spread of lines of code removed"""
    global standard_deviations_list
    global values_list
    removed_list = values_list[2]
    # print("Lines removed average is: ", np.average(removed_list))
    # print("Lines removed standard deviation is: ", np.std(removed_list))
    # Standard deviation of lines removed
    removed_sd = standard_deviations_list[2]
    removed_scores = []
    username_accesser = 0
    list_length = len(github_data)
    for ef in range(len(github_data)):
        # print("Checking GitHub user: ", github_data[username_accesser][0])
        # This if/else calculates the amount of code removed to the,
        # standard deviation in order to grade the team.
        # Ths if statment will end if the user was within 0.5 of the standard
        # deviation.
        if github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 0.5
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 0.5
        ):
            # print("appending 5 to removed_scores list")
            removed_scores.append(5)
            username_accesser += 1
        # This if statment will end if the user was within 1.0 of the standard
        # deviation.
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 1.0
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 1.0
        ):
            # print("appending 4 to removed_scores list")
            removed_scores.append(4)
            username_accesser += 1
        # This if statment will end if the user was within 1.5 of the standard
        # deviation.
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 1.5
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 1.5
        ):
            # print("appending 3 to removed_scores list")
            removed_scores.append(3)
            username_accesser += 1
        # This if statment will end if the user was within 2.0 of the standard
        # deviation.
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 2.0
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 2.0
        ):
            # print("appending 2 to removed_scores list")
            removed_scores.append(2)
            username_accesser += 1
        # This if statment will end if the user was within 2.25 of the standard
        # deviation.
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 2.25
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 2.25
        ):
            # print("appending 1 to removed_scores list")
            removed_scores.append(1)
            username_accesser += 1
        else:
            # print("appending 0 to removed_scores list")
            removed_scores.append(0)
            username_accesser += 1
    global removed_overall_score
    removed_overall_score = np.average(removed_scores)
    # The "''...'_percent" variables calculate the percentage score the team received for this category. These print statments print out the numeric and percentage scores for the amount of code the team removed.
    removed_percent = removed_overall_score / 5
    removed_percent = np.around(removed_percent, decimals=2)
    print(
        "\nThe team earned a score of: [",
        np.average(removed_scores),
        "/ 5] for teamwork on lines removed, or: ",
        "{:.2%}".format(removed_percent),
        "\n",
    )


def total_team_score_calculator():
    """This will provide the overall score for how the team worked together"""
    # Adding the needed global variables for this function
    global commits_overall_score
    global added_overall_score
    global removed_overall_score
    global total_team_score
    # Performs a calculation to determine how the team performed
    # as a whole across the three metrics
    total_team_score = (
        commits_overall_score + added_overall_score + removed_overall_score
    )
    # This calculates whether the team is deserving of a bonus point.
    # Understanding that commit's may not be entirely indicative
    # of individual contribution, this measure is meant to
    # incentivize keeping the ratio of commits:lines_added
    # no more than 1:2. This also allows for one team member
    # to have contributed nothing, or have a higher ratio, and for
    # the team to still receive the bonus point. This is to
    # understand that teams may have members that do not contribute,
    # at no fault to teamwork dynamics.
    bonus_point = 0
    division_counter = 0
    global github_data
    for gh in range(len(github_data)):
        if github_data[division_counter][1] == 0:
            division_counter += 1
        elif (
            github_data[division_counter][1] / github_data[division_counter][2]
        ) <= 0.5:
            bonus_point += 1
            division_counter += 1
    if bonus_point >= len(github_data) - 1:
        total_team_score = total_team_score + 1
    else:
        pass
    # The following five lines of code provide the scoring information
    # output to the user.
    # print("Across these three metrics, the team earned a total score of: [", total_team_score, "/ 15]")
    total_team_percent = total_team_score / 15
    total_team_percent = np.around(total_team_percent, decimals=4)
    print(
        "Across these three metrics, the team earned a total score of: [",
        total_team_score,
        "/ 15], or: ",
        "{:.2%}".format(total_team_percent),
    )


if __name__ == "__main__":
    # Getting user input
    standard_deviations()
    print("Please enter what scores you would like to see.")
    score_wanted = input(
        "The options are: 'all', 'commits', 'added', and 'removed'.\n---\n"
    )
    if score_wanted == "all":
        # Sequential calls of the functions declared above to perform
        # the necessary calculations and provide the user with an overall
        # team evaluation.
        commits_calculator()
        added_calculator()
        removed_calculator()
        total_team_score_calculator()
        print("\n---\n")
    if score_wanted == "commits":
        commits_calculator()
        print("---\n")
    if score_wanted == "added":
        added_calculator()
        print("---\n")
    if score_wanted == "removed":
        removed_calculator()
        print("---\n")
