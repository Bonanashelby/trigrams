"""This is our tests for our Trigrams."""
import pytest


DICT_TEST = [
    ['At the most remote end of the crypt there appeared another less spacious.', 'At the', ['most']],
    ['the most cake the most pie', 'the most', ['cake', 'pie']]
]


def test_list():
    """Testing to check string is list."""
    from trigrams import read_text
    assert type(read_text('../poe_test.txt')) == list


def test_dict():
    """Testing to check that we have a dictionary."""
    from trigrams import make_dict, read_text
    assert type(make_dict(read_text('../poe_test.txt'))) == dict


# @pytest.mark.parametrize('string, key, value', DICT_TEST)
# def test_dict_entry(string, key, value):
#     """Testing dictionary values for given keys."""
#     from trigrams import make_dict, read_text
#     story_dict = make_dict(read_text('../poe_test.txt'))
#     assert story_dict[key] == value
