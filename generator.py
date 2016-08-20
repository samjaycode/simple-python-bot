# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/20/16

#python bot - pybot

def bot(sentence) :
    
    #unwanted chars are removed
    unwatedChars = "!@#$?,." #if users  
    for char in unwatedChars: #uses for to loop through input
        sentence = sentence.replace(char,"") #gets rid of unwanted characters
   
    #create lists of words that might be asked
    welcomeDict = ['hello', 'hi', 'welcome', 'hey', 'whats up' ] #creating a welcome dictionary
    healthDict = ['how', 'hows', 'are', 'you', 'hey', 'whats', 'up' ] #creating a asking how you are doing dictionary
    payoutDict = ['payout', 'payment', 'pay', 'money', 'my', ] # dictionary for payment

    #split up the sentence into an array
    sentence = sentence.split()

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
	 botResponse.append('We make the payout on the 1st ')
    
    finalBotResponse = ''.join(botResponse) # joins the array into a string
    
    return finalBotResponse # final response from bot

print bot('How are you? When is my payout')

