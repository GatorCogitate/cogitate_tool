#!/bin/sh

# Make sure that you understand the purpose of this script

# Run the test suite so that:
# --> -x: Stops on first error or failure
# --> -s: Outputs all diagnostic information
pipenv run pytest -x -s
