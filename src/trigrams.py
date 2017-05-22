"""This is a module that takes a text file and returns a generated story."""
import io
import random


# TEXT = ''


# function that implements trigram algorithm
def main(some_file, word_count):
    """Take a file, make a dictionary, and return a story."""
    print(make_story((make_dict(read_text(some_file))), word_count))


def read_text(some_file):
    """Get text from a file and returns a list."""
    open_file = io.open(some_file, encoding='utf-8')
    text = open_file.read().replace('\n', ' ').split()
    open_file.close()
    return text


# Reads list and makes dictionary
def make_dict(some_list):
    """Generate trigram key/value pairs."""
    story_dict = {}
    for i in range(len(some_list) - 2):
        story_key = '{} {}'.format(some_list[i], some_list[i + 1])
        if story_key in story_dict:
            story_dict[story_key].append(some_list[i + 2])
        else:
            story_dict[story_key] = [some_list[i + 2]]
    return story_dict


# Builds story text
def make_story(story_dict, word_count):
    """Return generated story."""
    story = random.choice(list(story_dict.keys())) + ' '
    for i in range(word_count):
        last_two_words = ' '.join(story.split()[-2:])
        if last_two_words in story_dict:
            if len(story_dict[last_two_words]) > 1:
                list_index = random.randint(0, len(story_dict[last_two_words]) - 1)
            else:
                list_index = 0
            story_add = story_dict[last_two_words][list_index] + ' '
        else:
            story_add = random.choice(list(story_dict.keys())) + ' '
        story = story + story_add
    return story


if __name__ == '__main__':  # pragma no cover
    main('../poe_test.txt', 200)
