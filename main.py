# rule based AI python chatbot

import datetime
import time

name = input("hiii welcome,enter your name:")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print("good morning,",name)
elif 11 <= presenthour <= 17:
    print("good afternoon,",name)
elif 17 <= presenthour <= 20:
    print("good evening,",name)
else:
    print("good night,",name)




print("Hello! welcome to your chatbot")
print("you can ask me any questions,Type 'bye' to exit from the bot")

#chatbot memory creation [ dictionary of responses]

Responses = {
    "hello": "hi , welcome. how can i help you",
    "how are you": "I am fine.what about you?",
    "who are you": "i am your  AI buddy",
    "motivate me": "keep going. Every bug of your project will make you a better developer",
    "happy": "great to hear that",
    "what's your favourite dilouge": "insaan jab gareeb ho🤣",
    "sad": "I am sorry you're feeling sad. Remember, tough times don't last forever. 💙",
    "what is python": "Python is a popular programming language used in AI, ML, Data Science and Web Development.",
    "what is machine learning": "Machine Learning enables computers to learn from data.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who created python": "Python was created by Guido van Rossum.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
    "good morning": "Good Morning! Have a productive day.",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a great day.",
    "your favourite language": "I like Python because it is simple and powerful.",
    "what can you do": "I can answer questions, motivate you and have simple conversations."

}

#method/function to get response of chatbot

def getresponseofbot(userquestion):
    userquestion = userquestion.lower()

    

    # Special mood detection
    if "sad" in userquestion:
        return "You seem sad. Don't give up. Every challenge teaches something valuable. 💙"

    if "happy" in userquestion:
        return "That's wonderful! Keep spreading positivity. 😊"


    for eachkey in Responses: 
        if eachkey in userquestion:
            return Responses[eachkey]
        
    return "I am not able to tell that yet.still in learning mood"
    
# take user input



while True:
    userinput = input("please ask your question:")

    print("Bot is thinking...")
    time.sleep(1)

    reply = getresponseofbot(userinput)
    print("bot response:", reply)

    if "bye" in userinput.lower():
        break