"""This is our tests for our Trigrams."""


def test_list():
    """Testing to check string is list."""
    from trigrams import read_text
    assert type(read_text('../poe_test.txt')) == list


def test_dict():
    """Testing to check that we have a dictionary."""
    from trigrams import make_dict, read_text
    assert type(make_dict(read_text('../poe_test.txt'))) == dict
