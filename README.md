# cogitate_tool

## Development Doc

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

## Steps to run `Cogitate Tool`
- Must be in the `cogitate_tool` folder.
- Before you run the program make sure you have installed the dev packages.
- Run the following command `pipenv run python src/print_table.py`
- Enter the following `contributor_data_template`
- If you want to use the current repository use `../`.


## Steps to run `individual_metrics.py`

- Must be in the `src` folder
- Run the python file using `pipenv run python print_table.py`
- Paste the URL or local path of the repository
- If the current repository is meant to be selected, enter `../` as the path.
    This will cause the program to take the directory right outside of the
    `src` folder

## Run the test suite

- Must be in the main folder `cogitate_tool` not in the tests folder
- Run test suite using the command: `pipenv run test`
