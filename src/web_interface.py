"""Web Interface for interacting with Github repository info."""

import argparse
import streamlit as st
import numpy as np
import pandas as pd
import data_processor
import json_handler
from PIL import Image


def web_interface():
    """Execute the web interface."""

    # link = "https://github.com/GatorIncubator/petition-pronto"
    # token = "7ec6647bf060d0fcbd8f3c72d68844fa99292a79"
    # repo = "GatorIncubator/petition-pronto"
    updated_dict = json_handler.get_dict_from_json_file("individual_metrics_storage")

    # Sidebar menu options:
    add_selectbox = st.sidebar.selectbox(
        "What feature would you like to view?",
        (
            "Home",
            "Commits By An Individual",
            "Lines of Code Added, Modified, Deleted by an Individual",
            "Types of Files Modified by an Individual",
            "Overall Contribution Score To Team Project by an Individual",
            "Issues Contributed To By An Individual",
            "Pull Requests Contributed To By An Individual",
            "Team Members Who Contribute Source Code Without Tests",
            "Percentage of Individual Contribution",
        ),
    )

    ################### Feature 1 ###################
    # How many commits did an individual make to a GitHub repository?
    if add_selectbox == "Home":
        home_page(updated_dict)
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
    elif add_selectbox == "Overall Contribution Score To Team Project by an Individual":
        graph_team_score(updated_dict)
    ################### Feature 5 ###################
    # Are there individuals who collaborate together too frequently or not enough?
    if add_selectbox == "Issues Contributed To By An Individual":
        graph_issues(updated_dict)
    ################### Feature 6 ###################
    # Are there team members who are “code hoarders” or “domain experts”?
    elif add_selectbox == "Pull Requests Contributed To By An Individual":
        graph_pull_request(updated_dict)
    ################### Feature 7 ###################
    # Are there team members who contribute source code without also adding test cases?
    elif add_selectbox == "Team Members Who Contribute Source Code Without Tests":
        graph_test_contributions(updated_dict)
    ################### Feature 8 ###################
    # Are there team members who break the build or contribute to unusually high code churn?
    elif add_selectbox == "Percentage of Individual Contribution":
        graph_percent_individual_contribution(updated_dict)
    else:
        pass


def home_page(updated_dict):
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
            "`pipenv run python src/cogitate.py -l repository_link -t user_token -r repository_name -rm y`"
        )
        st.markdown("### Where :")
        st.markdown(
            "- `repository_link` is the link of the GitHub repository you want to analyze"
        )
        st.markdown("- `user_token` is your personal Github token")
        st.markdown(
            "- `repository_name` is the name of the repository in this format `org/name`"
        )


def graph_commits_by_individual(dict):
    """Graph commit information by individuals for web interface."""
    st.title("Commit Information")  # dispaly relevant title for dataframe

    df = pd.DataFrame.from_dict(dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][1:2]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_lines_of_code(dict):
    """Graph lines of code added, modified, and deleted for web interface."""
    st.title(
        "Lines of Code Added, Modified, Deleted by an Individual"
    )  # dispaly relevant title for dataframe

    df = pd.DataFrame.from_dict(dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][2:6]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_types_of_files(dict):
    """Graph to output types of files modified for web interface."""
    st.title("Types of Files Modified by an Individual")

    df = pd.DataFrame.from_dict(dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][7:8]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_team_score(dict):
    """Displays the average team score for the web interface."""
    st.title("Average Team Score")

    team_score = data_processor.calculate_team_score(dict, 0.75, 0.25, 0.5)

    st.write("The calculated average team score for this repo is: ", team_score)

    return team_score


def graph_issues(dict):
    """Graphs the issues modified of individuals for web interface."""
    st.title("Issues Contributed To By An Individual")  # disp`aly relevant

    df = pd.DataFrame.from_dict(dict, orient="index").T

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


def graph_pull_request(dict):
    """Graph PRs contributed to by an individual for web interface."""
    st.title("Pull Requests Contributed to By An Individual")

    df = pd.DataFrame.from_dict(dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph
    for name in columns:
        prs_commented = len(df[name][10])
        df[name][10] = prs_commented
        prs_opened = len(df[name][11])
        df[name][11] = prs_opened

    st.bar_chart(
        df[columns][11:13]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_test_contributions(dict):
    """Graph test contributions for web interface."""
    st.title("Team Members Who Contribute Source Code Without Tests")

    df = pd.DataFrame.from_dict(dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph
    st.bar_chart(
        df[columns][12:14]
    )  # display dataframe/graph that vizualizes commit info

    return df


def graph_percent_individual_contribution(dict):
    """Graph percentage of individual contribution."""

    st.title("Team Members Who Contribute Source Code Without Tests")
    new_dict = data_processor.individual_contribution(dict)
    print(new_dict)


web_interface()
