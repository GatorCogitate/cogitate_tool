"""Test the code that determines how the well the team worked together"""

from calculateMetrics import metrics
import sys
import string


def test_standard_deviations():
    """Function to test the standard_deviations function"""
    metrics.standard_deviations()
    assert len(metrics.values_list) >= 0
    assert len(metrics.standard_deviations_list) >= 0


def test_commits_calculator():
    """Test the commits calc. function"""
    assert metrics.commits_overall_score == 0
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

# def test_get_user_score():
    # """Test the user score"""
    # metrics.input() = "cassidyt2"
    # metrics.get_user_scores().username == "cassidyt2"
    # user_score_output = metrics.get_user_scores()
    # assert user_score_output == metrics.user_scores
