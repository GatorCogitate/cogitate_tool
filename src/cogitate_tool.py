""" Command Line Interface for interacting with Github repository info. """
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from data_collection import collect_commits
from driller import find_repositories
from pprint import pprint


def CL_interface():
    """ Command Line Interface using methods from other classes. """
    # Define the style of the interface
    style = style_from_dict(
        {
            Token.Separator: "#cc5454",
            Token.QuestionMark: "#673ab7 bold",
            Token.Selected: "#cc5454",  # default
            Token.Pointer: "#673ab7 bold",
            Token.Instruction: "",  # default
            Token.Answer: "#f44336 bold",
            Token.Question: "",
        }
    )

    # Prompt for user

    questions = [
        {
            "type": "checkbox",
            "message": "Informative messages",
            "name": "name_of_the_dictionary",
            "choices": [
                Separator("= Question 1 ="),
                {"name": "Option1"},
                {"name": "Option2"},
                {"name": "Option3"},
            ],
            "validate": lambda answer: "You must choose at least one."
            if len(answer) == 0
            else True,
        },
        {
            "type": "password",
            "message": "Please enter your password",
            "name": "user_pswd",
            "validate": lambda pswd: "You must enter a pasword."
            if len(pswd) == 0
            else True,
        },
        {
            "type": "input",
            "message": "Please enter your name: ",
            "name": "user_name",
            "validate": lambda name: "You must enter a name."
            if len(name) == 0
            else True,
        },
        {
            "type": "input",
            "message": "Please enter your repository URL: ",
            "name": "user_repo",
            "validate": lambda url: "You must enter a repositroy URL."
            if len(url) == 0
            else True,
        },
    ]
    answers = prompt(questions, style=style)
    # inspect output
    print(answers)
    return answers


if __name__ == "__main__":
    answers_dict = CL_interface()
    pprint(collect_commits())
    print()
    pprint(find_repositories(answers_dict["user_repo"]))
