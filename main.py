from trie import *
from view_trie import *

d = Trie()

file = open("words.txt", "r")
lines = file.read().splitlines()

for word in lines:
    d.insert(word)

view = TrieView(d)