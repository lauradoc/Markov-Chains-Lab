"""Generate Markov text from text files."""
import sys



import random

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        word_tuple = (words[i], words[i+1])
        word_add = words[i + 2]

        if word_tuple not in chains:
            chains[word_tuple] = []

        chains[word_tuple].append(word_add)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #make list of keys
    # extend function to add to list
    #inside loop pick random word 
    #use random choice to pull key
    #dict.keys = gives you a list of random dict keys to pick from

    chains_keys = []
    for key in chains.keys():
        chains_keys.append(key)

    words.extend(random.choice(chains_keys))

    for key, word in chains.items():
        words.append(random.choice(word))
    

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
