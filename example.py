from Trie import Trie

print()
print('Initializing Trie with ["an", "app"].')
DICTIONARY = Trie([
    'an',
    'app'
])
print()

print('Searching the Trie for "app".')
print('"app":', DICTIONARY.find('app'))
print()

print('Searching the Trie for "apple".')
print('"apple":', DICTIONARY.find('apple'))
print()

print('Adding "apple" to the Trie.')
DICTIONARY.add(['apple'])
print('Searching the Trie for "apple".')
print('"apple":', DICTIONARY.find('apple'))
print()

print('Removing "app" from the Trie.')
DICTIONARY.remove(['app'])
print('Searching the Trie for "app".')
print('"app":', DICTIONARY.find('app'))
print()

import json
print('Printing the Trie Dict.')
print(json.dumps(DICTIONARY.trie(), indent=4))
print()
