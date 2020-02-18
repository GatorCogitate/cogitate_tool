"""Tests to ensure that the functions in the demonstration work."""

from pygithub import im_commits_pygithub


def test_empty():
    """Check to see if the dictionary is equal to zero."""
    im_commits_pygithub.get_repo_commits_py_github()
    assert im_commits_pygithub.test_dict != 0
