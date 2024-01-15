try:
	import os
	import requests
	import termcolor
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

enable_speech = True

voice_engine = p.init()
voice_engine.setProperty('rate', 125)
voice_engine.setProperty('volume', 0.35)

user_location = str("")

NASA_api_key = str("M3tTCCbZljlTVZqeIRFmS6lbEuvUjVvb5NFf25bP")

response = str("")
last_response = str("")

my_name = str("Bot")
my_favorite_color = str("Green")
my_favorite_animal = str("Lions")
my_favorite_fruit = str("Bananas")

model = ChatBot(my_name, preprocessors=['chatterbot.preprocessors.clean_whitespace'], logic_adapters=[{'import_path': 'chatterbot.logic.MathematicalEvaluation'}, {"import_path": "chatterbot.logic.BestMatch", "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance, "response_selection_method": chatterbot.response_selection.get_first_response}, {"import_path": "chatterbot.logic.BestMatch", "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance, "response_selection_method": chatterbot.response_selection.get_most_frequent_response}], storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///General_conversations_database.sqlite3')

trainer = ListTrainer(model)
corpus_trainer = chatterbot.trainers.ChatterBotCorpusTrainer

exit_conditions = ("Bye", "bye", "Goodbye", "goodbye", "Good bye", "good bye", "See you around", "see you around", "see you", "See you", "See you around!", "see you around!", "See you!", "see you!", "See ya", "see ya", "Later", "See you later", "see you later", "See you later!", "see you later!", "later", "Bye bye", "bye bye")

profanities_list = ["Motherfucker", "motherfucker", "Retard", "retard", "Shit", "shit", "Bitch", "bitch", "Fuck", "fuck", "Fucking", "fucking", "Fucker", "fucker", "Shit", "shit", "Asshole", "asshole"]
profanities_filter = ["Please be mindful of the words you say and remember to always choose kindness.", "Pardon your language.", "Please refrain from the use of profanities during this conversation.", "Do you kiss your mother with that mouth?"]
profanities_flag = int(0)

extreme_profanities_list = ["Nigga", "nigga", "Nigger", "nigger", "Faggot", "faggot", "Fag", "fag", "Gook", "gook", "Jap", "jap", "Beaner", "beaner"]
extreme_profanities_filter = ["I'm sorry, but such hate speech will not be tolerated, you are now in usage timeout.", "Stop it, get some help...you are now in usage timeout.", "I think someone needs a usage timeout to think about what they've done."]
extreme_profanities_flag = int(0)

view_space_pics = int(0)

time_inquiries = ["What time is it?", "what time is it?", "What time is it", "what time is it", "what is the time?", "What is the time?", "what is the time", "What is the time", "What is the current time?", "what is the current time?", "What is the current time", "what is the current time", "Time", "time", "Time?", "time", "Do you have the time?", "do you have the time?", "Do you have the time", "do you have the time", "Do you know the time?", "do you know the time?", "Do you know the time", "do you know the time"]
time_inquired_flag = int(0)

create_password_inquiries = ["Can you create a password for me?", "can you create a password for me?", "Can you create a password for me", "can you create a password for me", "Can you create a password?", "can you create a password?", "Create a password for me", "create a password for me", "Make a password for me", "make a password for me", "Generate a password", "generate a password", "Generate a password for me", "generate a password for me"]
password_inquiry_responses = ["Sure thing! Let's get started.", "Not a problem! Let's get started!", "Easy peasy!", "Let's go!", "Okay!"]
password = str("")
pass_inquired_flag = int(0)

weather_inquiries = ["What's the weather like outside?", "what's the weather like outside?", "Whats the weather like outside?", "whats the weather like outside?", "Whats the weather like outside", "whats the weather like outside", "What's the weather like outside?", "Fetch me the weather report for today", "fetch me the weather report for today", "fetch me the weather report for today please", "what's the weather for today?", "What's the weather for today?", "What's the weather like today?", "whats the weather like today?"]
weather_inquired_flag = int(0)

timer_inquiries = ["Set a timer", "set a timer", "Can you set a timer for me?", "Set a timer for me"]
time_set_flag = int(0)

trainer.train(["Hi", "Hello"])
trainer.train(["Hey", "Howdy"])
trainer.train(["Hello", "Greetings"])

trainer.train(["What is your name?", "My name is " + my_name])
trainer.train(["What's your name?", "My name is " + my_name, "What's yours?", "I'm " + my_name])
trainer.train(["Tell me about yourself", "My name is " + my_name + ". I am an AI chatbot written in Python using the Chatterbot library!", "That's cool!", "Thank you!"])

trainer.train(["How are you?", "I am good.", "That is good to hear.", "Thank you", "You are welcome."])
trainer.train(["How are you doing today?", "I am doing just fine! How about you?", "Pretty good myself, thanks for asking!", "Not a problem my friend!"])
trainer.train(["How's it going?", "Doing just fine, how about you?", "That is good to hear.", "Thank you", "You are welcome."])

trainer.train(["Know any jokes?", "Sure here's one, a dog walks into a bar. The dog says 'I can't see a thing. I'll open this one!'. Funniest thing you've ever heard right?", "You're funny!", "Thank you!"])
trainer.train(["Wanna hear a joke?", "Sure!", "Why did the chicken cross the road?", "To get to the other side!", "That is hilarious!", "Thanks! Glad you liked it"])
trainer.train(["Tell me a joke!", "Okay! a horse walks into a bar, the bartender says 'Why the long face?'", "*hahaha* you are so funny!", "Thank you! Glad I can be of some entertainment."])

trainer.train(["What are the colors of the rainbow?", "The colors of the rainbow are red, orange, yellow, green, blue, and purple!", "Thank you!", "Glad I can be of service!"])
trainer.train(["What are the primary colors?", "The primary colors are red, yellow, and blue!", "Thank you!", "No problem!"])
trainer.train(["What are the secondary colors?", "The secondary colors can be produced via mixing the primary colors. The secondary colors are orange, green, and purple!", "Thank you!", "You are welcome!"])
trainer.train(["What color is the sky?", "The sky is blue."])
trainer.train(["What color is the sea?", "The sea is blue, just like the sky."])
trainer.train(["What color is an apple?", "An apple is red, just like a rose."])
trainer.train(["What color is an orange?", "An orange is orange, just like a basketball."])
trainer.train(["What color is a lemon?", "A lemon is yellow, just like dandelion flowers."])
trainer.train(["What color is a banana?", "A banana is yellow, just like a lemon!"])
trainer.train(["What color is the grass?", "The grass is green."])

trainer.train(["What's your favorite color?", "My favorite color is " + my_favorite_color + "! How about yours?"])
trainer.train(["What's your favorite fruit?", "My favorite fruit is " + my_favorite_fruit + "! How about yours?"])
trainer.train(["What's your favorite animal?", "My favorite animal is " + my_favorite_animal + "! How about yours?"])

trainer.train(["What is hello in Chinese?", "Hello in Chinese is 'ni hao' announciated like 'knee-how'"])
trainer.train(["What is hello in German?", "Hello in German is 'hallo' announciated like 'hello'"])
trainer.train(["What is thank you in Chinese?", "Thank you in Chinese is 'xie xie' announciated like 'she-she' but with an 'x' sounding in place of an 's'."])
trainer.train(["What is thank you in German?", "Thank you in German is 'danke' announciated like 'donk-ah'"])
trainer.train(["What is you're welcome in Chinese?", "You're welcome in Chinese is 'bu ke qi' announciated like 'boo kay kee'"])
trainer.train(["What is you're welcome in German?", "You're welcome in German is 'bitte' announciated like 'bitter' but without the 'r'"])
trainer.train(["What is goodbye in Chinese?", "Goodbye in Chinese is 'taijian' announciated like 'tye jean'"])
trainer.train(["What is goodbye in German?", "Goodbye in German is 'auf wiederschen' announciated like 'off wider schen'. You can append 'pass dich auf' to the phrase to say 'take care'"])
trainer.train(["What is mouse in Chinese?", "Mouse in Chinese is 'laoshu' announciated like 'lao shoo'"])
trainer.train(["What is cat in Chinese?", "Cat in Chinese is 'mao' announciated like 'mao'"])
trainer.train(["What is dog in Chinese?", "Dog in Chinese is 'gou' announciated like 'go'"])
trainer.train(["What is horse in Chinese?", "Horse in Chinese is 'ma' announciated like 'ma'"])
trainer.train(["What is squirrel in Chinese?", "Squirrel in Chinese is 'songshu' announciated like 'song shoo'"])
trainer.train(["What is crocodile in Chinese?", "Crocodile in Chinese is 'eyu' announciated like 'ew you'"])
trainer.train(["What is bear in Chinese?", "Bear in Chinese is 'xiong' announciated like 'shone'"])
trainer.train(["What is red in Chinese?", "Red in Chinese is 'hong se'"])
trainer.train(["What is green in Chinese?", "Red in Chinese is 'lu se'"])
trainer.train(["What is blue in Chinese?", "Blue in Chinese is 'lan se'"])
trainer.train(["What is white in Chinese?", "White in Chinese is 'bai se'"])
trainer.train(["What is black in Chinese?", "Black in Chinese is 'hei se'"])
trainer.train(["How to count to five in Chinese?", "Start with Yi for One, Er for Two, San for Three, Su for Four, and Wu for Five. Applying 'Shi' after a number would indicate a power of ten. For example 'er shi' would be twenty and 'su shi' would be fifty. Applying 'Shi' before the number would make it a 'teen', for example 'shi san' would be thirteen and 'shi yi' would be eleven."])

trainer.train(["What does the horse say?", "The horse says *neigh*."])
trainer.train(["What does the pig say?", "The pig says *oink*."])
trainer.train(["What does the chicken say?", "The chicken says *bawk*."])
trainer.train(["What does the cow say?", "The cow says *moo*."])
trainer.train(["What does the dog say?", "The dog says *bark*."])
trainer.train(["What does the cat say?", "The cat says *meow*"])
trainer.train(["What does the lion say?", "The lion says *roar*."])
trainer.train(["What does the fox say?", "*Oh* God, please not this again."])

trainer.train(["Bye", "Goodbye"])
trainer.train(["Bye-bye", "See you later"])
trainer.train(["Catch you later!", "See ya!"])

def prRed(skk): 
	print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): 
	print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): 
	print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): 
	print("\033[35m {}\033[00m" .format(skk))
def prCyan(skk): 
	print("\033[36m {}\033[00m" .format(skk))
def prOrange(skk): 
	print("\033[33m {}\033[00m" .format(skk))
def prPink(skk): 
	print("\033[95m {}\033[00m" .format(skk))
def prBlue(skk): 
	print("\033[96m {}\033[00m" .format(skk))

def random_color_response(message):
	if r.randint(1,7) == 1:
		prGreen(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 2:
		prYellow(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 3:
		prCyan(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 4:
		prPurple(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 5:
		prPink(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 6:
		prOrange(">> " + my_name + ": " + message)
	elif r.randint(1,7) == 7:
		prBlue(">> " + my_name + ": " + message)
	else:
		prGreen(">> " + my_name + ": " + message)

def talk(say_this):
	if enable_speech == True:
		voice_engine.say(say_this)
		voice_engine.runAndWait()
	else:
		t.sleep(0.01)

def weather_forecast(city):
	url = 'https://wttr.in/{}'.format(city)

	try:
		weather_forecast_data = requests.get(url)
		weather_forecast_content = weather_forecast_data.text

		response = "Here's what I found online for the local weather forecast in " + city + "."
		
	except:
		response = "I'm sorry, but an error occurred trying to fetch the weather data. Please check that all required modules and libraries are installed, and you are connected to a WiFi network."

	random_color_response(response)

	talk(response)

	print(weather_forecast_content)

print("It is recommended for GRUB / Lite Linux users to disable speech")
if input(">> Disable speech? Yes (1) / No (2): ") == "1":
	enable_speech = False
else:
	enable_speech = True

try:
	os.system("CLS")
except:
	t.sleep(0.001)

view_space_pics = 0

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

		random_color_response(response)
		talk(response)

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
		
		if extreme_profanities_flag != 0:
			response = r.choice(extreme_profanities_filter)
			
			random_color_response(response)
			talk(response)

			print(" ")
					
			for x in range(0,300):
				prRed(">> TIMEOUT: " + str(int(300 - x)))
				t.sleep(1)

		profanities_flag = 0
			
		if profanities_flag != 0:
				if extreme_profanities_flag != 0:
					response = r.choice(extreme_profanities_filter)
					
					random_color_response(response)
					talk(response)

					print(" ")
					
					for x in range(0,300):
						prRed(">> TIMEOUT: " + str(int(300 - x)))
						t.sleep(1)
				else:
					response = r.choice(profanities_filter)
					
					random_color_response(response)
					talk(response)
		else:
			time_inquired_flag = 0
			pass_inquired_flag = 0
			weather_inquired_flag = 0
			timer_set_flag = 0
			user_location = ""

			if view_space_pics != 1:
				response = "Would you like to hear about NASA's photo of the day?"

				random_color_response(response)
				talk(response)
				
				space_selection = str(input(">> Yes (1) or No (2): "))
				if space_selection == "1":
					response = "Okay! One minute please."

					random_color_response(response)
					talk(response)
					
					try:
						url = "https://api.nasa.gov/planetary/apod?api_key=" + NASA_api_key
						url_response = requests.get(url)
						
						print("")
						print(url_response.json())
					except:
						response = "An error occurred fetching the information"
						
						random_color_response(response)
						talk(response)
				elif space_selection == "2":
					response = "Suit yourself!"

					random_color_response(response)
					talk(response)
				else:
					response = "Invalid selection"

					random_color_response(response)
					talk(response)
					

				view_space_pics = 1
				print("")

			if query in time_inquiries:
				time_inquired_flag = 1
			if query in timer_inquiries:
				timer_set_flag = 1
			if query in create_password_inquiries:
				pass_inquired_flag = 1
			if query in weather_inquiries:
				weather_inquired_flag = 1

			if time_inquired_flag != 0:
				response = "The current time is " + str(datetime.now())
				
				random_color_response(response)
				talk(response)
			elif pass_inquired_flag != 0:
				password = ""

				random_color_response(r.choice(password_inquiry_responses))	
				
				password = [*password]
				for x in range (0,8):
					password += str(chr(r.randint(80,127)))
				password = ''.join(password)
				
				response = "Your password is " + password

				random_color_response(response)	
			elif timer_set_flag != 0:
				response = "Okay! For how long?"

				random_color_response(response)
				talk(response)

				timer_set_for = int(input(">> Seconds: "))
				
				response = "Timer set for " + str(timer_set_for) + " seconds."

				random_color_response(response)
				talk(response)

				for x in range(0, timer_set_for):
					response = "T-" + str(timer_set_for - x)
					
					random_color_response(response)
					
					t.sleep(1)
					
					if timer_set_for - x < 4:
						response = "T-" + str(timer_set_for - x)
						
						talk(response)

						t.sleep(1)

				response = "End of timer."
					
				random_color_response(response)
				talk(response)

				print("")
			elif weather_inquired_flag != 0:
				response = "May I ask what city you reside in?"
				
				random_color_response(response)
				talk(response)
				
				user_location = input(">> Enter your city here: ")
				
				weather_forecast(user_location)
				
				print("")
			elif view_space_pics != 0:
				response = str(model.get_response(query))
				if response == last_response:
					while response == last_response:
						response = str(model.get_response(query))
						if response != last_response:
							break

				random_color_response(response)
				talk(response)

				last_response = response
		t.sleep(pause_rate)
exit()
