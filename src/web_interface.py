"""Web Interface for interacting with Github repository info."""

# from data_collection import collect_commits
import argparse

# from pprint import pprint

# from driller import find_repositories


import streamlit as st
import numpy as np
import pandas as pd


def web_interface():
    """Execute the web interface."""

    # Sidebar menu:
    add_selectbox = st.sidebar.selectbox(
        'What feature would you like to view?',
        ('Commits By An Individual', 'Lines of Code Added, Modified, Deleted by an Individual', 'Types of Files Modified by an Individual', 'Overall Contribution Score To Team Project by an Individual', 'Collaboration Tendencies of Individuals', 'Team Members Who Are Code Hoarders', 'Team Members Who Contribute Source Code Without Tests', 'Team Members Who Contribute To High Code Churn', 'Team Members Who Frequently Fix The Build', 'Team Members Who Are Unable To Contribute')
    )

    ################### Feature 1 ###################
    # How many commits did an individual make to a GitHub repository?
    if add_selectbox == 'Commits By An Individual':
        st.title("Commit Information")  # dispaly relevant title for dataframe

        df = pd.DataFrame({
          'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
          'Christian Lussier': [8, 5, 9, 3],
          'Cory Wiard': [5, 9, 3, 5],
          'Devin Spitalny': [2, 5, 7, 3],
          'Devin Ho': [8, 9, 2, 1],
          'Jordan Wilson': [5, 9, 3, 8],
          'Danny Reid': [5, 4, 3, 5],
          'Anthony Baldeosingh': [1, 2, 1, 2],
          'Xingbang Liu': [6, 9, 4, 7]
        })  # create dataframe with sample dates and contributor commit numbers

        df = df.rename(columns={'date':'index'}).set_index('index')  # set date as index

        df  # display chart of sample commits

        columns = st.multiselect(
            label="Enter the names of specific contributors below:", options=df.columns
        )  # allow users to display specific contributor information on dataframe graph

        st.line_chart(df[columns])  # display dataframe/graph that vizualizes commit info

    ################### Feature 2 ###################
    # How many lines of code did an individual add, modify, and delete?
    elif add_selectbox == 'Lines of Code Added, Modified, Deleted by an Individual':
        st.title("Lines of Code Added, Modified, Deleted by an Individual")  # dispaly relevant title for dataframe

    ################### Feature 3 ###################
    # Why types of files did an individual normally modify in a repository?

    ################### Feature 4 ###################
    # What is the overall score for an individual’s contribution to a team project?
    elif add_selectbox == 'An individuals overall contribution to a team or project':
    ################### Feature 5 ###################
    # Are there individuals who collaborate together too frequently or not enough?

    ################### Feature 6 ###################
    # Are there team members who are “code hoarders” or “domain experts”?

    ################### Feature 7 ###################
    # Are there team members who contribute source code without also adding test cases?
    elif add_selectbox == 'Team Members Who Contribute Source Code Without Tests':
        st.title("Team Members Who Contribute Source Code Without Tests")
    ################### Feature 8 ###################
    # Are there team members who break the build or contribute to unusually high code churn?

    ################### Feature 9 ###################
    # Are there team members who frequently fix the build right before merging a PR to master?

    ################### Feature 10 ###################
    # Are there team members who are unable to contribute or who seem stuck on finishing a task?
    else:
        pass






web_interface()
