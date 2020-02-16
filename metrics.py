"""Determine how the well the team worked together"""

import numpy as np

# Uses the patter ["username", commit_total, lines_added, lines_deleted, issues_opened]
github_data = [
    ["cassidyt2", 28, 355, 76, 2],
    ["johnSmith", 22, 349, 50, 4],
    ["janeDoe", 23, 375, 30, 3],
    ["edgarAllenPoe", 27, 315, 75, 7],
    ["georgeWashington", 25, 360, 65, 10],
]
standard_deviations_list = []
commits_list = []
added_list = []
removed_list = []
commits_overall_score = 0
added_overall_score = 0
removed_overall_score = 0


def standard_deviations():
    commits_counter = 0
    global github_data
    global commits_list
    list_length = len(github_data)
    while commits_counter <= list_length - 1:
        # print(github_data[commits_counter][1])
        commits_list.append(github_data[commits_counter][1])
        commits_counter += 1
    print("")
    print("The total number of commits is: ", sum(commits_list))
    print("Standard deviation of the commits is: ", np.std(commits_list))
    print("")
    global standard_deviations_list
    standard_deviations_list.append(np.std(commits_list))
    # Beginning code for lines added
    lines_added_counter = 0
    global added_list
    while lines_added_counter <= list_length - 1:
        added_list.append(github_data[lines_added_counter][2])
        lines_added_counter += 1
    print("")
    print("The total number of lines added is: ", sum(added_list))
    print("Standard deviation of lines added is: ", np.std(added_list))
    print("")
    standard_deviations_list.append(np.std(added_list))
    # Beginning code for lines removed
    lines_removed_counter = 0
    global removed_list
    while lines_removed_counter <= list_length - 1:
        removed_list.append(github_data[lines_removed_counter][3])
        lines_removed_counter += 1
    print("")
    print("The total number of lines removed is: ", sum(removed_list))
    print("Standard deviation of lines removed is: ", np.std(removed_list))
    print("")
    standard_deviations_list.append(np.std(removed_list))
    print("")
    print("List of each standard deviation: ")
    print(standard_deviations_list)
    print("")


def commits_calculator():
    """This will determine how well the team worked together by analyzing the spread of commits"""
    global standard_deviations_list
    global commits_list
    print("Commits average is: ", np.average(commits_list))
    print("Commits SD is: ", np.std(commits_list))
    # Standard deviation of commits
    commits_sd = standard_deviations_list[0]
    commit_scores = []
    username_accesser = 0
    list_length = len(github_data)
    # for ab in range(len(github_data)):
    for ab in range(len(github_data)):
        # sd_check_counter = 0.5
        # print("Checking GitHub user: ",github_data[username_accesser][0])
        # print("Commits average is: ",np.average(commits_list))
        # print("GitHub user ", github_data[username_accesser][0], " made ", github_data[username_accesser][1], " commits.")
        # print("Average + 2.0 SD's is: ", np.average(commits_list)+(commits_sd*2.0))
        # print("Average - 2.0 SD's is: ", np.average(commits_list)-(commits_sd*2.0))
        # print("")
        # print("")
        if github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 0.5
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 0.5
        ):
            print("appending 5 to commit_scores list")
            commit_scores.append(5)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 1.0
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 1.0
        ):
            print("appending 4 to commit_scores list")
            commit_scores.append(4)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 1.5
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 1.5
        ):
            print("appending 3 to commit_scores list")
            commit_scores.append(3)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 2.0
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 2.0
        ):
            print("appending 2 to commit_scores list")
            commit_scores.append(2)
            username_accesser += 1
        elif github_data[username_accesser][1] <= np.average(commits_list) + (
            commits_sd * 2.5
        ) and github_data[username_accesser][1] >= np.average(commits_list) - (
            commits_sd * 2.5
        ):
            print("appending 1 to commit_scores list")
            commit_scores.append(1)
            username_accesser += 1
        else:
            print("Appending 0 to commit_scores list")
            commit_scores.append(0)
            username_accesser += 1
    global commits_overall_score
    commits_overall_score = np.average(commit_scores)
    print("")
    print("Each users scores are listed below: ")
    print(commit_scores)
    print("The average of these scores is: ", np.average(commit_scores))
    print(
        "The team earned a score of: [",
        np.average(commit_scores),
        "/ 5] for teamwork on commits.",
    )
    print("")


def added_calculator():
    """This will determine how well the team worked together by analyzing the spread of lines of code added"""
    global standard_deviations_list
    global added_list
    print("Lines added average is: ", np.average(added_list))
    print("Commits SD is: ", np.std(added_list))
    # Standard deviation of commits
    added_sd = standard_deviations_list[0]
    # Standard deviation of lines added
    added_sd = standard_deviations_list[1]
    # Standard deviation of lines removed
    removed_sd = standard_deviations_list[2]
    # max_sd_multiplier = 2.5
    added_scores = []
    username_accesser = 0
    list_length = len(github_data)
    # for ab in range(len(github_data)):
    for ab in range(len(github_data)):
        # sd_check_counter = 0.5
        # print("Checking GitHub user: ",github_data[username_accesser][0])
        # print("Lines added average is: ",np.average(added_list))
        # print("GitHub user ", github_data[username_accesser][0], " made ", github_data[username_accesser][2], " additions.")
        # print("Average + 2.0 SD's is: ", np.average(added_list)+(added_sd*2.0))
        # print("Average - 2.0 SD's is: ", np.average(added_list)-(added_sd*2.0))
        # print("")
        # print("")
        if github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 0.5
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 0.5
        ):
            print("appending 5 to added_scores list")
            added_scores.append(5)
            username_accesser += 1
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 1.0
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 1.0
        ):
            print("appending 4 to added_scores list")
            added_scores.append(4)
            username_accesser += 1
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 1.5
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 1.5
        ):
            print("appending 3 to added_scores list")
            added_scores.append(3)
            username_accesser += 1
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 2.0
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 2.0
        ):
            print("appending 2 to added_scores list")
            added_scores.append(2)
            username_accesser += 1
        elif github_data[username_accesser][2] <= np.average(added_list) + (
            added_sd * 2.5
        ) and github_data[username_accesser][2] >= np.average(added_list) - (
            added_sd * 2.5
        ):
            print("appending 1 to added_scores list")
            added_scores.append(1)
            username_accesser += 1
        else:
            print("Appending 0 to added_scores list")
            added_scores.append(0)
            username_accesser += 1
    global added_overall_score
    added_overall_score = np.average(added_scores)
    print("")
    print("Each users scores are listed below: ")
    print(added_scores)
    print("The average of these scores is: ", np.average(added_scores))
    print(
        "The team earned a score of: [",
        np.average(added_scores),
        "/ 5] for teamwork on lines added.",
    )
    print("")


def removed_calculator():
    """This will determine how well the team worked together by analyzing the spread of lines of code removed"""
    global standard_deviations_list
    global removed_list
    print("Lines removed average is: ", np.average(removed_list))
    print("Lines removed SD is: ", np.std(removed_list))
    # Standard deviation of lines removed
    removed_sd = standard_deviations_list[2]
    # max_sd_multiplier = 2.5
    removed_scores = []
    username_accesser = 0
    list_length = len(github_data)
    # for ab in range(len(github_data)):
    for ab in range(len(github_data)):
        # sd_check_counter = 0.5
        # print("Checking GitHub user: ",github_data[username_accesser][0])
        # print("Lines added average is: ",np.average(removed_list))
        # print("GitHub user ", github_data[username_accesser][0], " made ", github_data[username_accesser][2], " additions.")
        # print("Average + 2.0 SD's is: ", np.average(removed_list)+(removed_sd*2.0))
        # print("Average - 2.0 SD's is: ", np.average(removed_list)-(removed_sd*2.0))
        # print("")
        # print("")
        if github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 0.5
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 0.5
        ):
            print("appending 5 to removed_scores list")
            removed_scores.append(5)
            username_accesser += 1
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 1.0
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 1.0
        ):
            print("appending 4 to removed_scores list")
            removed_scores.append(4)
            username_accesser += 1
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 1.5
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 1.5
        ):
            print("appending 3 to removed_scores list")
            removed_scores.append(3)
            username_accesser += 1
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 2.0
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 2.0
        ):
            print("appending 2 to removed_scores list")
            removed_scores.append(2)
            username_accesser += 1
        elif github_data[username_accesser][3] <= np.average(removed_list) + (
            removed_sd * 2.5
        ) and github_data[username_accesser][3] >= np.average(removed_list) - (
            removed_sd * 2.5
        ):
            print("appending 1 to removed_scores list")
            removed_scores.append(1)
            username_accesser += 1
        else:
            print("Appending 0 to removed_scores list")
            removed_scores.append(0)
            username_accesser += 1
    global removed_overall_score
    removed_overall_score = np.average(removed_scores)
    print("")
    print("Each users scores are listed below: ")
    print(removed_scores)
    print("The average of these scores is: ", np.average(removed_scores))
    print(
        "The team earned a score of: [",
        np.average(removed_scores),
        "/ 5] for teamwork on lines removed.",
    )
    print("")


def total_team_score_calculator():
    """This will provide the overall score for how the team worked together"""
    global commits_overall_score
    global added_overall_score
    global removed_overall_score
    total_team_score = (
        commits_overall_score + added_overall_score + removed_overall_score
    )
    # total_team_score = round(total_team_score_calculator, 2)
    print("Altogether, across these three metrics, the team earned a total score of:")
    print("[", total_team_score, "/ 15]")
    # total_team_score_calculator = str(round(total_team_score_calculator, 2))
    total_team_percent = total_team_score / 15
    total_team_percent = np.around(total_team_percent, decimals=4)
    print("{:.2%}".format(total_team_percent))


if __name__ == "__main__":
    standard_deviations()
    commits_calculator()
    added_calculator()
    removed_calculator()
    total_team_score_calculator()
