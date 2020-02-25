from github import Github

# Using an access token
# Insert newly developed access token in quotations
g = Github("")

# Get and welcome the current user.
user = g.get_user()
print("\nWelcome back: \n" + user.name + ", " + user.login + ".")

# Search user by name.
user1 = g.get_user("santacruzm")
user2 = g.get_user("Jordan-A")
user3 = g.get_user("cklima616")
user4 = g.get_user("JMilamber")
user5 = g.get_user("chachtel1")

print("\nResearch Team Names Found: \n")
print(user1.name)
print(user2.name)
print(user3.name)
print(user4.name)
print(user5.name)

# Access team repository.
teamRepo = g.get_repo("GatorCogitate/cogitate_tool")
print("\nTeam Repository:\n" + teamRepo.name)

# Output current repository.
print("\nCurrent Repository Name: \n" + teamRepo.name)

# Return labels in repository.
labels = teamRepo.get_labels()
print("\n Labels: \n")
for label in labels:
    print(label)

# list open issues.
open_issues = teamRepo.get_issues(state="open")
print("\nOpen Issues in Team Repository: \n")
for issue in open_issues:
    print(issue)

# Get a specific issue.
print("PyGithub issue tracker")
print(teamRepo.get_issue(number=2))

# list branches in team repository.
print("\nBranches in Team Repository:\n")
print(list(teamRepo.get_branches()))

# Get the number of views and breakdown for the past two weeks.
contents = teamRepo.get_views_traffic()
contents = teamRepo.get_views_traffic(per="week")
print("\nNumber of views: \n")
print(contents)

# Get the milestone list.
open_milestones = teamRepo.get_milestones(state="open")
print("\nMilestone List: \n")
for milestone in open_milestones:
    print(milestone)

# Get the number of clones for the last two weeks.
contents = teamRepo.get_clones_traffic()
contents = teamRepo.get_clones_traffic(per="week")
print("\n Number of clones: \n")
print(contents)

# Get all contents of the root directory of repository.
contents = teamRepo.get_contents("")
print("\nRepository Contents: \n")
for content_file in contents:
    print(content_file)

# Print out the contents of a file.
contents = teamRepo.get_contents("README.md")
print("\n")
print(contents)
