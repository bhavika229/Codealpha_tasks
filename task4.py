print("Welcome to the Chatbot! Type 'bye' to exit.")
responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a bot, but I'm good!",
    "bye": "Goodbye!"
}

while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Bot: Goodbye!")
        break
    print("Bot:", responses.get(user_input, "I don't understand that."))
