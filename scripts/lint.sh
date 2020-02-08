#!/bin/bash

# determine whether or not black code formatting
# will fail if code is not correctly formatted
# "--check" returns non-zero exit code if formatting needed
# otherwise, the black check is run for diagnostic purposes
if [[ "$1" == "--check" ]]; then
    CHECK="--check"
else
    CHECK=""
fi

# assume that all of the linters passed and prove otherwise
PASSED=true

OS="$(uname)"

# collect the files on MacOS and Linux
if [[ "$OS" == "Darwin" ]]; then
    FILES=$(find -E . -type f -regex '\./(termfrequency|tests)/.*.py')
else
    FILES=$(find . -type f -regextype posix-extended -regex '\./(termfrequency|tests)/.*.py')
fi

# Notes about the linters run on Linux and MacOS:
# - black checks and fixes Python code formatting
# - pylint and flake8 check Python code
# - other linters such as radon may be added later

# define all of the linters to iteratively run
declare -A LINTERS
LINTERS=( ["black"]="pipenv run black $CHECK $FILES" ["pylint"]="pipenv run pylint $FILES" ["flake8"]="pipenv run flake8 $FILES" ["pydocstyle"]="pipenv run pydocstyle $FILES" )

# run each of the already configured linters
for tool in "${!LINTERS[@]}"; do
    echo " -- Running $tool"
    # shellcheck disable=SC2086
    if ! ${LINTERS[$tool]}; then
        echo " -- Failed"
        PASSED=false
    else
        echo " -- Passed"
    fi
    echo ""
done

# display the final diagnostic information
if [[ "$PASSED" != "true" ]]; then
    echo "Not all linters passed!"
    exit 1
else
    echo "All is good!"
    exit 0
fi
