# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/20/16

#python ai pot - pybot

def g(sentence) :

    unwatedChars = "!@#$" #keep adding to this 
    for char in unwatedChars: #uses for to loop through input
        sentence = sentence.replace(char,"") #gets rid of unwanted characters

    welcomeDict = ['hello', 'hi', 'welcome', 'hey', 'whats up' ] #creating a welcome dictionary
    healthDict = ['how are you', 'hows it going', 'whats new', 'hey', 'whats up' ] #creating a asking how you are doing dictionary
    
    if sentence in welcomeDict:
        return 'hi back'
    elif sentence in healthDict:
	 return 'I am well, thanks!'

print g('hi!')

