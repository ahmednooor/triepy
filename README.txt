# A Python Class to implement a Trie data structure for a list of words.

# USAGE:

# Import Class
from path/to/Trie.py import Trie

# Initialize
DICTIONARY = Trie([
    an,
    app
])

# Find a word
DICTIONARY.find('app')    # will return True
DICTIONARY.find('apple')    # will return False

# Add new word/s
DICTIONARY.add([
    apple,
    apricot
])

# Remove word/s
DICTIONARY.remove([
    app,
    apricot
])

# Get implemented Trie in the form of Python Dictionary
DICTIONARY.trie()    # will return a python dictionary
