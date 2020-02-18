# cogitate_tool_lines

#### Steps to run `count_code_lines.py`

- Must be in the `src` folder
- Run the python file using `pipenv run python count_code_lines.py`
- Paste the URL or local path of the repository
- If the current repository is meant to be selected, enter `../` as the path. This will cause the program to take the directory right outside of the `src` folder
- __NOTE__: the program only displays statistics for the default master branch of the repository if run using repository URL. However, it would display the checked out branch statistics if the local path was provided. This is a current limitation of pydriller

#### Run the test suite

- Must be in the main folder outside of the tests folder
- Run test suite using the command: `pipenv run test`
- __NOTE__: The test case will take the current repository as a default unless that path variable is changed in the `test_count_code_lines.py` file.
