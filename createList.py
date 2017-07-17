from collections import OrderedDict
import re

#------------------------
# shared variables:
#------------------------

words = OrderedDict()

outputFilename = 'output.txt'

filename1 = 'data.txt'

allophones = {
    'aeiou' : 'a',
    'bp' : 'b',
    'cjsz' : 'z',
    'dt' : 'd',
    'fv' : 'v',
    'gkq' : 'g',
    'hx' : 'h',
    'lr' : 'l',
    'mn' : 'm',
    'w' : 'w',
    'y' : 'y'
    }

#------------------------
# functions:
#------------------------

def initialSyllablePlusInitialVowel(word):
    if word:
        for i in range(1,len(word)): # first letter can be a vowel
            letter = word[i]
            if letter in 'aeiou':
                return word[:i+2]
    return word

def joinOverlappingAllophones(word1,word2):
    if word1 and word2:
        # find letter in allophone dictionary
        for entry in allophones:
            if word1[-1] in entry:
                if word2[0] in entry:
                    return word1[:-1] + word2
    return word1 + word2

def createWord(words):
    newWord = ''
    for language in words:
        if language != 'Eng':
            word2 = initialSyllablePlusInitialVowel(words[language])
            newWord = joinOverlappingAllophones(newWord, word2)
    return newWord

#------------------------
# main part of the program:
#------------------------

# get lines of file into a list:
with open(filename1,'r') as f1:
    data = f1.readlines()

# get language headers:
langs = data[0].replace(',\n','').split(',')[1:] # "0,Eng,...,...,...," -> "..., ..., ..." (no 'Eng' and no final comma or '\n')

# put those language headers into the ordered dictionary:
for lang in langs:
    words[lang] = ''

# fill arrays:
for line in data:
    i = 0
    for lang in words:
        i += 1
        words[lang] = line.split(',')[i]
    originalWords = words.copy()
    originalWords_Alt = words.copy()
    if words['Eng'] != 'Eng':
        newWord = createWord(words) # here is the major function call!

        # write to file
        with open(outputFilename,'a') as f2:
            entry = newWord.strip()
            for lang in langs:
                entry += ',' + originalWords[lang]
            entry += ',\n'
            f2.write(entry)
