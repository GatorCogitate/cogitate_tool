# cogitate_tool
Tool to analyze contributions when working in a team.

## Run FastAPI
* Install the pipfile dependencies `pip install pipenv --user` and `pipenv install --dev`
* Run the command `uvicorn demo:app --reload
`
* Please note that `demo` stands for the python file name and `app` stands for the name of the FastAPI object created
* Click on `http://127.0.0.1:8000 ` to see the results of the function created
* Add /docs to the end so it looks like `http://127.0.0.1:8000/docs`
* Click on the blue button named `GET`
* Click on `Try it out`
* Paste your GitHub user token in the parameter box
* Tokens can be generated on GitHub, steps shown [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line#creating-a-token)
* Click on execute, the results will show a list and number of your github repos
