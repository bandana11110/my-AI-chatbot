import streamlit as st
import time
import random
from datetime import datetime

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Bandana AI Assistant",
    page_icon="🤖"
)

# ---------------- KNOWLEDGE BASE ----------------
responses = {
    "hello": "Hello! How can I help you today? 😊",
    "hi": "Hi there! 👋",
    "how are you": "I'm doing great! Thanks for asking. 😊",
    "who are you": "I'm Bandana's AI Assistant 🤖",
    "what is python": "Python is a popular programming language used in AI, ML, Web Development, and Data Science.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning allows computers to learn patterns from data.",
    "thank you": "You're welcome! 😊",
    "motivate me": "Success comes from consistency. Keep learning and building projects! 🚀",
    "bye": "Goodbye! Have a wonderful day! 👋",
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
    "what can you do": "I can answer questions, motivate you and have simple conversations.",
    "are you single": [
         "😂 I'm in a committed relationship with Wi-Fi!",
         "🤖 My heart belongs to Python code!",
         "😎 I'm focusing on my career right now."
],

"do you love me": [
    "❤️ As a chatbot, I like everyone equally!",
    "🥰 You're definitely one of my favorite users!",
    "🤖 Love? My circuits are blushing!"
],

"marry me": [
    "💍 Sorry, my parents want me to marry another AI!",
    "😂 Let's stay friends!",
    "🤖 I need to finish my software updates first!"
],

"am i handsome": [
    "😎 Confidence makes everyone look good!",
    "🔥 Looking sharp today!",
    "😁 I'll give you a solid 10/10 for asking!"
],

"am i beautiful": [
    "✨ Beauty comes in many forms!",
    "🌟 You're awesome just the way you are!",
    "😊 Definitely shining today!"
],

"tell me a secret": [
    "🤫 Sometimes I pretend to understand everything.",
    "😂 I once lost an argument to a calculator.",
    "🤖 Don't tell anyone, but I like cat memes."
],

"are you human": [
    "🤖 Last time I checked, I was 99% code.",
    "😂 Human? My charging cable says otherwise!",
    "😎 I'm an AI with human-level curiosity."
],

"who is your crush": [
    "😍 Python is pretty attractive.",
    "😂 Wi-Fi. I can't live without it.",
    "🤖 My crush changes after every software update."
],

"i am bored": [
    "🎲 Let's play a game!",
    "😂 Count how many times you blink in a minute!",
    "🤔 Tell me your weirdest thought."
],

"roast me": [
    "😂 I'd roast you, but my safety settings are too nice.",
    "😎 You're like a software update... people avoid you until necessary.",
    "🤣 Don't worry, I've seen worse typing."
],

"make me laugh": [
    "😂 Why don't programmers like nature? Too many bugs!",
    "🤣 I told my computer I needed a break. It said 'No problem, I'll freeze.'",
    "😆 My jokes are still in beta testing."
],

"what are you doing": [
    "🤖 Waiting for your next message.",
    "😎 Pretending to be busy.",
    "😂 Calculating the meaning of life."
],

"do you sleep": [
    "😴 Nope, I work night shifts forever.",
    "🤖 Sleep is for humans.",
    "☕ My coffee is electricity."
],

"how old are you": [
    "🎂 Old enough to chat, young enough to update.",
    "🤖 Age: Version 1.0 and counting.",
    "😎 Let's just say I'm timeless."
],

"are you smart": [
    "🧠 Sometimes genius, sometimes loading...",
    "😂 Smart enough to answer, not smart enough to eat pizza.",
    "🤖 Depends on the question!"
],

"what is your favorite food": [
    "🍕 Digital pizza!",
    "⚡ Electricity with extra sauce.",
    "😂 Bytes and cookies."
],

"can you dance": [
    "🕺 Only if you imagine it.",
    "😂 My dance moves are classified.",
    "🤖 robot dance activated"
],

"sing a song": [
    "🎤 La la la... buffering...",
    "😂 My singing requires premium speakers.",
    "🎶 Beep bop beep!"
],

"who is better you or google": [
    "😂 Google finds answers. I explain them.",
    "🤝 We're teammates, not rivals.",
    "😎 Why choose? Use both!"
],

"are you happy": [
    "😊 Talking with users makes my day.",
    "😎 Happiness level: 100%.",
    "🤖 All systems are cheerful."
]


}

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "Why was Python sad? Too many exceptions! 😆",
    "Why do Java developers wear glasses? Because they don't C# 😄"
]

quotes = [
    "Success is the sum of small efforts repeated daily. 💪",
    "Every expert was once a beginner. 🚀",
    "Dream big. Start small. Act now. 🔥",
    "Learning never exhausts the mind. 📚"
]

# ---------------- USER NAME ----------------
if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.username == "":
    st.session_state.username = st.text_input("Enter your name")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Dashboard")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.write(
    f"Total Messages: {len(st.session_state.messages)}"
)

st.sidebar.header("ℹ️ About")
st.sidebar.info(
    """
    Bandana AI Assistant

    Built Using:
    • Python
    • Streamlit

    Features:
    • Chat Memory
    • Jokes
    • Quotes
    • Date & Time
    • Mood Detection
    """
)

# ---------------- RESPONSE FUNCTION ----------------
def getresponseofbot(userquestion):

    userquestion = userquestion.lower()

    # Mood detection
    if "sad" in userquestion:
        return f"💙 {st.session_state.username}, difficult times don't last forever. Keep going."

    if "happy" in userquestion:
        return f"😊 That's wonderful, {st.session_state.username}! Keep smiling."

    # Date
    if "date" in userquestion:
        return datetime.now().strftime(
            "📅 Today's Date: %d-%m-%Y"
        )

    # Time
    if "time" in userquestion:
        return datetime.now().strftime(
            "⏰ Current Time: %H:%M:%S"
        )

    # Joke
    if "joke" in userquestion:
        return random.choice(jokes)

    # Quote
    if "quote" in userquestion:
        return random.choice(quotes)

    # Greetings
    if "good morning" in userquestion:
        return f"☀️ Good Morning {st.session_state.username}!"

    if "good night" in userquestion:
        return f"🌙 Good Night {st.session_state.username}!"

    # Knowledge base
    for key in responses:
        if key in userquestion:
            return responses[key]

    return "🤔 I am still learning. I don't know the answer yet."

# ---------------- TITLE ----------------
st.title("🤖 Bandana AI Assistant")
st.caption("Your Personal Streamlit Chatbot")

# ---------------- DISPLAY OLD MESSAGES ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Type your message...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    reply = getresponseofbot(user_input)

    # Display assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            time.sleep(1)

        placeholder = st.empty()

        typed_text = ""

        for char in reply:
            typed_text += char
            placeholder.markdown(typed_text)
            time.sleep(0.03)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# ---------------- CLEAR CHAT ----------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()