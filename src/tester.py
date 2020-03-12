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

    link = "https://github.com/GatorIncubator/petition-pronto"
    token = "fa77f5d2fce4d780e68539cc987680b5626cc352"
    repo = "GatorIncubator/petition-pronto"
    repository = data_collection.authenticate_repository(token, repo)
    # Populate json file
    data_collection.collect_and_add_raw_data_to_json(link, "raw_data_storage")
    # allows the user to enter the merge while loop if they specified to
    data_collection.collect_and_add_individual_metrics_to_json()
    # calculate metrics to be used for team evaluation
    individual_metrics_dict = data_collection.calculate_individual_metrics()

    ISSUE_DATA = {}
    ISSUE_DATA = data_collection.retrieve_issue_data(repository, "all", ISSUE_DATA)
    DATA = data_collection.merge_metric_and_issue_dicts(
        individual_metrics_dict, ISSUE_DATA
    )

    # Sidebar menu options:
    add_selectbox = st.sidebar.selectbox(
        "What feature would you like to view?",
        (
            "Commits By An Individual",
            "Lines of Code Added, Modified, Deleted by an Individual",
            "Types of Files Modified by an Individual",
            "Overall Contribution Score To Team Project by an Individual",
            "Issues Contributed To By An Individual",
            "Pull Requests Contributed To By An Individual",
            "Team Members Who Contribute Source Code Without Tests",
            "Team Members Who Contribute To High Code Churn",
            "Team Members Who Frequently Fix The Build",
            "Team Members Who Are Unable To Contribute",
        ),
    )

    graph_team_score(individual_metrics_dict)

def graph_team_score(dict):
    """Graphs an individuals overall contribution for web interface."""
    st.title("An individuals overall contribution to a team or project")

    team_score = data_processor.calculate_team_score(
        dict, .75, .25, .5
    )
    print(team_score)
    #updated = data_processor.add_new_metrics(new_dict)
    #print(pd.DataFrame.from_dict(updated).T)



web_interface()  # call web interface main function
