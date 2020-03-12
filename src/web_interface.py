"""Web Interface for interacting with Github repository info."""

import argparse
import streamlit as st
import numpy as np
import pandas as pd
import data_collection
import data_processor
import json_handler

def web_interface():
    """Execute the web interface."""

    link = "https://github.com/lussierc/lussiercLaTeXResume"
    token = "0abec51ed0fd75a8f976f523a8fc7fd01e651091"
    repo = "lussierc/lussiercLaTeXResume"
    repository = data_collection.authenticate_repository(token, repo)
    print("1")
    # Populate json file
    data_collection.collect_and_add_raw_data_to_json(
        link, "raw_data_storage"
    )
    # allows the user to enter the merge while loop if they specified to
    data_collection.collect_and_add_individual_metrics_to_json()
    # calculate metrics to be used for team evaluation
    individual_metrics_dict = data_collection.calculate_individual_metrics()

    # Sidebar menu options:
    add_selectbox = st.sidebar.selectbox(
        "What feature would you like to view?",
        (
            "Commits By An Individual",
            "Lines of Code Added, Modified, Deleted by an Individual",
            "Types of Files Modified by an Individual",
            "Overall Contribution Score To Team Project by an Individual",
            "Collaboration Tendencies of Individuals",
            "Team Members Who Are Code Hoarders",
            "Team Members Who Contribute Source Code Without Tests",
            "Team Members Who Contribute To High Code Churn",
            "Team Members Who Frequently Fix The Build",
            "Team Members Who Are Unable To Contribute",
        ),
    )

    ################### Feature 1 ###################
    # How many commits did an individual make to a GitHub repository?
    if add_selectbox == "Commits By An Individual":
        graph_commits_by_individual(individual_metrics_dict)
    ################### Feature 2 ###################
    # How many lines of code did an individual add, modify, and delete?
    elif add_selectbox == "Lines of Code Added, Modified, Deleted by an Individual":
        graph_lines_of_code(individual_metrics_dict)
    ################### Feature 3 ###################
    # What types of files did an individual normally modify in a repository?
    elif add_selectbox == "What Types of Files did an Individual":
        graph_types_of_files(individual_metrics_dict)
    ################### Feature 4 ###################
    # What is the overall score for an individual’s contribution to a team project?
    elif add_selectbox == "An individuals overall contribution to a team or project":
        graph_overall_contribution()
    ################### Feature 5 ###################
    # Are there individuals who collaborate together too frequently or not enough?
    if add_selectbox == "Collaboration Tendencies of Individuals":
        graph_collaboration_tendencies()
    ################### Feature 6 ###################
    # Are there team members who are “code hoarders” or “domain experts”?
    elif add_selectbox == "Team Members Who Are Code Hoarders":
        graph_code_hoarders()
    ################### Feature 7 ###################
    # Are there team members who contribute source code without also adding test cases?
    elif add_selectbox == "Team Members Who Contribute Source Code Without Tests":
        graph_test_contributions(individual_metrics_dict)
    ################### Feature 8 ###################
    # Are there team members who break the build or contribute to unusually high code churn?
    elif add_selectbox == "Team Members Who Contribute To High Code Churn":
        graph_code_churn()
    ################### Feature 9 ###################
    # Are there team members who frequently fix the build right before merging a PR to master?
    elif add_selectbox == "Team Members Who Frequently Fix The Build":
        graph_build_fix_rate()
    ################### Feature 10 ###################
    # Are there team members who are unable to contribute or who seem stuck on finishing a task?
    elif add_selectbox == "Team Members Who Are Unable To Contribute":
        graph_unable_to_contribute()
    else:
        pass


def graph_commits_by_individual(dict):
    """Graph commit information by individuals for web interface."""
    st.title("Commit Information")  # dispaly relevant title for dataframe

    updated_dict = data_processor.add_new_metrics(dict)

    df = (pd.DataFrame.from_dict(updated_dict, orient='index').T)

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns][1:2])  # display dataframe/graph that vizualizes commit info

def graph_lines_of_code(dict):
    """Graph lines of code added, modified, and deleted for web interface."""
    st.title(
        "Lines of Code Added, Modified, Deleted by an Individual"
    )  # dispaly relevant title for dataframe
    updated_dict = data_processor.add_new_metrics(dict)

    df = (pd.DataFrame.from_dict(updated_dict, orient='index').T)

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns][2:5])  # display dataframe/graph that vizualizes commit info


    edited_dict = data_processor.individual_contribution(updated_dict)

def graph_types_of_files(dict):
    """Graph to output types of files modified for web interface."""
    st.title("Types of Files Modified by an Individual")

    updated_dict = data_processor.add_new_metrics(dict)

    df = (pd.DataFrame.from_dict(updated_dict, orient='index').T)

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns][8:9])  # display dataframe/graph that vizualizes commit info


    edited_dict = data_processor.individual_contribution(updated_dict)

def graph_overall_contribution():
    """Graphs an individuals overall contribution for web interface."""
    st.title("An individuals overall contribution to a team or project")

    df = pd.DataFrame(
        {
            "date": ["10/1/2019", "10/2/2019", "10/3/2019", "10/4/2019"],
            "Christian Lussier": [7, 5, 5, 3],
            "Cory Wiard": [2, 1, 3, 5],
            "Devin Spitalny": [8, 1, 0, 7],
            "Devin Ho": [9, 9, 2, 5],
            "Jordan Wilson": [5, 9, 3, 8],
            "Danny Reid": [1, 2, 3, 1],
            "Anthony Baldeosingh": [7, 4, 3, 4],
            "Xingbang Liu": [6, 6, 8, 2],
        }
    )  # create dataframe with sample data for files

    df = df.rename(columns={"date": "index"}).set_index("index")  # set date as index

    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.line_chart(df[columns])  # display dataframe/graph that vizualizes commit info


def graph_collaboration_tendencies():
    """Graphs the collaboration tendencies of individuals for web interface."""
    st.title("Collaboration Tendencies of Individuals")  # disp`aly relevant
    df = pd.DataFrame(
        {
            "date": ["1/1/2020", "1/2/2020", "1/3/2020", "10/4/2020"],
            "Christian Lussier": [80, 5, 9, 3],
            "Cory Wiard": [5, 90, 3, 5],
            "Devin Spitalny": [23, 58, 70, 3],
            "Jordan Wilson": [5, 5, 3, 8],
            "Danny Reid": [50, 41, 311, 5],
            "Anthony Baldeosingh": [10, 200, 1, 22],
        }
    )  # create dataframe with sample dates and contributor commit numbers

    df = df.rename(columns={"date": "index"}).set_index("index")  # set date as index

    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.line_chart(df[columns])  # display dataframe/graph that vizualizes commit info


def graph_code_hoarders():
    """Graph what team members are code hoarders for web interface."""
    st.title("Team Members Who Are Code Hoarders")

    df = pd.DataFrame(
        {
            "commits": ["total", "src", "tests", "scripts"],
            "Christian Lussier": [10, 2, 5, 3],
            "Cory Wiard": [12, 4, 4, 4],
            "Devin Spitalny": [18, 13, 1, 4],
            "Devin Ho": [11, 2, 8, 1],
            "Jordan Wilson": [10, 3, 3, 4],
            "Danny Reid": [14, 8, 3, 3],
            "Anthony Baldeosingh": [16, 14, 1, 1],
            "Xingbang Liu": [13, 4, 5, 4],
        }
    )

    df = df.rename(columns={"commits": "index"}).set_index("index")  # set date as index

    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns])  # display dataframe/graph that vizualizes commit info


def graph_test_contributions(dict):
    """Graph test contributions for web interface."""
    st.title("Team Members Who Contribute Source Code Without Tests")
    updated_dict = data_processor.add_new_metrics(dict)
    df = (pd.DataFrame.from_dict(updated_dict, orient=‘index’).T)

    columns = st.multiselect(
    label=“Enter the names of specific contributors below:“, options=df.columns
    )  # allow users to display specific contributor information on dataframe graph


def graph_code_churn():
    """Graph code churn for web interface."""
    st.title(
        "Team Members Code Churn Contributions"
    )  # dispaly relevant title for dataframe
    df = pd.DataFrame(
        {
            "type": ["Code Churn"],
            "Christian Lussier": [8],
            "Cory Wiard": [5],
            "Devin Spitalny": [2],
            "Devin Ho": [8],
            "Jordan Wilson": [5],
            "Danny Reid": [5],
            "Anthony Baldeosingh": [1],
            "Xingbang Liu": [6],
        }
    )  # create dataframe with sample dates and contributor commit numbers

    df = df.rename(columns={"type": "index"}).set_index("index")  # set date as index

    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns])  # display dataframe/graph that vizualizes commit info


def graph_build_fix_rate():
    """Graph about who frequently fixes the build for web interface."""
    st.title("Feature 9")  # dispaly relevant title for dataframe


def graph_unable_to_contribute():
    """Graph team members who are unable to contribute."""
    st.title(
        "Team Members Who Are Unable To Contribute"
    )  # dispaly relevant title for dataframe
    df = pd.DataFrame(
        {
            "type": ["Unable To Contribute"],
            "Christian Lussier": [1],
            "Cory Wiard": [1],
            "Devin Spitalny": [1],
            "Devin Ho": [2],
            "Jordan Wilson": [1],
            "Danny Reid": [1],
            "Anthony Baldeosingh": [2],
            "Xingbang Liu": [1],
        }
    )  # create dataframe with sample dates and contributor commit numbers

    df = df.rename(columns={"type": "index"}).set_index("index")  # set date as index

    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    st.bar_chart(df[columns])  # display dataframe/graph that vizualizes commit info


web_interface()  # call web interface main function
