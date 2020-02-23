import pytest
from src import driller


def test_answers_dict():
    """ Checks that the find_repositories function returns repo."""
    test_repo = "https://github.com/GatorCogitate/cogitate_tool"
    repo_obj = driller.find_repositories(test_repo)
    assert type(repo_obj) == "<class 'pydriller.repository_mining.RepositoryMining'>"
