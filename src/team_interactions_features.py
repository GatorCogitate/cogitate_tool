""" Features to measure code hoarding and common collaborations in branches. """

""" Method to determine code hoarders. """

""" Method to determine frequent collaborators in a team project. """
# will add a feature to have user define this value
user_collaboration_max = 5
# populate array with input text
sampleData = open("branch_info_input.txt", "r")
dataCollect = list(sampleData.read())
sampleData.close()
