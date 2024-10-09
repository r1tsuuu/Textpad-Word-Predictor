#!/usr/bin/env python3

from pygtrie import CharTrie

class Wordlist:
    def __init__(self, filename):
        self.trie = CharTrie()
        with open(filename) as words:
            lines = words.readlines()
            for line in lines:
                self.trie[line.strip()] = True

    def contains(self, word: str) -> bool:
        '''
        Check whether `word` can be found in the word list.
        '''
        return self.trie.has_key(word)

    def contains_prefix(self, prefix: str) -> bool:
        '''
        Check whether there is a word in the word list that starts with `prefix`.
        '''
        return self.trie.has_subtrie(prefix) or self.trie.has_key(prefix)
