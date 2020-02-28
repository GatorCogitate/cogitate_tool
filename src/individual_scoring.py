# For 3/3/2020:
# TODO Fake data - start with dictionary - Madelyn *
# TODO function for commit score - Teona *
# TODO function for added lines score - Teona *
# TODO function for deleted lines - Wonjoon *
# TODO lines modified score - Madelyn *
# TODO lines per commit score - Wonjoon *
# TODO amount of files modified overall score - Madelyn *
# TODO file for printing the individual score - Teona *
# TODO average of all scores - Everyone, once other features are finished

# Possible other features or scoring metrics:
# TODO amount of files per commit score
# TODO talk about using PyGithub to retrieve issue data
# TODO amount of comments in lines of code score - research tools for parsing
# TODO date distribution score
# TODO average overall score and individual score to produce new individual score
# TODO give notification of duplicate username if there is one, or the possibility
# User inputs the weight for each category for finding total individual score

# Helpful reminders:
# Use pipeline programming style
# Implement test cases as functions are written in the test_individual_scoring.py file
# Scoring will be done first as percentages ((individual contribution/total branch)*100)

# Add fake data that corresponds to overall-eval-analyzing-metrics branch
# github_data uses the pattern ["username", commit_total, lines_added,
# lines_deleted, total_lines, modified_lines, lines_per_commit, files_changed]
github_data = {
    "WonjoonC": [28, 355, 76, 2],
    "Hannah Schultz": [22, 349, 50, 4],
    "Jordan-A": [23, 375, 30, 3],
    "noorbuchi": [27, 315, 75, 7],
    "bagashvilit": [25, 360, 65, 10],
    "Alexander_Hamilton": [41, 530, 100, 230],
    "Karl_Marx": [0, 0, 0, 400],
    "Julius_Caesar": [25, 310, 68, 1],
    "Napoleon_Bonaparte": [24, 363, 70, 3],
    "Alexander_the_Great": [42, 540, 110, 1],
}

github_data1 = {
"noorbuchi" : {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"bagashvilit" : {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Jordan-A" : {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"WonjoonC": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Hannah Schultz": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Alexander_Hamilton": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Karl_Marx": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Julius_Caesar": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Napoleon_Bonaparte": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
"Alexander_the_Great": {"EMAIL": email, "COMMITS" : total_commits, "ADDED" : total_added_lines, "REMOVED" : total_removed_lines},
}
