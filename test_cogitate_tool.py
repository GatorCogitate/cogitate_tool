from cogitate_tool import CL_interface


def test_answers_dict_():
    """ Checks that the answers_dict populates with user input. """
    assert len(cogitate_tool.answers) == 0
    congitate_tool.CL_interface()
    assert len(cogitate_tool.answers) < 0
