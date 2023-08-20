import time
import sys


class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
   
    def char_to_index(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        cur = self.root
        for letter in word:
            cur_index = self.char_to_index(letter)
            if cur.children[cur_index] == None:
                cur.children[cur_index] = TrieNode()

            cur = cur.children[cur_index]
                

        cur.word_end = True
    
    def is_a_word(self, word):
        cur = self.root
        for letter in word:
            cur_index = self.char_to_index(letter)
            if cur.children[cur_index] == None:
                return False
            else:
                cur = cur.children[cur_index]
        
        return cur.word_end # When it goes len(word) levels deep into the trie, return if last node is the end of the word or not
    
    def is_set(self, word):
        cur = self.root
        for letter in word:
            cur_index = self.char_to_index(letter)
            if cur.children[cur_index] == None:
                return False
            else:
                cur = cur.children[cur_index]
        
        return True



dictionary = open("dictionary.txt", "r")
words = dictionary.readlines()
dict_trie = Trie()

n = time.time()
for word in words:
    dict_trie.insert(word.rstrip())
print("DONE: " + str(time.time() - n))

def solve(a):
    res = []
    for i in range(len(a)):
        c = a[i]
        if dict_trie.is_a_word(c):
            res.append(c)
        for j in range(i + 1, len(a)):
            c += a[j]
            if dict_trie.is_a_word(c):
                res.append(c)
    print(res)
    
       

if __name__ == "__main__":
    solve("iflight")