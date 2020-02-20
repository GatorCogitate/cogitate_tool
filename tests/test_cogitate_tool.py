import cogitate_tool


def test_answers_dict():
    """ Checks that the answers_dict populates with user input. """
    t_answers_dict = []
    assert len(t_answers_dict) == 0
    t_answers_dict = cogitate_tool.CL_interface()
    assert len(t_answers_dict) != 0
