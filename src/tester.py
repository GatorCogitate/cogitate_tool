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
    token = "6a9c046d3faa149026ba980bdd65fb87c62fac2a"
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


    graph_team_score(updated_dict)

def graph_team_score(dict):
    """Graphs an individuals overall contribution for web interface."""

    updated_dict = data_processor.individual_contribution(dict)
    df = pd.DataFrame.from_dict(updated_dict, orient="index").T
    print(df)
    #updated = data_processor.add_new_metrics(new_dict)
    #print(pd.DataFrame.from_dict(updated).T)



web_interface()  # call web interface main function
