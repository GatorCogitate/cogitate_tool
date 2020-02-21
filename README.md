# cogitate_tool

Tool to analyze contributions when working in a team.

## About the Feature

The Feature 1 tool was built with the purpose of trying to determine if there
was a student within the group who was only writing test cases. The tool pydriller
to retrieve information regarding commits from any repository and the program will
scan through looking for the word "test". The program will display the following
information.

- Authors within the repository
- List the various commits by an individual
- What files that individual edited
- How many commits contain the fragment "test"
- The number of commits by the individual
- The percentage of the commits went towards testing

## To Use the Tool

It is essential that anyone who wishes to utilize this tool has the following
downloaded and functional on their device:

- pydriller

Pydriller can be installed to a device by searching for "pydriller" in GitHub
and following the installation steps or by using the link below.
https://github.com/ishepard/pydriller

## Running the Tool

This tool requires a path to a repository in order for the desired information to
be outputted. This means either a URL or a local path. The program is most
functional with master branches of repositories, as the output that is produced
with a path to a sub-branch is unpredictable. The command that will run this tool
is - python3 test_commits.py .
