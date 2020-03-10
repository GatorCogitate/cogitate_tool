""" Test suite for the command line interface functions in cogitate.py. """


import pytest
import random
import string
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
