

def chatbot():
    print("🤖 Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()   # take input and convert to lowercase

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a simple rule-based chatbot written in Python.")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
            break
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand that. Try asking something else.")


chatbot()
