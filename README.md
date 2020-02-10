# cogitate_tool
Tool to analyze contributions when working in a team.

## Run FastAPI
* Install the pipfile dependencies `pip install pipenv --user` and `pipenv install --dev`
* Run the command `uvicorn demo:app --reload`
* You will be prompted to either call main in the terminal window or proceed to the FastAPI process
* Please note that `demo` stands for the python file name and `app` stands for the name of the FastAPI object created
* Click on `http://127.0.0.1:8000 ` to see the results of the function created
* Add /docs to the end so it looks like `http://127.0.0.1:8000/docs`
* There are three different functions you can choose from, you __must__ choose them in the order displayed
* For first function `create_user`:
  * Click on the blue button named `GET`
  * Click on `Try it out`
  * Paste your GitHub user token in the parameter box
  * Tokens can be generated on GitHub, steps shown [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line#creating-a-token)
  *   Make sure to give the token repository access
  * Click on `execute`
  * The results will show you the message `username created successfully!`
* For second function `get_repo_list`:
  * Click on the blue button named `GET`
  * Click on `Try it out`
  * Click on execute
  * The result is a list of your repositories' names
* For third function `get_repo_info`:
  * Click on the blue button named `GET`
  * Click on `Try it out`
  * Enter the number of any repository from the list (ex: `cogitate_tool` number is 33)
  * Click on execute
  * The result is a list of the names of every branch in that repository
