import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]



def remove_punctuation(str):
    for character in str:
        if character in string.punctuation:
            str = str.replace(character, "")
    return str


def remove_stop_words(word_list):
    # all words that aren't stop words are no_stop_words
    no_stop_words = []
    for word in word_list:
        if word not in STOP_WORDS:
            no_stop_words.append(word)
    return no_stop_words


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as reader:
        text = reader.read()
        clean_text = remove_punctuation(text)

    # turn string into list and lower turns it to lowercase
    word_list = clean_text.lower().split()
    # print(word_list)
    word_count_dict = {}
    cleaner_text = remove_stop_words(word_list)
    # print(cleaner_text)
    # to make the word count:
    for word in cleaner_text: 
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + 1
            #print(word_count_dict)
        else:
            word_count_dict[word] = 1
    for word, count in word_count_dict.items():
        print(word, count)


# Other way of doing it:
#     word_count = {}
#     word_count[word] = word_count.get(word, 0) + 1
#     print(word_count)

# for word, count in word_count.items():
#     print(word, count)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
