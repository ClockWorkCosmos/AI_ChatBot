# Artificially Intelligent Chatbot

An artificially intelligent 'chatbot' written in Python using the Chatterbot module / library. This CLI based chatbot provides entertaining replies with text to speech responses powered by PYTTSX3.
Additional features include the ability to answer simple current time or math inquiries, as well as a built-in profanities filter and user time-out on extreme profanities such as racial slurs.

Features List:
  * AI Generated Text & Voice Responses
  * Fetch Current Date & Time
  * Answer Simple Math Questions Involving Addition, Subtraction, Multiplication, and / or Division
 *  Built-In Profanities Filter (with extreme profanities punishable by a usage timeout)
 *  Built-In Filter for Repetitive Responses
 *  Knowledgable of Basic Color Theorem
 *  Peak Ancient Sumerian Humor #ask if they know any jokes ;)
  
Required Modules / Library:
 * Os  #Used to clear the terminal output after load list trainers
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
