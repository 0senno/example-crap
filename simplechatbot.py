import random

def get_response(user_input):
    responses = {
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
        "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
        "name": ["My name is ChatBot.", "You can call me ChatBot.", "I'm ChatBot!"],
        "age": ["I don't have an age. I'm just a program.", "Age is just a number for me."],
        "favorite color": ["I don't have a favorite color. I'm a bot!", "I don't see colors, unfortunately."],
        "thanks": ["You're welcome!", "No problem!", "Anytime!"],
        "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."]
    }
    
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

def main():
    print("Welcome to ChatBot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
