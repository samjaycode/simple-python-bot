# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/20/16

#python bot - pybot

def bot(sentence) :
    
    unwantedChars = "!@#$?,." #unwanted chars are removed

    for char in unwantedChars: # uses a for loop to go through the input
        sentence = sentence.replace(char,"") # gets rid of unwanted characters

    #split up the sentence into an array and make all characters lower case
    sentence = sentence.lower()
    sentence = sentence.split()
 
    #create lists of words that might be asked
    welcomeDict = ['hello', 'hi', 'welcome', 'hey', 'whats up' ] # creating a welcome dictionary
    healthDict = ['how', 'hows', 'are', 'you', 'hey', 'whats', 'up' ] # creating a asking how you are doing dictionary
    payoutDict = ['payout', 'payment', 'pay', 'money', 'my', ] # dictionary for payment
   
    #checks for any common values
    welcomeResult = len(set(welcomeDict).intersection(sentence))
    healthResult = len(set(healthDict).intersection(sentence))
    payoutResult = len(set(payoutDict).intersection(sentence))
  
    botResponse = [] # creates a list

    if welcomeResult > 0:
        botResponse.append('Hello back. How can I help? ')
    if healthResult > 1 :
	 botResponse.append('I am well, thanks! ')
    if payoutResult > 1 :
	 botResponse.append('We make the payout on the 1st. ')

    botResponse.append('If you still have any questions send us an email. ')
    
    finalBotResponse = ''.join(botResponse) # joins the array into a string
    
    return finalBotResponse # final response from bot

print bot('How are you. I need my payout')

