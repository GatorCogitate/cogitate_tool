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
    token = "130bfe8bd0ed21841058282c08c1dcd4b67e234b"
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


    graph_team_score(individual_metrics_dict)

def graph_team_score(dict):
    """Graphs an individuals overall contribution for web interface."""

    updated_dict = data_processor.individual_contribution(dict)
    updated = data_processor.add_new_metrics(new_dict)
    df = pd.DataFrame.from_dict(updated_dict, orient="index").T
    print(df)
    #updated = data_processor.add_new_metrics(new_dict)
    #print(pd.DataFrame.from_dict(updated).T)



web_interface()  # call web interface main function
