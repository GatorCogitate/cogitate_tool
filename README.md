# cogitate_tool

[![Build Status](https://travis-ci.com/GatorCogitate/cogitate_tool.svg?branch=master)](https://travis-ci.com/GatorCogitate/cogitate_tool)
[![codecov](https://codecov.io/gh/GatorCogitate/cogitate_tool/branch/master/graph/badge.svg)](https://codecov.io/gh/GatorCogitate/cogitate_tool)

## Table of Contents

## About the cogitate_tool

## Installing the cogitate_tool

## Testing the cogitate_tool

## Running the cogitate_tool

## Contributors


### 1. File Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── .travis.yml
├── .gitignore
|
├── data
│   ├── demofile.json
│   └── testfile.json
|
├── scripts
│   ├── cogitate.sh
│   └── test.sh
├── src
│   ├── cogitate.py
│   ├── data_collection.py
│   ├── data_processor.py
│   ├── driller.py
│   ├── json_handler.py
│   └── __init__.py
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── test_json_handler.py
    └── test_driller.py

```

### 2. How to Use

#### 2.1 How To Install Packages

After pulling the repo, use `pipenv shell` in `cogitate_tool/` to enter the virtual
environment. Use `exit` to exit. Under the virtual environment, use
`pipenv install <package_name> --dev` to install new packages for development.

Here is a good [tutorial](https://realpython.com/pipenv-guide/) on how to use `pipenv`.

When under development, always install the virtual environment first by using
`pipenv install --dev`, then run the developing program by using
`pipenv run python program_name`.

#### 2.2 How to setup scripts

The purpose of script is to automate the running or testing process. To make the
scripts take effect, add the following code to the `Pipfile`:

```
[scripts]
command_name = "./scripts/script_name.sh"
```

Here the `command_name` is the command you want to use when running the project.
For example, if the `command_name` is `cogitate`, the we can use `pipenv run cogitate`.

### 3. CLI

The [homepage](https://docs.python.org/3/howto/argparse.html) for `argparse`.

- `-l` or `--link` Cogitate a repo by the url of the repo.
- `-t` or `--token` Github user token.
- `-r` or `--repo` User's repository.
- `-s` or `--state` State of the issue.

### 4. PyDriller

The [homepage](https://github.com/ishepard/pydriller) and [documentation](https://pydriller.readthedocs.io/en/latest/intro.html)
for `PyDriller`.

The available attributes can be found at their homepage.

## Steps to print out table

- Must be in the `cogitate_tool` folder.
- Before you run the program make sure you have installed the dev packages.
- Run the following command `pipenv run python src/data_collection.py`
- Enter the name of the `.json` you would like to write the data to.
- If you want to use the current repository press `ENTER`, otherwise enter URL/path
  to other repository.
