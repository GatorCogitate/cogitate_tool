""" Test suite for the command line interface functions in cogitate.py. """

import random
import string
import subprocess
from subprocess import PIPE
import pytest
from src import cogitate
from src import data_collection


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
    "non_url_value",
    ["https://5", "https://fgh", "https://?", "https://~~~", "https://y5"],
)
def test_link_validator_raise_argparse_error(non_url_value, capsys):
    result = subprocess.run(
        [
            "pipenv",
            "run",
            "python",
            "src/cogitate.py",
            "-l", non_url_value,
            "-t", "token",
            "-r", "GatorCogitate/cogitate_tool",
            "-rm", "n",
        ],
        stderr=subprocess.PIPE,
    )
    stringResult = result.stderr.decode("utf-8")
    assert "cogitate.py: error: argument -l/--link " and non_url_value and "is not an URL" in stringResult


@pytest.mark.parametrize(
    "non_url_value",
    ["https://github.com", "https://github.com/affsadf", "https://github.com/?",
     "https://github.com/~~~", "https://github.com/y5"],
)
def test_link_validator_valid_link_invalid_repo(non_url_value, capsys):
    token = data_collection.retrieve_token("data/token.txt")
    try:
        result = subprocess.run(
            [
                "pipenv",
                "run",
                "python",
                "src/cogitate.py",
                "-l", non_url_value,
                "-t", token,
                "-r", "GatorCogitate/cogitate_tool",
                "-rm", "n",
            ],
            stdout=subprocess.PIPE,
        )
    except BaseException:
        pytest.skip("Rate Limit Exceeded.")
    stringResult = result.stdout.decode("utf-8")
    assert "Invalid repository link: " + non_url_value in stringResult


@pytest.mark.parametrize(
    "non_bool_value",
    ["5", "fgh", "?", "~~~", "y5"],
)
def test_bool_validator_raise_argparse_error(non_bool_value, capsys):
    result = subprocess.run(
        [
            "pipenv",
            "run",
            "python",
            "src/cogitate.py",
            "-l", "https://github.com/GatorCogitate/cogitate_tool",
            "-t", "token",
            "-r", "GatorCogitate/cogitate_tool",
            "-rm", non_bool_value,
        ],
        stderr=subprocess.PIPE,
    )
    stringResult = result.stderr.decode("utf-8")
    assert "cogitate.py: error: argument -rm/--runmerge: Boolean value expected, for example, yes, y, t, true" in stringResult


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
            "link : https://github.com/GatorCogitate/cogitate_tool\n"
            + "token : test_token\n"
            + "repo : GatorCogitate/cogitate_tool\nrunmerge : False\n"
            + "below : 5.0\nabove : 10.0\nwithin : 2.0\nstate : open\n"
            + "web : True\nmetric : i\ntestwithprintargs : y\n",
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
            "link : https://github.com/GatorCogitate/cogitate_tool\n"
            + "token : test_token\n"
            + "repo : GatorCogitate/cogitate_tool\nrunmerge : False\n"
            + "below : 0.2\nabove : 0.2\nwithin : 0.6\nstate : all\n"
            + "web : False\nmetric : both\ntestwithprintargs : y\n",
        ),
    ],
)
def test_retrieve_arguments(run_arguments_dict, correct_args, capsys):
    """
    Test run first with values for all possible arguments and then for all
    required arguments with unrequired arguments checked for their default values
                        NOTICE
    For this test case to run correctly in travis each line in the above correct_args
    must befollowed by a \n.
    To run this test in the command line interface, place a \r before every \n
    """
    call = subprocess.run(run_arguments_dict, stdout=PIPE)
    args = call.stdout.decode("utf-8")
    assert args == correct_args
    pass


@pytest.mark.parametrize(
    "invalidToken",
    ["".join([random.choice(string.ascii_letters + string.digits) for n in range(15)])],
)
def test_terminal_output_invalid_token(invalidToken, capsys):
    """
    Test correct output is produced with an invalid access token.
    For this test to work in Travis the stringReslt below must be compared to:
    "Cannot authenticate repository.\n"
    For this test to work in the command line it must be compared to:
    "Cannot authenticate repository.\r\n"
    """
    result = subprocess.run(
        [
            "pipenv",
            "run",
            "python",
            "src/cogitate.py",
            "-l", "https://github.com/GatorCogitate/cogitate_tool",
            "-t", invalidToken,
            "-r", "GatorCogitate/cogitate_tool",
            "-rm", "n",
        ],
        stdout=subprocess.PIPE,
    )
    stringResult = result.stdout.decode("utf-8")
    assert stringResult == "Cannot authenticate repository.\n"


def test_terminal_output_req_arg(capsys):
    result = subprocess.run(
        ["pipenv", "run", "python", "src/cogitate.py", ], stderr=subprocess.PIPE,
    )
    stringResult = result.stderr.decode("utf-8")
    assert "cogitate.py: error: the following arguments are required:" in stringResult
