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
`pipenv run python 'program_name'`.

#### 2.2 How To Setup Scripts

The purpose of script is to automate the running or testing process. To make the
scripts take effect, add the following code to the `Pipfile`:

```
[scripts]
command_name = "./scripts/script_name.sh"
```

Here the `command_name` is the command you want to use when running the project.
For example, if the `command_name` is `cogitate`, the we can use `pipenv run cogitate`.

#### 2.3 The Parameters

##### Token

* Datatype: String
* Required: True
* Flag: `-t` or `--token`

The purpose of a token in this context provides an alternate passwords that you
can use to authenticate. The personal access tokens with Git allows you to authenticate
with a token in place of your password. This is vital for our tool because it
allows the user to be used for HTTPS Git operations.

* How To Generate a token

The following will demonstrate step by step the process to generate a token in
order to use the tool:
  1. Cick your profile icon on GitHub and then click Settings
  2. On the sidebar, click the Developer settings and then Personal access tokens.
  3. Click Generate new token.
  4. Add a token description and click Generate token.
  5. Save the token for future use.

Do note that for security reasons, you will not be able to see the token again
once logged off.

##### Link

* Datatype: String
* Required: True
* Flag: `-l` or `--link`

The link is the URL of the targeted repository in GitHub. This can be find at
GitHub website.

##### Repo

* Datatype: String
* Required: True
* Flag: `-r` or `--repo`

The repo is the targeted repository name. It includes the root part and the
name part. The root part is the username or organization name. The name part is
the actual name of the repository. In our case, it would be `GatorCogitate/cogitate_tool`

##### Delete Username

* Datatype: String
* Required: True
* Flag: `-du` or `--deleteusername`

Username that is merged into the kept username, then deleted.

##### Kept Username

* Datatype: String
* Required: True
* Flag: `-ku` or `--keptusername`

Username that is kept into the merged username, then deleted.

##### End Merge

* Datatype: String
* Required: True
* Flag: `-em` or `--endmerge`

Ends the process of merging usernames.

##### State

* Datatype: String
* Required: False
* Default: `both`

State of the Issue, open or closed.

##### Web

* Datatype: String
* Required: False
* Default: False

Whether to show the detailed result in web interface.

### 3. CLI

The [homepage](https://docs.python.org/3/howto/argparse.html) for `argparse`.

The available attributes can be found at their homepage.

* `-l` or `--link` Cogitate a repo by the url of the repo.
* `-t` or `--token` Github user token.
* `-r` or `--repo` User's repository.
* `-s` or `--state` State of the issue.

### 4. PyDriller

The [homepage](https://github.com/ishepard/pydriller) and [documentation](https://pydriller.readthedocs.io/en/latest/intro.html)
for `PyDriller`.

The available attributes can be found at their homepage.

## Steps to print out table

* Must be in the `cogitate_tool` folder.
* Before you run the program make sure you have installed the dev packages.
* Run the following command `pipenv run python src/data_collection.py`
* Enter the name of the `.json` you would like to write the data to.
* If you want to use the current repository press `ENTER`, otherwise enter URL/path
  to other repository.
