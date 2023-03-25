# Trie of words

Implementation of a trie for words in Python, with Tkinter interface to visualize it.

# Description

The goal of this project is to generate a trie of words (incluting only letters A-Z, non-case-sensitive), that can be visualized through a user interface implemented with Tkinter.

A Trie is described by its height and its root, which is a TrieNode.  
A TrieNode has a value and a dictionary containing all his children, indexed by the children's values. Another property of the TrieNode is the "is_word" property. If it is `True`, then the TrieNode is the final letter of a word.

A Trie object has the following functions:

- `find`: given a string of letters, returns `True` if the string is present in the Trie, else returns `False`.
- `insert`: given a string of letters, inserts the string into the Trie. 
- `remove`: given a string of letters, if the string is in the Trie, removes the string from the Trie.

The advantage to use a Trie to store words is that the running time of each of these functions only depends on the length of the input word.

# Structure of the project

`trie.py` contains the implementation of the TrieNode and Trie classes.

`view_trie.py` contains the implementation of the ViewTrie class, this class is used to generate the user interface to visualize tries.

`main.py` contains script to create a trie from a `.txt` file and visualize it. 

`words.txt` contains a relatively short list of random words to test the trie.

`words_alpha.txt` contains a list of over 466k English words, source: https://github.com/dwyl/english-words.

# How to run the project
 
Clone this repository, navigate to the project folder.
Run the main file from the terminal:

    python main.py