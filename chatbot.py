answers = {
    "hi": "Hey there !",
    "hey": "Hey there !",
    "hello": "Hey there !",
    "how are you": "I'm fine",
    "your name": "I am a Bot",
    "what is your name": "I am a Bot",
    "what is python": "Python is a interpreted programming langauge ,used for various task and projects.",
    "python": "Python is a interpreted programming langauge ,used for various task and projects.",
    "bye": "Goodbye !",
    "goodbye": "Goodbye !",
    "exit": "Goodbye !",
}

while True:
    user_input = input("User : ").lower().strip()
    reply = answers.get(user_input, "I don't understand !")

    print(f"Bot : {reply}")

    if user_input in ("bye", "goodbye", "exit"):
        break
