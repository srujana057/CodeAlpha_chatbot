def chatbot():
    print("🤖 Chatbot: Hi! Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi!")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm fine, thanks! 😊")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a simple chatbot.")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! 👋")
            break
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()