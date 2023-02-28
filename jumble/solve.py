# import time
# import sys


# class TrieNode:
#     def __init__(self):
#         self.children = [None for i in range(26)]
#         self.word_end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
   
#     def char_to_index(self, char):
#         return ord(char) - ord('a')
    
#     def insert(self, word):
#         cur = self.root
#         for letter in word:
#             cur_index = self.char_to_index(letter)
#             if cur.children[cur_index] == None:
#                 cur.children[cur_index] = TrieNode()

#             cur = cur.children[cur_index]
                

#         cur.word_end = True
    
#     def is_a_word(self, word):
#         cur = self.root
#         for letter in word:
#             cur_index = self.char_to_index(letter)
#             if cur.children[cur_index] == None:
#                 return False
#             else:
#                 cur = cur.children[cur_index]
        
#         return cur.word_end # When it goes len(word) levels deep into the trie, return if last node is the end of the word or not
    
#     def is_set(self, word):
#         cur = self.root
#         for letter in word:
#             cur_index = self.char_to_index(letter)
#             if cur.children[cur_index] == None:
#                 return False
#             else:
#                 cur = cur.children[cur_index]
        
#         return True



# dictionary = open("dictionary.txt", "r")
# words = dictionary.readlines()
# dict_trie = Trie()

# n = time.time()
# for word in words:
#     dict_trie.insert(word.rstrip())
# print("DONE: " + str(time.time() - n))


def generate_combinations(cur, options):
    print("Entering")
    print("CURRENT ", cur)
    for i in range(0, len(options)):
        new_cur = cur + options[i]
        new_options = options[i:]
        print(new_cur, new_options)
        generate_combinations(new_cur, new_options)
       

if __name__ == "__main__":
    print("H")
    generate_combinations("", "dog")