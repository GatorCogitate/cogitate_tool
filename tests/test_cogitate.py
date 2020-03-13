""" Test suite for the command line interface functions in cogitate.py. """

import random
import string
import subprocess
from subprocess import PIPE
import pytest
from src import cogitate


@pytest.mark.parametrize("valid_input", ["https://allegheny.edu"])
def link_validator_valid_url(valid_input):
    assert cogitate.link_validator(valid_input) is True


@pytest.mark.parametrize("invalid_input", ["thisShouldNotPass"])
def link_validator_invalid_str(invalid_input):
    assert cogitate.link_validator(invalid_input) is not True


@pytest.mark.parametrize(
    "true_string, false_string",
    [("t", "f"), ("True", "False"), ("yes", "no"), ("Y", "N")],
)
def test_bool_validator_xpass(true_string, false_string):
    assert cogitate.bool_validator(true_string)
    assert not cogitate.bool_validator(false_string)


@pytest.mark.parametrize(
    "run_arguments_dict, correct_args",
    [
        (
            [
                "pipenv",
                "run",
                "python",
                "src/cogitate.py",
                "-l",
                "https://github.com/GatorCogitate/cogitate_tool",
                "-t",
                "test_token",
                "-r",
                "GatorCogitate/cogitate_tool",
                "-rm",
                "n",
                "-b",
                "5",
                "-a",
                "10",
                "-wi",
                "2",
                "-s",
                "open",
                "-w",
                "y",
                "-m",
                "i",
                "-twpa",
                "y",
            ],
            "link : https://github.com/GatorCogitate/cogitate_tool\r\n"
            + "token : test_token\r\n"
            + "repo : GatorCogitate/cogitate_tool\r\nrunmerge : n\r\n"
            + "below : 5.0\r\nabove : 10.0\r\nwithin : 2.0\r\nstate : open\r\n"
            + "web : True\r\nmetric : i\r\ntestwithprintargs : y\r\n",
        ),
        (
            [
                "pipenv",
                "run",
                "python",
                "src/cogitate.py",
                "-l",
                "https://github.com/GatorCogitate/cogitate_tool",
                "-t",
                "test_token",
                "-r",
                "GatorCogitate/cogitate_tool",
                "-rm",
                "n",
                "-twpa",
                "y",
            ],
            "link : https://github.com/GatorCogitate/cogitate_tool\r\n"
            + "token : test_token\r\n"
            + "repo : GatorCogitate/cogitate_tool\r\nrunmerge : n\r\n"
            + "below : 0.2\r\nabove : 0.2\r\nwithin : 0.6\r\nstate : all\r\n"
            + "web : False\r\nmetric : both\r\ntestwithprintargs : y\r\n",
        ),
    ],
)
def test_retrieve_arguments(run_arguments_dict, correct_args, capsys):
    """
    Test run first with values for all possible arguments and then for all
    required arguments with unrequired arguments checked for their default values
    """
    call = subprocess.run(run_arguments_dict, stdout=PIPE)
    args = call.stdout.decode("utf-8")
    assert args == correct_args


@pytest.mark.parametrize(
    "invalidToken",
    ["".join([random.choice(string.ascii_letters + string.digits) for n in range(15)])],
)
def test_terminal_output_invalid_token(invalidToken, capsys):
    """ Test correct output is produced with an invalid access token. """
    result = subprocess.run(
        [
            "pipenv",
            "run",
            "python",
            "src/cogitate.py",
            "-l https://github.com/GatorCogitate/cogitate_tool",
            "-t",
            invalidToken,
            "-r GatorCogitate/cogitate_tool",
            "-rm y",
        ],
        stderr=subprocess.PIPE,
    )
    stringResult = result.stderr.decode("utf-8")
    assert stringResult == "Cannot authenticate repository."


def test_terminal_output_req_arg(capsys):
    result = subprocess.run(
        ["pipenv", "run", "python", "src/cogitate.py", ], stderr=subprocess.PIPE,
    )
    stringResult = result.stderr.decode("utf-8")
    assert "cogitate.py: error: the following arguments are required:" in stringResult
