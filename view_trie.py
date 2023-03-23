from trie import *
import tkinter as tk

class TrieView():
    global HEIGHT_LEVEL
    HEIGHT_LEVEL = 60
    global WIDTH_BUTTONS
    WIDTH_BUTTONS = 50

    def __init__(self, trie: Trie):
        self.trie = trie
        self.window = tk.Tk()
        self.window.title("Trie")
        self.window.geometry(f"{26 * WIDTH_BUTTONS + WIDTH_BUTTONS // 2}x{self.trie.height * HEIGHT_LEVEL}")
        self.canvas = tk.Canvas(self.window)
        self.canvas.place(x=0,y=0, relheight=1, relwidth=1)
        self.lines = {level: [] for level in range(self.trie.height + 1)}

        # Grid configuration
        for level in range(self.trie.height + 1):
            tk.Grid.rowconfigure(self.window, level, weight=1, uniform='foo')
        for letter in range(26):
            tk.Grid.columnconfigure(self.window, letter, weight=1, uniform='foo')

        # Create buttons dict
        self.buttons = {self.trie.root: tk.Button(self.window, text='Root', command= lambda: self.view_levels(self.trie.root, 0))}
        self.buttons[self.trie.root].grid(row=0, column=13)
        self.window.mainloop()

    def view_levels(self, root=None, level=0): 
        if not root:
            root = self.trie.root
        else:
            for button in self.window.grid_slaves(row=level):
                button.configure(fg='black')
            self.buttons[root].configure(fg='blue')

        for l in range(level + 1, self.trie.height + 1):
            for button in self.window.grid_slaves(row=l):
                button.destroy()
            for line in self.lines[l-1]:
                self.canvas.delete(line)

        for value, node in root.children.items():
            self.buttons[node] = tk.Button(self.window, text=f'{value}', command= lambda curr = node: self.view_levels(curr, level + 1))
            if node.is_word:
                self.buttons[node].configure(highlightbackground="red")
            self.buttons[node].grid(row=level+1, column=ord(value)-65)
            self.window.update()
            self.lines[level].append(self.canvas.create_line(
                self.buttons[root].winfo_rootx() - WIDTH_BUTTONS // 2, 
                self.buttons[root].winfo_rooty() - HEIGHT_LEVEL // 2, 
                self.buttons[node].winfo_rootx() - WIDTH_BUTTONS // 2, 
                self.buttons[node].winfo_rooty() - HEIGHT_LEVEL // 2, 
                fill="green"
                ))