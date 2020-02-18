from cogitate_tool import CL_interface


def test_answers_dict():
    """ Checks that the answers_dict populates with user input. """
    assert len(CL_interface.answers) == 0
    congitate_tool.CL_interface()
    assert len(CL_interface.answers) < 0
