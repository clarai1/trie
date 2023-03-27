# Trie of words

Implementation of a trie for words in Python, with Tkinter interface to visualize it.

# Description

The goal of this project is to generate a trie of words (incluting only letters A-Z, non-case-sensitive), that can be visualized through a user interface implemented with Tkinter.

## Trie structure

A `Trie` is described by its height and its root, which is a `TrieNode`.  
A `TrieNode` has a value and a dictionary containing all his children, indexed by the children's values. Another property of the `TrieNode` is the "is_word" property. If it is `True`, then the TrieNode is the final letter of a word.

A Trie object has the following functions:

- `find`: given a string of letters, returns `True` if the string is present in the trie, else returns `False`.
- `insert`: given a string of letters, inserts the string into the trie. 
- `remove`: given a string of letters, if the string is in the Trie, removes the string from the trie.

The advantage to use a `Trie` to store words is that the running time of each of these functions only depends on the length of the input word.

## Trie visualization

Once a `Trie` object is created, one can visualize it through a Tkinter interface by generating an instance of the `ViewTrie` class with the generate trie as input.

When creating a `ViewTrie` object, a Tkinter window will open showing only a button "Root".
After clicking on it, the initials of words present in the trie will appear.
Clicking on any letter will display the next level of letters present in the trie, starting with the current prefix.
The current prefix letters are colored in blue. 
When a letter is the final letter of a word in the trie, its button has red background.

Short video demonstration: 

https://user-images.githubusercontent.com/117021003/227970802-d29fe6a4-6189-462c-a421-5d9399667441.mov

# Structure of the project

`trie.py` contains the implementation of the TrieNode and Trie classes.

`view_trie.py` contains the implementation of the ViewTrie class, this class generates the user interface to visualize a given trie.

`main.py` contains script to create a trie from a `.txt` file and visualize it. 

`words.txt` contains a relatively short list of random words to test the trie.

`words_alpha.txt` contains a list of over 466k English words, source: https://github.com/dwyl/english-words.

# How to run the project
 
Clone this repository, navigate to the project folder.
Run the main file from the terminal:

    python main.py
