# Task 1: Rule-Based Chatbot
# CODSOFT AI Internship

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great 😊 Thanks for asking!"

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot created for the CODSOFT AI Internship."

    elif "help" in user_input:
        return "Sure! You can ask me about my name, how I work, or say hello."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Please try something else."


print("🤖 Chatbot is running (type 'bye' to exit)")

while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("Bot:", reply)

    if "bye" in user.lower() or "exit" in user.lower():
        break
