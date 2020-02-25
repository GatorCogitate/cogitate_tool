"""Test the code that determines how the well the team worked together"""

from calculateMetrics import metrics
import sys
import string


def test_standard_deviations():
    """Function to test the standard_deviations function"""
    metrics.standard_deviations()
    assert len(metrics.values_list) >= 0
    assert metrics.new_counter >= 0
    assert metrics.standard_deviations_counter >= 0
    assert len(metrics.standard_deviations_list) >= 0


def test_commits_calculator():
    """Test the commits calc. function"""
    assert metrics.len(commits_scores) >= 0
    metrics.commits_calculator()
    assert metrics.commits_overall_score >= 0


def test_added_calculator():
    """Tests the lines added calculator"""
    assert metrics.added_overall_score == 0
    metrics.added_calculator()
    assert metrics.added_overall_score >= 0


def test_removed_calculator():
    """Tests the lines removed calculator"""
    assert metrics.removed_overall_score == 0
    metrics.removed_calculator()
    assert metrics.removed_overall_score >= 0


def test_total_team_score_calculator():
    """Tests the total team calculator"""
    assert metrics.total_team_score == 0
    metrics.total_team_score_calculator()
    assert metrics.total_team_score >= 0
