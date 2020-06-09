# How to solve graph problem
# 1. Translate the problem into graph terminology
# 2. Build the graph
# 3. Traverse/search

# Problem
# Given two words (begin_word and end_word), and a list of English words, return
# the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not
# a transformed word.

# begin: hit

# end:   cog

# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

import string
import os
import sys


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()

with open(os.path.join(sys.path[0], 'words.txt'), 'r') as f:
    for line in f:
        line = line.strip()
        word_set.add(line.lower())

letters = list(string.ascii_lowercase)


def get_neighbors(word):
    neighbors = []

    word_letters = list(word)

    # for each letter in the word
    for i in range(len(word_letters)):
        # replace with all english letters
        for letter in letters:
            # copy the word letters
            t = list(word_letters)

            t[i] = letter
            # [w, o, r, d]
            w = "".join(t)
            # word
            # see if we form a word
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


def find_word_ladders(begin_word, end_word):
    visited = set()

    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        cur_word = path[-1]  # get last node out of the path

        if cur_word not in visited:
            visited.add(cur_word)

            if cur_word == end_word:
                return path

            for neighbor in get_neighbors(cur_word):
                path_copy = list(path)  # copy the list so far
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


print(find_word_ladders('spam', 'salt'))
