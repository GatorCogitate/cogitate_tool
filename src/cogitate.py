"""Command Line Interface for the Cogitate tool."""

import argparse
import validators
import data_collection
import data_processor

# **uncomment web interface import statement when the web interface is complete**
# import web_interface


def main(args):
    """Execute the CLI."""
    if args["testwithprintargs"] == "y":
        for key, value in args.items():
            print(key, ":", value)
        return
    else:
        pass
    # Assess PyGithub access through token and repo path
    repository = data_collection.authenticate_repository(args["token"], args["repo"])
    # Assess PyDriller access with link validator method
    if repository == "INVALID" or link_validator(args["link"]) is False:
        print("Cannot authenticate repository.")
        return
    # allows the user to enter the CLI **needs to be uncommented when web interface is complete**
    elif args["web"]:
        # print(web_interface.web_interface())
        print("'web Link'")
    elif not args["web"]:
        print(
            "To see the output in the web, simply add '-w yes' to your command line arguments."
        )
        # Populate json file
        data_collection.collect_and_add_raw_data_to_json(
            args["link"], "raw_data_storage"
        )
        # calculate metrics to be used for team evaluation
        issue_dict = {}
        issue_dict = data_collection.retrieve_issue_data(
            repository, args["state"], issue_dict
        )
        individual_metrics_dict = data_collection.calculate_individual_metrics()
        merged_dict = data_collection.merge_metric_and_issue_dicts(
            individual_metrics_dict, issue_dict
        )
        updated_dict = data_processor.add_new_metrics(merged_dict)
        if args["metric"] in ["t", "team"]:
            team(updated_dict, args["below"], args["above"], args["within"])
        elif args["metric"] in ["i", "individual"]:
            individual(updated_dict)
        elif args["metric"] == "both":
            new_individual_metrics_dict = individual(updated_dict)
            team(
                new_individual_metrics_dict,
                args["below"],
                args["above"],
                args["within"],
            )
        else:
            print("unknown value given for '-m' '--metric' in command line arguments")
            return


def retrieve_arguments():
    """Retrieve the user arguments and return the args dictionary."""
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
        help="User's Repository name, start with root dirctory (user or organization name)"
        + "\nExample GatorCogitate/cogitate_tool",
    )
    a_parse.add_argument(
        "-rm",
        "--runmerge",
        required=True,
        type=str,
        help="Starts the process of merging usernames.",
    )
    a_parse.add_argument(
        "-b",
        "--below",
        required=False,
        type=float,
        default=0.2,
        help="Determines lower weight.",
    )
    a_parse.add_argument(
        "-a",
        "--above",
        required=False,
        type=float,
        default=0.2,
        help="Determines higher weight.",
    )
    a_parse.add_argument(
        "-wi",
        "--within",
        required=False,
        type=float,
        default=0.6,
        help="Determines value within weight.",
    )
    a_parse.add_argument(
        "-s",
        "--state",
        required=False,
        type=str,
        default="all",
        help="State of the Issues to be retrieved; open, closed, or all",
    )
    a_parse.add_argument(
        "-w",
        "--web",
        required=False,
        type=bool_validator,
        default=False,
        help="Whether to show the detailed result in web interface. (y/n)",
    )
    a_parse.add_argument(
        "-m",
        "--metric",
        required=False,
        type=str,
        default="both",
        help="Invokes calculation of team or individual metrics. If not specified, both are run."
        + "\n(t/i/team/individual/both)",
    )
    a_parse.add_argument(
        "-twpa",
        "--testwithprintargs",
        required=False,
        type=str,
        default="n",
        help="To be used ONLY for testing purposes. Prints the args{} dict and closes program",
    )

    # add arguments for below/above/within weight

    args = vars(a_parse.parse_args())

    # pprint(find_repositories(args["link"]))
    return args


def team(individual_metrics_dict, below_float, above_float, within_float):
    """Call all team-based funtions."""
    team_score = data_processor.calculate_team_score(
        individual_metrics_dict, below_float, above_float, within_float
    )
    print("Team Score:")
    print(team_score)


def individual(updated_dict):
    """Call all individual-based funtions."""
    new_dict = data_processor.individual_contribution(updated_dict)
    data_collection.print_individual_in_table()
    return new_dict


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
    args_dict = retrieve_arguments()
    main(args_dict)
