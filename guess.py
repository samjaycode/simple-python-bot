# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/19/16

#Overview:
#The computer randomly generates a number. The user inputs a number, and the computer #will tell you if you are too high, or too low. Then you will get to keep guessing #until you guess the number.

from random import randint

def g(number) :
    gen = randint(0,9)

    if number > gen :
        return str(gen) + ' to high'
    elif number < gen : 
        return str(gen) + ' to low'
    else :
        return 'correct'


