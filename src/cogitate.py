"""Command Line Interface for the Cogitate tool."""

import argparse
import os
import validators
from progress.bar import IncrementalBar
import data_collection
import data_processor
import json_handler


def main(args):
    """Execute the CLI."""
    if args["testwithprintargs"] == "y":
        for key, value in args.items():
            print(key, ":", value)
        return

    if not args["clearJson"]:
        progress_bar = IncrementalBar("Processing", max=3)
        updated_metrics_dict = json_handler.get_dict_from_json_file(
            "individual_metrics_storage"
        )
        # check for data in json file to catch user error in use of --
        if len(updated_metrics_dict) == 0:
            print("\n\n     Json empty: no data to retreive\n\n")
            return
        progress_bar.next(1)
        print("  Starting process...")
        progress_bar.next(1)
        print("  Retrieved json data")
    else:
        progress_bar = IncrementalBar("Processing", max=10)
        progress_bar.next(1)
        print("  Starting process...")
        updated_metrics_dict = collect_process_merge_data(args, progress_bar)
        if ("INVALID REPO/LINK" or "INVALID LINK") in updated_metrics_dict:
            return
        else:
            pass

    if args["metric"] in ["t", "team"]:
        progress_bar.next(1)
        print("  Calculating Team Scores")
        team(updated_metrics_dict, args["below"], args["above"], args["within"])
        progress_bar.finish()

    elif args["metric"] in ["i", "individual"]:
        progress_bar.next(1)
        print("  Calculating Individual Scores")
        progress_bar.finish()
        individual(updated_metrics_dict)

    elif args["metric"] == "both":
        progress_bar.next(1)
        print("  Calculating Scores")
        progress_bar.finish()
        individual(updated_metrics_dict)
        team(
            updated_metrics_dict, args["below"], args["above"], args["within"],
        )

    else:
        print("unknown value given for '-m' '--metric' in command line arguments")
        progress_bar.finish()
        return
    # allows the user to enter the web interface
    if args["web"] is True:
        os.system("streamlit run src/web_interface.py")
    else:
        print(
            "To see the output in the web, simply add '-w yes' to your command line arguments."
        )


# pylint: disable=R0915
# pylint: disable=C0330
def collect_process_merge_data(args, progress_bar):
    """Collect data and overwrite json file. Updates progress bar."""
    # Assess PyGithub access through token and repo path
    repository = data_collection.authenticate_repository(args["token"], args["repo"])
    # Assess PyDriller access with link validator method
    if repository == "INVALID" or link_validator(args["link"]) is False:
        print("Cannot authenticate repository.")
        progress_bar.finish()
        return "INVALID REPO/LINK"
    else:
        # Populate json file
        try:
            data_collection.collect_and_add_raw_data_to_json(
                args["link"], "raw_data_storage"
            )
            progress_bar.next(1)
            print("  Repository authenticated")
            progress_bar.next(1)
            print("  Raw Data Collected")
        except BaseException:
            print("Invalid repository link: " + args["link"])
            progress_bar.finish()
            return "INVALID LINK"
        # end of repository authentication
        # calculate metrics to be used for team evaluation
        issue_dict = {}
        issue_dict = data_collection.retrieve_issue_data(
            repository, args["state"], issue_dict
        )
        progress_bar.next(1)
        print("  Issue Data Collected")

        # calculate individual metrics
        individual_metrics_dict = data_collection.calculate_individual_metrics()
        progress_bar.next(1)
        print("  Individual Data Calculated")
        merged_dict = data_collection.merge_metric_and_issue_dicts(
            individual_metrics_dict, issue_dict
        )
        progress_bar.next(1)
        print("  Merged Data Sets")
        # merge duplicate usernames if user requests to
        if args["runmerge"]:
            progress_bar.next(1)
            print("  Merging Duplicate Usernames")
            while True:
                data_collection.print_individual_in_table(
                    data_dict=merged_dict, headings=[],
                )
                while True:
                    name_to_keep = str(input("\nPlease enter the username to keep: "))
                    if name_to_keep in merged_dict:
                        break
                    print("Unable to find the username to keep in dictionary")

                while True:
                    name_to_merge = str(input("\nPlease enter the username to merge: "))
                    if name_to_merge in merged_dict and name_to_merge != name_to_keep:
                        break
                    print(
                        "Username is either not in dictionary, "
                        + " or is a copy of username to keep"
                    )

                merged_dict = data_collection.merge_duplicate_usernames(
                    merged_dict, name_to_keep, name_to_merge
                )
                cont = input("\nMerge another username? (y/n)")
                if cont.lower() == "y":
                    pass
                else:
                    print("\nEnding Username merge...")
                    break
        elif not args["runmerge"]:
            progress_bar.next(1)
            print(
                "  Duplicate usernames unmerged"
                + "\nMerging duplicate usernames is suggested, "
                + "\nTo do so change '-rm' to 'y' in your command line arguments"
            )

        updated_metrics_dict = data_processor.add_new_metrics(merged_dict)
        progress_bar.next(1)
        print("  Added secondary metrics")
        # write dictionary to the json file.
        json_handler.write_dict_to_json_file(
            updated_metrics_dict, "individual_metrics_storage.json"
        )
        progress_bar.next(1)
        print("  Writing Data to JSON")
    return updated_metrics_dict


def retrieve_arguments():
    """Retrieve the user arguments and return the args dictionary."""
    a_parse = argparse.ArgumentParser()
    a_parse.add_argument(
        "-l",
        "--link",
        required=True,
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
        type=bool_validator,
        help="Starts the process of merging usernames. (y/n)",
    )
    a_parse.add_argument(
        "-b",
        "--below",
        required=False,
        type=float,
        default=0.2,
        help="Determines lower weight. Example : 0.2",
    )
    a_parse.add_argument(
        "-a",
        "--above",
        required=False,
        type=float,
        default=0.2,
        help="Determines higher weight. Example : 0.2",
    )
    a_parse.add_argument(
        "-wi",
        "--within",
        required=False,
        type=float,
        default=0.6,
        help="Determines value within weight. Example : 0.6",
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
    a_parse.add_argument(
        "-cj",
        "--clearJson",
        required=False,
        type=bool_validator,
        default=True,
        help="Allows the user to specify not to overwrite data currently in the"
        + "json files, so that calculations can be rerun with different modifiers",
    )
    # add arguments for below/above/within weight

    args = vars(a_parse.parse_args())

    return args


def team(individual_metrics_dict, below_float, above_float, within_float):
    """Call all team-based funtions."""
    below = below_float
    above = above_float
    within = within_float
    team_score = data_processor.calculate_team_score(
        individual_metrics_dict, below, above, within
    )
    print("Team Score:")
    print(team_score)
    return team_score


def individual(updated_dict):
    """Call all individual-based funtions."""
    new_dict = data_processor.individual_contribution(updated_dict)
    data_collection.print_individual_in_table(
        data_dict=new_dict,
        headings=["COMMITS", "ADDED", "REMOVED", "MODIFIED", "RATIO"],
        percentage=True,
    )


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
