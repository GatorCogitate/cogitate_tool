
![Cogitate Logo](/images/logo.png)
[![Build Status](https://travis-ci.com/GatorCogitate/cogitate_tool.svg?branch=master)](https://travis-ci.com/GatorCogitate/cogitate_tool)
[![codecov](https://codecov.io/gh/GatorCogitate/cogitate_tool/branch/master/graph/badge.svg)](https://codecov.io/gh/GatorCogitate/cogitate_tool)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

# About GatorCogitate

Cogitate is a free and open source tool written in Python. It is designed to
evaluate the level of contributions for members of a GitHub repository. GatorCogitate
generates a score for members based on a variety of metrics including:

- Lines Added
- Lines Removed
- Lines Deleted
- Pull Requests
- Issue Tracker
- Teamwork Performance

These metrics are combined into an overall score for the user.

*Note: This tool is alpha software. Please contact us if you intend to run it in
production.*

## Installing GatorCogitate

**1. Clone the GatorCogitate source code onto your machine.**

With HTTPS:

```
git clone https://github.com/GatorCogitate/cogitate_tool.git
```

Or with SSH:

```
git clone git@github.com:GatorCogitate/cogitate_tool.git
```

**2. Install Pipenv (Recommended)**
Documentation for installing pipenv can be found [Here.](https://pipenv.kennethreitz.org/en/latest/#install-pipenv-today)
After pulling the repo, use `pipenv shell` in `cogitate_tool/` to enter the virtual
environment. Use `exit` to exit. Under the virtual environment, use
`pipenv install <package_name> --dev` to install new packages for development.
Otherwise use `pipenv install --dev` to install all dependencies.

Here is a good [tutorial](https://realpython.com/pipenv-guide/) on how to use `pipenv`.

Alternatively, all dependencies will need to be installed locally with the commands:

```
python3 -m pip install --upgrade pip
python3 -m pip install -e
```

## Running GatorCogitate

GatorCogitate uses `argparse` which allows a user to make arguments during program
execution. The required arguments for the tool are as follows:

- `-t, --token`: Input a Github user token to allow `Pygithub` access to information
  such as the Issue Tracker.
- `-r, --repo`: Input the GitHub Repository name (`username/repo_name`).

Run the command `pipenv run python src/cogitate.py -t [GitHub Token] -r [Path]`
in the root directory.
Check out `cogitate.py` to see additional arguments that can be used..

*Note: Any users that do not wish to develop the tool can stop reading here.*

### Development Info

#### 2.1 How To Install Packages

When under development, always install the virtual environment first by using
`pipenv install --dev`, then run the developing program by using
`pipenv run python program_name`.

#### 2.2 How to setup scripts

The purpose of script is to automate the running or testing process. To make the
scripts take effect, add the following code to the `Pipfile`:

```
[scripts]
command_name = “./scripts/script_name.sh”

```

Here the `command_name` is the command you want to use when running the project.
For example, if the `command_name` is `cogitate`, the we can use `pipenv run cogitate`.

### 3. Command Line Interface

The [homepage](https://docs.python.org/3/howto/argparse.html) for `argparse`.

The available attributes can be found at their homepage.

- `-l` or `--link` Cogitate a repo by the url of the repo.
- `-t` or `--token` Github user token.
- `-r` or `--repo` User's repository.
- `-rm` `-runmerge` (y/n).
- `-s` or `--state` State of the issue.

#### CLI Parameters

##### Token

- Datatype: String
- Required: True
- Flag: `-t` or `--token`

The purpose of a token in this context provides an alternate passwords that you
can use to authenticate. The personal access tokens with Git allows you to authenticate
with a token in place of your password. This is vital for our tool because it
allows the user to be used for HTTPS Git operations.

- How To Generate a token

The following will demonstrate step by step the process to generate a token in
order to use the tool:

1. Click your profile icon on GitHub and then click Settings.

1. On the sidebar, click the Developer settings and then Personal access tokens.

1. Click Generate new token.

1. Add a token description and click Generate token.

1. Save the token for future use.

Do note that for security reasons, you will not be able to see the token again
once logged off.

##### Link

- Datatype: String
- Required: True
- Flag: `-l` or `--link`

The link is the URL of the targeted repository in GitHub. This can be found at
the GitHub website.

##### Repo

- Datatype: String
- Required: True
- Flag: `-r` or `--repo`

The repo is the targeted repository name. It includes the root part and the
name part. The root part is the username or organization name. The name part is
the actual name of the repository. In our case, it would be `GatorCogitate/cogitate_tool`

##### Run Merge

- Datatype: String
- Required: True
- Flag: `-rm` or `--runmerge`

Determines if the process of merging duplicate Github usernames will be run,
based on the user's input.

##### Below

- Datatype: Float
- Required: True
- Flag: `-b` or `--below`

Determines lower weight.

##### Above

- Datatype: Float
- Required: True
- Flag: `-a` or `--above`

Determines higher weight.

##### Within

- Datatype: Float
- Required: True
- Flag: `-wi` or `--within`

Determines value within weight.

##### State

- Datatype: String
- Required: False
- Default: `both`
- Flag: `-s` or `--state`

State of the Issue: open, closed, or all.

##### Web

- Datatype: String
- Required: False
- Default: False
- Flag: `-w` or `--web`

Determines if the detailed results of the tool's calculations will be shown in
the web interface, based on the user's input.

##### Metric

- Datatype: String
- Required: False
- Default: `both`
- Flag: `-m` or `--metric`

Invokes calculation of team or individual metrics. If not specified, both are run.

### 4. PyDriller

The [homepage](https://github.com/ishepard/pydriller) and [documentation](https://pydriller.readthedocs.io/en/latest/intro.html)
for `PyDriller`.

The available attributes can be found at their homepage.

## Limitations of GatorCogitate

GatorCogitate is a tool that allows a user to determine how well both individuals
and teams are contributing to a GitHub repository. This tool offers a lot of great
features, but currently has some limitations that the developers would like users
to be aware of.

- Currently GatorCogitate determines an individuals contribution as a
  percentage of their contribution to the overall total of a certain metric. For
  individuals who commit the `.gitignore` and `pipfile.lock` files, their
  contribution for lines added will most likely be much higher than their
  teammates. Please be aware that high amounts of lines of code added could be due
  to generated files.

- The tools that the developers have used for accessing data from GitHub offer a
  lot of possibilites for information mining. GatorCogitate does
  utilize some of these possibilites, but not all. At this time, not all
  information about **all** aspects of a GitHub repositiory will be
  available with GatorCogitate.

- GatorCogitate gives information about which files and file formats an
  invidiual edits. The file formats are not completely comprehensive,
  but do give an idea of what types of files a team member worked on in
  a GitHub repository.

## Future Development

The developers would like to develop even more features to our tool in the future.
These ideas include:

- Allow the user to determine which branch of their GitHub repository they would
  like to analyze.

- Include the dates of commits in returned information, which would allow the
  filtration of data in a timeline.

- Create line graphs which display commits over time to allow a user to see daily
  or weekly contribution for each individual in a team.

- Give information to the user regarding comments; including how many comments are
  in a file, and also how many comments are written per commit, and the ratio of
  comments to lines of source code.

- Continue refactoring our tool to reduce limitations and improve both efficiency
  and run time.

## Contacting the Developers

### IssueTracker

The role of an issue is to starting a conversation or a discussion. Issues
are located within the GitHub Issue tracker, which is where developers discuss
changes or problems related to the project. If you see an open issue that you want
to tackle, quickly comment on the issue to let others know you’re working on a
solution. Therefore, people are less likely to duplicate your work.

**An issue is usually opened under the following circumstances:**

- Reporting an error you can’t solve yourself.

- Discussing a high-level topic.

- Proposing a new feature or necessary change.

**Tips for effective communication:**

- Keep requests short and direct.

- Give context.

- Ask questions.

- Respect decisions.

### Pull Request Process

A pull request is created by a contributor to propose and collaborate on given
updates to a repository. Once a branch or issue is created and the changes are
committed, the creation of a pull request is needed, in order to receive feedback
on the proposed changes.

- To create a pull request that is ready for review, click "Create Pull Request".

- Once a pull request is opened, you can discuss and review the potential changes.

- If the developer is satisfied with the proposed changes, the PR will be merged.

Note: Anyone with push access to the repository can complete the merge. Ultimately,
a pull request is utilized to submit a working solution.
