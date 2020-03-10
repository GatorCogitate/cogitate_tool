"""Command Line Interface for the Cogitate tool."""

import argparse
import validators
import data_collection

# **uncomment web interface import statement when the web interface is complete**
# import web_interface


def main(args):
    """Execute the CLI."""

    # Currently only validates the PyGithub repository
    repository = data_collection.authenticate_repository(args["token"], args["repo"])
    if repository is False:
        print("Cannot authenticate repository.")
        return
    # allows the user to enter the CLI **needs to be uncommented when web interface is complete**
    if args["web"]:
        # print(web_interface.web_interface())
        print("'web Link'")
    elif not args["web"]:
        print(
            "To see the output in the web, simply add '-w yes' to your command line arguments."
        )
        # Temporary structure given issue retrieval is the only function
        data_collection.collect_and_add_raw_data_to_json(args["link"])
        contributor_data = data_collection.initialize_contributor_data(
            "contributor_data_template"
        )
        contributor_data = data_collection.retrieve_issue_data(
            repository, args["state"], contributor_data
        )


def retrieve_arguments():
    """Retrieve the user arguments and return the args dictionary."""
    # As no other functions exist in master as of this pull request, the args
    # below are written to accomadate issual retrieval in data_collection.py

    a_parse = argparse.ArgumentParser()
    a_parse.add_argument(
        "-l",
        "--link",
        type=link_validator,
        help="Cogitate a repo by the url of the repo, require full link of the repo",
    )
    a_parse.add_argument(
        "-t", "--token", required=True, type=str, help="Github User Token"
    )
    a_parse.add_argument(
        "-r",
        "--repo",
        required=True,
        type=str,
        help="User's Repository name, start with root dirctory (user or organization name)",
    )
    a_parse.add_argument(
        "-d",
        "--deleteusername ",
        required=True,
        type=str,
        help="Username that is merged into the kept username, then deleted.",
    )
    a_parse.add_argument(
        "-s",
        "--state",
        required=False,
        type=str,
        default="both",
        help="State of the Issue, open or closed",
    )
    a_parse.add_argument(
        "-w",
        "--web",
        required=False,
        type=bool_validator,
        default=False,
        help="Whether to show the detailed result in web interface",
    )

    args = vars(a_parse.parse_args())

    # pprint(find_repositories(args["link"]))
    return args


def team():
    """Call all team-based funtions."""


def individual():
    """Call all individual functions."""


def link_validator(url_str):
    """Take a string and checks if it is a valid URL."""
    # url() returns a boolean value
    if not validators.url(url_str):
        raise argparse.ArgumentTypeError("%s is not an URL" % url_str)
    return url_str


def bool_validator(bool_str):
    """Take a string and checks if user says yes or no."""
    positive_command_list = ["yes", "y", "t", "true", "1"]
    negative_command_list = ["no", "n", "f", "false", "0"]
    if isinstance(bool_str, bool):
        return bool_str
    if bool_str.lower() in positive_command_list:
        return True
    elif bool_str.lower() in negative_command_list:
        return False
    else:
        raise argparse.ArgumentTypeError(
            "Boolean value expected, for example, yes, y, t, true"
        )


if __name__ == "__main__":
    args = retrieve_arguments()
    main(args)
