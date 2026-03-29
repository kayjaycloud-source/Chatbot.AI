def chatbot():
    print("Hello! I'm a chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm not sure how to help with that. Please try again.")

if __name__ == "__main__":
    chatbot()   