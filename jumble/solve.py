import time
import sys
from itertools import permutations


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
    
    def find(self, word):
        cur = self.root
        for letter in word:
            cur_index = self.char_to_index(letter)
            if cur.children[cur_index] == None:
                return False
            else:
                cur = cur.children[cur_index]
        
        return cur.word_end # When it goes len(word) levels deep into the trie, return if last node is the end of the word or not


dictionary = open("dictionary.txt", "r")
words = dictionary.readlines()
dict_trie = Trie()

n = time.time()
for word in words:
    dict_trie.insert(word.rstrip())
print("DONE: " + str(time.time() - n))

for word in words:
    if dict_trie.find(word.rstrip()) == False:
        print("FALSE")

def generate_combinations(arr):
    for r in range(len(arr)):
        for combination in permutations(arr, r + 1):
            yield ''.join(combination)


if __name__ == "__main__":
    for combination in generate_combinations(list(sys.argv[1].rstrip())):
        if dict_trie.find(combination) and combination != sys.argv[1].rstrip():
            print(combination)