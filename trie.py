class TrieNode():

    def __init__(self, value=None, end_word=False):
        self.value = value.upper() if value else None # this is a char
        self.children = dict() # Dictionary indexed by letters with TrieNodes as values
        self.is_word = end_word

class Trie():

    def __init__(self):
        self.root = TrieNode()
        self.height = 0
        
    def find(self, word: str) -> bool:
        word = word.upper()
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        if current.is_word:
            return True
        else: 
            return False

    def insert(self, word: str) -> None:
        word = word.upper()

        if self.height < len(word):
            self.height = len(word)

        current = self.root
        for ch in word: 
            if ch not in current.children:
                current.children[ch] = TrieNode(ch, end_word=False)
            current = current.children[ch]
        current.is_word = True 

    def remove(self, word: str) -> None:
        
        if not self.find(word):
            return 
        
        word = word.upper()
        to_delete = (self.root.children, word[0])
        current = self.root
        for ch in word:
            if len(current.children) > 1:
                to_delete = (current.children, ch)
                
            current = current.children[ch]
        if current.children: 
            current.is_word = False
        else:
            to_delete[0].pop(to_delete[1])
