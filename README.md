# Artificially Intelligent Chatbot

! NOTE : MAY BE INCOMPATIBLE WITH NEWER VERSIONS OF PYTHON !

An artificially intelligent 'chatbot' written in Python using the Chatterbot module / library. This CLI based chatbot provides entertaining replies with text to speech responses powered by PYTTSX3.
Additional features include the ability to answer simple current time or math inquiries, as well as a built-in profanities filter and user time-out on extreme profanities such as racial slurs.

Features List:
  * AI generated text & voice responses
  * Fetch Current Date & Time #Try asking 'what's the weather like outside?'
  * Fetch local weather forecast
  * Answer simple math questions involving addition, subtraction, multiplication, and / or division
 *  Built-In profanities filter (with extreme profanities punishable by a usage timeout)
 *  Built-In filter for repetitive responses
 *  Knowledgable of Basic Color Theorem
 *  Peak Ancient Sumerian humor #Ask if they know any jokes ;)
 *  Colorful text responses
  
Required Modules / Library:
 * Os  #Used to clear the terminal output after load list trainers
 * Requests #To fetch weather data from the web
 * Termcolor  #Differiantates chatbot replies from user replies with color for its text
 * Pyttsx3  #Converts text responses to speech
*  Random  #Used for the random selection of some responses
 * Datetime  #Used for fetching the current date and time upon user request
 * Time  #Provides a pause time between replies as well as usage time out on extreme profanities
 * Chatterbot  #The primary module of this program

Data Preprocessors:
 * Clean Whitespace

Logic Adapters:
 * BestMatch
 * Mathematical Evaluation

Storage Adapters:
 * SQL Storage Adapter
