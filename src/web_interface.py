"""Web Interface for interacting with Github repository info."""

import argparse
import streamlit as st
import numpy as np
import pandas as pd
import data_collection
import data_processor
import json_handler
from PIL import Image


def web_interface():
    """Execute the web interface."""

    link = "https://github.com/GatorIncubator/petition-pronto"
    token = "7ec6647bf060d0fcbd8f3c72d68844fa99292a79"
    repo = "GatorIncubator/petition-pronto"
    repository = data_collection.authenticate_repository(token, repo)
    # Populate json file
    data_collection.collect_and_add_raw_data_to_json(
        link, "raw_data_storage"
    )
    # calculate metrics to be used for team evaluation
    issue_dict = {}
    issue_dict = data_collection.retrieve_issue_data(
        repository, "all", issue_dict
    )
    individual_metrics_dict = data_collection.calculate_individual_metrics()
    merged_dict = data_collection.merge_metric_and_issue_dicts(
        individual_metrics_dict, issue_dict
    )
    updated_dict = data_processor.add_new_metrics(merged_dict)
    print(updated_dict)

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
        home_page()
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

def home_page():
    image = Image.open('./images/logo.png')

    st.image(image,
             use_column_width=True)

    st.title("Welcome to Cogitate!")
    st.text("Use the sidebar on the left to navigate through Cogitate's features.")

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
    updated_dict = data_processor.add_new_metrics(dict)

    df = pd.DataFrame.from_dict(updated_dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][2:6]
    )  # display dataframe/graph that vizualizes commit info

    edited_dict = data_processor.individual_contribution(updated_dict)


def graph_types_of_files(dict):
    """Graph to output types of files modified for web interface."""
    st.title("Types of Files Modified by an Individual")

    updated_dict = data_processor.add_new_metrics(dict)

    df = pd.DataFrame.from_dict(updated_dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(
        df[columns][7:8]
    )  # display dataframe/graph that vizualizes commit info

    edited_dict = data_processor.individual_contribution(updated_dict)


def graph_team_score(dict):
    """Displays the average team score for the web interface."""
    st.title("Average Team Score")

    team_score = data_processor.calculate_team_score(dict, 0.75, 0.25, 0.5)

    st.write("The calculated average team score for this repo is: ", team_score)


def graph_issues(dict):
    """Graphs the issues modified of individuals for web interface."""
    st.title("Issues Contributed To By An Individual")  # disp`aly relevant

    updated_dict = data_processor.add_new_metrics(dict)

    df = pd.DataFrame.from_dict(updated_dict, orient="index").T

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


def graph_pull_request(dict):
    """Graph PRs contributed to by an individual for web interface."""
    st.title("Pull Requests Contributed to By An Individual")

    updated_dict = data_processor.add_new_metrics(dict)

    df = pd.DataFrame.from_dict(updated_dict, orient="index").T

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


def graph_test_contributions(dict):
    """Graph test contributions for web interface."""
    st.title("Team Members Who Contribute Source Code Without Tests")
    updated_dict = data_processor.add_new_metrics(dict)
    df = pd.DataFrame.from_dict(updated_dict, orient="index").T

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph
    st.bar_chart(
        df[columns][12:14]
    )  # display dataframe/graph that vizualizes commit info


def graph_percent_individual_contribution(individual_metrics_dict):
    """Graph percentage of individual contribution."""

    st.title("Team Members Who Contribute Source Code Without Tests")

web_interface()
