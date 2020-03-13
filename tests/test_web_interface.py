"""
Test module to determine the correctness of the web_interface.py file.
"""
import pytest
from src import data_collection
from src import json_handler
from src import web_interface










def test_graph_commits_by_individual():
    """Checks that the size of the input variable is correct."""
    df = web_interface.graph_commits_by_individual(dict)
    assert len(df) != 0
