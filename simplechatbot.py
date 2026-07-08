def get_bot_reply(user_input):
    user_input = user_input.lower().strip()
    
    # Dictionary of rules for easier management
    responses = {
        "hi": "Hello there! How's your day going?",
        "hello": "Hi! It's a pleasure to chat with you.",
        "how are you": "I'm just a bunch of code, but I'm functioning perfectly! How about you?",
        "what is your name": "I am ChatBot Y0, your virtual assistant.",
        "i am fine": "That's great to hear! Anything interesting happening today?",
        "i am sad": "I'm sorry to hear that. Remember that I'm here to chat if you need to vent!",
        "bye": "Goodbye! Take care and have a wonderful day!",
        "thank you": "You're very welcome!"
    }
    
    # Check if input matches any key
    for key in responses:
        if key in user_input:
            return responses[key]
            
    return "That's interesting! Tell me more about that."

def start_chat():
    print("--- Bot: Hello! I'm ready to chat. (Type 'bye' to exit) ---")
    
    while True:
        user_message = input("You: ")
        
        reply = get_bot_reply(user_message)
        print(f"Bot: {reply}")
        
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    start_chat()