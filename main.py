#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In this program, we will be moving through each line backwards, meaning we will be finding optimal solutions by starting at the end of the word and checking along
# the way whether the word is legal, meaning it belongs to the set of words. If a new word gives us a more optimal solution, we will store the starting index of
# the word in the id_first_words array. To read the most optimal solution, we will need to traverse this array starting from 0 (the length of the first word in
# the most optimal situation), jumping through it according to the length of the words stored in it.
import time
start_time = time.time()
global maxsentence


def Pod(n, word, set_words):
    global maxsentence
    i = n-1
    len = []  # table sum of squares length words
    id_first_words = []
    for k in range(1, n+2):
        len.append(-1)
        id_first_words.append(-1)
    len[n] = 0
    while i >= 0:
        j = 0
        while j+i < n:
            new_s = word[i:i+j+1]
            # j+1 - the length of the new word, len[i+j+1] - the largest sum of the squares of word lengths from the index i+j+1 upwards so far
            leng = ((j+1)*(j+1)) + len[i+j+1]
            if new_s in set_words and len[i+j+1] != -1 and (leng > len[i] or len[i] == -1):
                len[i] = leng
                id_first_words[i] = j+1
            j = j+1
        i = i-1
    i = 0
    while i < n:
        maxsentence.append(word[i:i+id_first_words[i]])
        i = i+id_first_words[i]


def Maximalize(line, set_words):
    Pod(len(line), line, set_words)
    last_id = len(maxsentence)-1
    last_word = maxsentence[last_id]
    maxsentence.pop(last_id)
    res = ''
    for i in maxsentence:
        res = res + i + ' '
    res = res+last_word
    return res


with open('zad2_input.txt', encoding="utf8") as file:
    with open('words_for_ai.txt', encoding="utf8") as file2:
        set_words = set()
        for word in file2:
            word = word.rstrip("\n")
            set_words.add(word)
    for line in file:
        file = open("zad2_output.txt", "a", encoding="utf8")
        maxsentence = []
        line = line.rstrip("\n")
        print(Maximalize(line, set_words), file=file)
        file.close()
print("--- %s seconds ---" % (time.time() - start_time))
