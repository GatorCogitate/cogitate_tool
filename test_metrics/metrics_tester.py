"""Test the code that determines how the well the team worked together"""

from calculate_metrics import metrics
import sys
import string


def test_standard_deviations():
    """Function to test the standard_deviations function"""
    metrics.standard_deviations()
    assert len(metrics.commits_list) >= 0
    assert len(metrics.added_list) >= 0
    assert len(metrics.removed_list) >= 0
    assert len(metrics.standard_deviations_list) >= 0

def test_commits_calculator():
    """Test the commits calc. function"""
    metrics.commits_calculator()
    assert metrics.commits_sd > 0
    assert len(metrics.commit_scores) >= 0

def test_added_calculator():
    """Tests the lines added calculator"""
    metrics.added_calculator()
    assert metrics.added_sd > 0
    assert len(metrics.added_scores) >= 0

def test_removed_calculator():
    """Tests the lines removed calculator"""
    metrics.removed_calculator()
    assert metrics.removed_sd > 0
    assert len(metrics.removed_scores) >= 0

def test_total_team_score_calculator():
    """Tests the total team calculator"""
    metrics.test_total_team_score_calculator()
    assert metrics.total_team_score >= 0
    assert metrics.total_team_percent >= 0
