try:
	import os
	import sys
	import termcolor
	import math as m
	import pyttsx3 as p
	import random as r
	import datetime
	import time as t
	import chatterbot
	from chatterbot import ChatBot
	from chatterbot import trainers
	from chatterbot.trainers import ListTrainer
	from chatterbot.comparisons import LevenshteinDistance
	from chatterbot.response_selection import get_most_frequent_response
	from termcolor import colored, cprint
	from datetime import datetime
except:
	print(">> Required libraries and modules not installed. Please install all requirements listed in the README file from the command line. Thank you. The program will exit in T-5...")
	t.sleep(5)
	exit()

pause_rate = float(0.25)

voice_engine = p.init()
voice_engine.setProperty('rate', 125)
voice_engine.setProperty('volume', 0.35)

response = str("")
last_response = str("")

my_name = str("Bot")
model = ChatBot(my_name, preprocessors=['chatterbot.preprocessors.clean_whitespace'], logic_adapters=[{'import_path': 'chatterbot.logic.MathematicalEvaluation'}, {"import_path": "chatterbot.logic.BestMatch", "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance, "response_selection_method": chatterbot.response_selection.get_first_response}], storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///Database.sqlite3')
trainer = ListTrainer(model)
corpus_trainer = chatterbot.trainers.ChatterBotCorpusTrainer
exit_conditions = ("Bye", "bye", "Goodbye", "goodbye", "See ya", "see ya", "Later", "See you later", "see you later", "See you later!", "see you later!", "later", "Bye bye", "bye bye")

profanities_list = ["Shit", "shit", "Bitch", "bitch", "Fuck", "fuck", "Fucking", "fucking", "Fucker", "fucker", "Shit", "shit", "Asshole", "asshole", "Nigga", "nigga", "Nigger", "nigger", "Faggot", "faggot", "Fag", "fag", "Gook", "gook", "Jap", "jap", "Beaner", "beaner"]
extreme_profanities_list = ["Nigga", "nigga", "Nigger", "nigger", "Faggot", "faggot", "Fag", "fag", "Gook", "gook", "Jap", "jap", "Beaner", "beaner"]
profanities_filter = ["Please be mindful of the words you say and remember to always choose kindness.", "Pardon your language.", "Please refrain from the use of profanities during this conversation.", "Do you kiss your mother with that mouth?"]
extreme_profanities_filter = ["I'm sorry, but such hate speech will not be tolerated, you are now in usage timeout.", "Stop it, get some help....you are now in usage timeout.", "I think someone needs a usage timeout to think about what they've done."]
profanities_flag = int(0)
extreme_profanities_flag = int(0)

time_inquired_flag = int(0)
time_inquiries = ["What time is it?", "what time is it?", "What time is it", "what time is it", "What is the current time?", "what is the current time?", "What is the current time", "what is the current time", "Time", "time", "Time?", "time", "Do you have the time?", "do you have the time?", "Do you have the time", "do you have the time", "Do you know the time?", "do you know the time?", "Do you know the time", "do you know the time"]

trainer.train(["Tell me about yourself", "My name is " + my_name + ". I am a chatbot written in Python using the Chatterbot library!", "Know any jokes?", "Sure here's one, a dog walks into a bar. The dog says 'I can't see a thing. I'll open this one!'. Funniest thing you've ever heard right?"])
trainer.train(["What are the colors of the rainbow?", "The colors of the rainbow are red, orange, yellow, green, blue, and purple!"])
trainer.train(["What are the secondary colors?", "The secondary colors can be produced via mixing the primary colors. The secondary colors are orange, green, and purple!", "What are the primary colors?", "The primary colors are red, yellow, and blue!"])
trainer.train(["What's your favorite color?", "My favorite color is green! How about yours?"])
trainer.train(["What color is the sky?", "The sky is blue."])
trainer.train(["What does the dog say?", "The dog says *bark*."])
trainer.train(["What does the cat say?", "The cat says *meow*"])
trainer.train(["What does the fox say?", "*Oh* God, please not this again."])
trainer.train(["What is your name?", "My name is " + my_name])
trainer.train(["Hi", "Hello"])
trainer.train(["Hey", "Howdy"])
trainer.train(["Hello", "Greetings"])
trainer.train(["Bye", "Goodbye"])
trainer.train(["Bye-bye", "See you later"])
trainer.train(["How are you?", "I am good.", "That is good to hear.", "Thank you", "You are welcome."])
trainer.train(["How's it going?", "Doing just fine, how about you?", "That is good to hear.", "Thank you", "You are welcome."])

def prRed(skk): 
	print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): 
	print("\033[92m {}\033[00m" .format(skk))

try:
	os.system("CLS")
except:
	t.sleep(0.001)

while True:
	profanities_flag = 0
	response = ""
	
	query = input(">> You: ")
	t.sleep(pause_rate)

	if query in exit_conditions:
		response = r.choice(["Bye", "Goodbye", "See you later"])
		if response == last_response:
			while response == last_response:
				response = str(model.get_response(query))
				if response != last_response:
					break

		prGreen(">> " + my_name + ": " + response)
		voice_engine.say(response)
		voice_engine.runAndWait()
		t.sleep(1)
		break
	else:
		query = query.split(" ")

		for x, _ in enumerate(query):
			if query[x] in profanities_list:
				profanities_flag = 1

				if query[x] in extreme_profanities_list:
					extreme_profanities_flag = 1
		query = ' '.join(query)

		if profanities_flag != 0:
				if extreme_profanities_flag != 0:
					response = r.choice(extreme_profanities_filter)
					prGreen(">> " + my_name + ": " + response)
					voice_engine.say(response)
					voice_engine.runAndWait()

					print(" ")
					for x in range(0,300):
						prRed(">> TIMEOUT: " + str(int(300 - x)))
						t.sleep(1)
				else:
					response = r.choice(profanities_filter)
					prGreen(">> " + my_name + ": " + response)
					voice_engine.say(response)
					voice_engine.runAndWait()
		else:
			time_inquired_flag = 0

			if query in time_inquiries:
				time_inquired_flag = 1

			if time_inquired_flag != 0:
				response = "The current time is " + str(datetime.now())
				prGreen(">> " + my_name + ": " + response)
				voice_engine.say(response)
				voice_engine.runAndWait()
			else:
				response = str(model.get_response(query))
				if response == last_response:
					while response == last_response:
						response = str(model.get_response(query))
						if response != last_response:
							break

				prGreen(">> " + my_name + ": " + response)
				voice_engine.say(response)
				voice_engine.runAndWait()
				last_response = response

		t.sleep(pause_rate)
exit()