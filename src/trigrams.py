import io


# function that implements trigram algorithm
def main(some_file, word_count):
    print(read_text(some_file))
    print(200)


def read_text(some_file):
    '''This function gets text from a file and returns a list.'''
    open_file = io.open(some_file, encoding='utf-8')
    text = open_file.read().replace('\n', ' ')
    open_file.close()
    return text.split(' ')


# Reads list and makes dictionary
def make_dict(some_list):
    """generate trigram key/value pairs"""
    story_dict = {}
    for i in range(len(some_list) - 2):
        story_dict['{} {}'.format(some_list[i], some_list[i + 1])] = some_list[i + 2]
    return story_dict


# Builds story text
def make_story(word_count):
    # pick a starting place
    # find trigrams in dictionary
    # if no trigram and story DNE word_count, pick
    pass


if __name__ == '__main__':
    main('../poe_test.txt', 200)
