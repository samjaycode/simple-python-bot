# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/20/16

#python bot - pybot

def bot() :
    
    name = raw_input('Hi, I\'m Snappy! What is your name? ')
    
    email = raw_input('Right on, ' + name + '! What\'s your email? ')

    sentence = raw_input('' + email + '.. sweet email! How can I help? ') # asks the question
    
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
    pricingDict = ['cost', 'pricing', 'price'] # dictionary for pricing
   
    #checks for any common values
    welcomeResult = len(set(welcomeDict).intersection(sentence))
    healthResult = len(set(healthDict).intersection(sentence))
    payoutResult = len(set(payoutDict).intersection(sentence))
    pricingResult = len(set(pricingDict).intersection(sentence))

    botResponse = [] # creates a list

    responseCount = 0 # creates a list

    botResponse.append(name + ', ')

    #checks to see if the bot can answer
    if welcomeResult > 0:
        botResponse.append('how can I help? ')
        responseCount += 1
    if healthResult > 1 :
	    botResponse.append('I am well, thanks! ')
    if pricingResult > 0 :
        botResponse.append('logo contests cost $100. You can see a list of all the pricing on our pricing page ')
        responseCount += 1
    if payoutResult > 0 :
	    botResponse.append('we make the payout on the 1st. ')

    # checks to see if the bot answered any questions
    if(responseCount or payoutResult != 0 or healthResult != 0): #if the bot did answer
        botResponse.append('if you still have any questions send us an email. ')
    else: # if it doesn't answer
        botResponse.append('we will get back to you shortly with an answer. ')

    finalBotResponse = ''.join(botResponse) # joins the array into a string
    
    return finalBotResponse # final response from bot

print bot()

