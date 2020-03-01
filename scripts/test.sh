#!/bin/bash

# Run the test suite so that:
# --> -x: Stops on first error or failure
# --> -s: Outputs all diagnostic information
pipenv run pytest -x -s -v
