# Artificially Intelligent Chatbot

! NOTE : MAY BE INCOMPATIBLE WITH NEWER VERSIONS OF PYTHON !

An artificially intelligent 'chatbot' written in Python using the Chatterbot module / library. This CLI based chatbot provides entertaining replies with text to speech responses powered by PYTTSX3.
Additional features include: the ability to answer simple current time or math inquiries, fetch the local weather forecast, provide the time, create random passwords, set timers, as well as a built-in profanities filter and user time-out on extreme profanities such as racial slurs.

Features List:
  * AI generated text & voice responses
  * Offers to view NASA's photo of the day
  * Fetch Current Date & Time #Try asking 'what time is it?'
  * Fetch local weather forecast #Try asking 'what's the weather like outside?'
  * Answer simple math questions involving addition, subtraction, multiplication, and / or division #Try asking 'What is two times seven?'
  * Can generate random passwords #Try asking 'create a password'
  * Can set a timer for the user #Try asking 'set a timer'
 *  Built-In profanities filter (with extreme profanities punishable by a usage timeout)
 *  Built-In filter for repetitive responses
 *  Knowledgable of Basic Color Theorem
 *  Peak Ancient Sumerian humor #Ask if they know any jokes ;)
 *  Colorful text responses
 *  Simple object colors
 *  Simple animal sounds
 *  Simple Chinese and German phrases #Try asking 'What is cat in Chinese?'
  
Required Modules / Library:
 * Os  #Used to clear the terminal output after load list trainers
 * Requests #To fetch data from the web
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
