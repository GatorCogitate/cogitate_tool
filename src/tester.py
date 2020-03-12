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
    token = "726eef5d5fef42737eb721a841dc063d8b087c3a"
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
    individual(individual_metrics_dict)

def individual(dict):
    """Call all individual-based funtions."""
    updated_dict = data_processor.add_new_metrics(dict)
    print(updated_dict)

    df = (pd.DataFrame.from_dict(updated_dict, orient='index').T)

    # for k in updated_dict.keys():
    #     print("KEYER   ", k)
    # # print("\n\n\nDF")
    # # print(df)


    df  # display chart of sample commits

    columns = st.multiselect(
        label="Enter the names of specific contributors below:", options=df.columns
    )  # allow users to display specific contributor information on dataframe graph

    # print("COLUMNS:", columns)
    # print("COMMITS: \t",df["COMMITS"])
    st.bar_chart(df[columns][1:2])  # display dataframe/graph that vizualizes commit info


    edited_dict = data_processor.individual_contribution(updated_dict)
    #print(pd.DataFrame.from_dict(edited_dict).T)

web_interface()
