"""Checks that the compute_tf_monolith.py produces the expected output."""

import shlex
import subprocess
import sys

if __name__ == "__main__":
    # assume that all of the checks run correctly and prove otherwise
    exit_code = 0
    # defines the command that will call the check_compute_tf_monolith.py
    command = 'dml gstats authorchurnmeta --author "MaddyKapfhammer"'

    # tokenize this command so that subprocess can accept each of its parts
    tokenized_command = shlex.split(command)
    print("Tokenized command to execute: " + str(tokenized_command))
    print()
    # run the tokenized command and display the output as a byte string
    result = subprocess.run(tokenized_command, stdout=subprocess.PIPE, check=True)
    # Display the standard output variable inside of the result from the subprocess
    # decode the byte string using UTF-8
    decoded_stdout = str(result.stdout.decode("utf-8"))
    print("Decoded output of executed command: \n" + decoded_stdout)
