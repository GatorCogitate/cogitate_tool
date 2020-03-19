"""Web Interface for interacting with Github repository info."""

import streamlit as st
import pandas as pd
from PIL import Image
import data_processor
import json_handler
import data_collection


# pylint: disable=E1120
def web_interface():
    """Execute the web interface."""
    updated_dict = json_handler.get_dict_from_json_file("individual_metrics_storage")

    # Sidebar menu options:
    add_selectbox = st.sidebar.selectbox(
        "What feature would you like to view?",
        (
            "Home",
            "Merge Duplicate Usernames (Recommended)",
            "Commits By An Individual",
            "Lines of Code Added, Modified, Deleted by an Individual",
            "Types of Files Modified by an Individual",
            "Average Overall Team Score",
            "Issues Contributed To By An Individual",
            "Pull Requests Contributed To By An Individual",
            "Team Members Who Contribute Source Code Without Tests",
            "Individual Contribution Percantages"
        ),
    )

    ################### Feature 1 ###################
    # How many commits did an individual make to a GitHub repository?
    if add_selectbox == "Home":
        home_page(updated_dict)

    elif add_selectbox == "Merge Duplicate Usernames (Recommended)":
        # while add_selectbox == "Merge Duplicate Usernames (Recommended)":
        merge_duplicate_users(updated_dict)

    elif add_selectbox == "Commits By An Individual":
        graph_commits_by_individual(updated_dict)
    ################### Feature 2 ###################
    # How many lines of code did an individual add, modify, and delete?
    elif add_selectbox == "Lines of Code Added, Modified, Deleted by an Individual":
        graph_lines_of_code(updated_dict)
    ################### Feature 3 ###################
    # What types of files did an individual normally modify in a repository?
    elif add_selectbox == "Types of Files Modified by an Individual":
        graph_types_of_files(updated_dict)
    ################### Feature 4 ###################
    # What is the overall score for an individual’s contribution to a team project?
    elif add_selectbox == "Average Overall Team Score":
        graph_team_score(updated_dict)
    ################### Feature 5 ###################
    # Issue info
    if add_selectbox == "Issues Contributed To By An Individual":
        graph_issues(updated_dict)
    ################### Feature 6 ###################
    # PR info
    elif add_selectbox == "Pull Requests Contributed To By An Individual":
        graph_pull_request(updated_dict)
    ################### Feature 7 ###################
    # Are there team members who contribute source code without also adding test cases?
    elif add_selectbox == "Team Members Who Contribute Source Code Without Tests":
        graph_test_contributions(updated_dict)
    elif add_selectbox == "Individual Contribution Percantages":
        graph_percent_individual_contribution(updated_dict)
    else:
        pass


def home_page(updated_dict):
    """Display home page graphics or data missing error message."""
    image = Image.open("./images/logo.png")

    st.image(image, use_column_width=True)

    st.markdown("# Welcome to Cogitate!")
    if not len(updated_dict) == 0:
        st.markdown(
            "## Use the sidebar on the left to navigate through Cogitate's features."
        )
    else:
        st.markdown("## Error, data was not collected!")
        st.markdown(
            "### please run the following command in your terminal window and try again."
        )
        st.markdown(
            "`pipenv run python src/cogitate.py -l repository_link -t user_token"
            + " -r repository_name -rm y`"
        )
        st.markdown("### Where :")
        st.markdown(
            "- `repository_link` is the link of the GitHub repository you want to analyze"
        )
        st.markdown("- `user_token` is your personal Github token")
        st.markdown(
            "- `repository_name` is the name of the repository in this format `org/name`"
        )
    with open("README.md") as readme_file:
        file_text = readme_file.read()
        logo_reference = "![Cogitate Logo](/images/logo.png)"
        if logo_reference in file_text:
            new_text = file_text.replace(logo_reference, "")
            st.markdown(new_text)
        else:
            st.markdown(file_text)


def graph_commits_by_individual(dictionary):
    """Graph commit information by individuals for web interface."""
    st.title("Commit Information")  # dispaly relevant title for dataframe

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][1:2]
    )  # display dataframe/graph that vizualizes commit info

    return df


def merge_duplicate_users(input_dict):
    """Prompts the user to choose two usernames from the dictionary to merge."""
    # Create needed select boxes with the dictionary keys as options
    keep = st.selectbox(
        label="Enter a username to keep:", options=list(input_dict.keys()), key="keep",
    )
    remove = st.selectbox(
        label="Enter a username to remove:",
        options=list(input_dict.keys()),
        key="remove",
    )
    # Add a button with the text merge
    merge = st.button("Merge")
    # Initialize placeholders for error messages and data text
    message_placehodler = st.empty()
    data_placeholder = st.empty()
    # Print the keys of the dictionary as a table in the appropriate placeholder
    data_placeholder.table(list(input_dict.keys()))
    # check if the merge button was clicked
    if merge:
        # check if the chosen usernames are the same and displays error
        if keep == remove:
            message_placehodler.markdown("__*ERROR: Identical users can't be merged*__")
        else:
            # shows a success message for the merge
            message_placehodler.markdown("__*Merge successfull*__")
            # Call the merge duplicate function and write to json
            # Writing on the json would change the dictionary state for all of
            # The web interface. It is necessary because the input for this
            # Is taken directly from the dictionary
            temp_dict = data_collection.merge_duplicate_usernames(
                input_dict, keep, remove
            )
            # recalculate the metrics to fix any discrepencies in modified lines
            # and format
            temp_dict = data_processor.add_new_metrics(temp_dict)
            json_handler.write_dict_to_json_file(
                temp_dict, "individual_metrics_storage"
            )
            # Reprint the merged data
            data_placeholder.table(list(temp_dict.keys()))


def graph_lines_of_code(dictionary):
    """Graph lines of code added, modified, and deleted for web interface."""
    st.title(
        "Lines of Code Added, Modified, Deleted by an Individual"
    )  # dispaly relevant title for dataframe

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][2:6]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_types_of_files(dictionary):
    """Graph to output types of files modified for web interface."""
    st.title("Types of Files Modified by an Individual")

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][7:8]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_team_score(dictionary):
    """Display the average team score for the web interface."""
    st.title("Average Team Score")

    team_score = data_processor.calculate_team_score(dictionary, 0.75, 0.25, 0.5)

    st.write("The calculated average team score for this repo is: ", team_score)

    return team_score


def graph_issues(dictionary):
    """Graphs the issues modified of individuals for web interface."""
    st.title("Issues Contributed To By An Individual")  # disp`aly relevant

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    for name in columns:
        issues_commented = len(df[name][8])
        df[name][8] = issues_commented
        issues_opened = len(df[name][9])
        df[name][9] = issues_opened

    st.bar_chart(
        df[columns][8:10]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_pull_request(dictionary):
    """Graph PRs contributed to by an individual for web interface."""
    st.title("Pull Requests Contributed to By An Individual")

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph
    for name in columns:
        prs_commented = len(df[name][10])
        df[name][10] = prs_commented
        prs_opened = len(df[name][11])
        df[name][11] = prs_opened

    st.bar_chart(
        df[columns][10:12]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_test_contributions(dictionary):
    """Graph test contributions for web interface."""
    st.title("Team Members Who Contribute Source Code Without Tests")

    df = pd.DataFrame.from_dict(dictionary, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph
    st.bar_chart(
        df[columns][12:14]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_percent_individual_contribution(dictionary):
    """Graph percentage of individual contribution."""
    st.title("Percentages of Individual Contribution")

    new_dict = data_processor.individual_contribution(dictionary)

    df = pd.DataFrame.from_dict(new_dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.title("Percentages of Commits, Added, & Removed:")

    st.bar_chart(#3
        df[columns][0:3]
    )  # display dataframe/graph

    st.title("Percentages of Modified & Ratio:")
    st.bar_chart(#3
        df[columns][4:6]
    )  # display dataframe/graph


web_interface()
