# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:19:34 2018

@author: adminuser
"""
import re

# Define variables
name = "ShenJi"
weather = "cloudy"

bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a dictionary with the predefined responses
responses = {
  "askname": "my name is {0}".format(name),
  "askweather": "the weather is {0}".format(weather),
  "default": "default message",
  "greet":"nice to meet you {0}".format(name),
  "goodbye": "See U later, Bye!",
  "thankyou": "My pleasure"
}

patterns = {
    'askname': re.compile(r'what|name', re.UNICODE),
    'askweather': re.compile(r'weather|today', re.UNICODE),
    'goodbye': re.compile(r'bye|farewell', re.UNICODE), 
    'greet': re.compile(r'hello|hi|hey', re.UNICODE), 
    'thankyou': re.compile(r'thank|thx', re.UNICODE)}

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    
    
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define find_name()
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call|called')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name

# Return the matching response if there is one, default otherwise
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Send messages
send_message("hello! BOT")
send_message("what's your name?")
send_message("what's the weather today?")
send_message("thanks very much!")