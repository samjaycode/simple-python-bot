# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/20/16

#python bot - pybot

def bot() :
    
    import nltk

    sentence = raw_input('sweet email! How can I help? ') # asks the question

    tokens = nltk.word_tokenize(sentence)

    return nltk.pos_tag(tokens)

print bot()

