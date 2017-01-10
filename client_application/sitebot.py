import apiai
import json
import requests
import random

CLIENT_ACCESS_TOKEN = '7164e74cc3d9448ea39e7a20d4efced1'
SESSION_ID = 12345

ai =apiai.ApiAI(CLIENT_ACCESS_TOKEN);

def print_bot_message(message):
    print "Bot  ::  "+message

#Intro message
#print_bot_message("Hi for now I am an echo bot I am gonna just repeat what you say !!\
#    if you are tired of me just say 'exit'")

def call_apiai(message):
    	request =ai.text_request()
    	request.session_id = SESSION_ID
    	request.query = message
    	response = request.getresponse()
    	raw_response = response.read()
    	response = json.loads(raw_response)
    	return response

while True:
    message = raw_input("User ::  ")
    if message.lower() == "exit":
        print_bot_message("Bye !! take care")
        exit()
    else:
	response = call_apiai(message)
        if response ["status"]["code"] == 200:
            reply_message = response["result"]["fulfillment"]["speech"]
        else:
            reply_message = "Sorry , I could not connect to api.ai"
        print_bot_message(reply_message)
    
