""" Test suite for the command line interface functions in cogitate.py. """

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
            ['pipenv', 'run', 'python', 'src/cogitate.py',
             '-l', 'https://github.com/GatorCogitate/cogitate_tool',
             '-t', '0153104d37b5cd427e375234a4cbda82442539f5', '-r',
             'GatorCogitate/cogitate_tool', '-rm', 'n', '-b', '5', '-a', '10',
             '-wi', '2', '-s', 'open', '-w', 'y', '-m', 'i', '-twpa', 'y'],
            "link : https://github.com/GatorCogitate/cogitate_tool\r\n"
            + "token : 0153104d37b5cd427e375234a4cbda82442539f5\r\n"
            + "repo' : GatorCogitate/cogitate_tool\r\nendmerge : n\r\n"
            + "below : 5.0\r\nabove : 10.0\r\nwithin : 2.0\r\nstate : open\r\n"
            + "web : True\r\nmetric : i\r\ntestwithprintargs : y\r\n'web Link'\r\n"
        )
    ]
)
def test_retrieve_arguments(run_arguments_dict, correct_args, capsys):
    call = subprocess.Popen(run_arguments_dict, stdout=PIPE)
    args, none = call.communicate()
    str(args)
    assert args == correct_args
