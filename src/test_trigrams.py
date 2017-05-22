"""This is our tests for our Trigrams."""


SAMPLE_DICT = {
    'The thousand': ['injuries'],
    'thousand injuries': ['of'],
    'injuries of': ['Fortunato'],
    'of Fortunato': ['I'],
    'Fortunato I': ['had'],
    'I had': ['borne'],
    'had borne': ['as'],
    'borne as': ['I'],
    'as I': ['best'],
    'I best': ['could,'],
    'best could,': ['but'],
    'could, but': ['when'],
    'but when': ['he']
}


def test_list():
    """Testing to check string is list."""
    from trigrams import read_text
    assert type(read_text('../poe_test.txt')) == list


def test_dict():
    """Testing to check that we have a dictionary."""
    from trigrams import make_dict, read_text
    assert type(make_dict(read_text('../poe_test.txt'))) == dict


def test_make_story():
    """Testing story for length."""
    from trigrams import make_story
    assert len(make_story(SAMPLE_DICT, 100).split()) == 100


def test_dict_entry():
    """Testing dictionary values for given keys."""
    from trigrams import make_dict, read_text
    story_dict = make_dict(read_text('../poe_test_short.txt'))
    assert story_dict == SAMPLE_DICT
