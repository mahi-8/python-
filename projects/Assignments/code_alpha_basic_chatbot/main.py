# Basic Chat Bot using Rule-Based Approach
# Chat bot Memory Creation (Dictionary of responses)

responses = {
    "hello": "Hi there! Welcome. How can I assist you today? 👋",
    "hi": "Hello! What can I do for you? 😊",
    "how are you": "I am a helpful assistant, so I'm always ready to work! ⚙️ How are you?",
    "what is your name": "I am a rule-based assistant designed to help with information. 🤖",
    "what time is it": "I don't have real-time access ⏳, but I can look up the time for a city if you ask!",
    "thank you": "You're welcome! Happy to help. 👍",
    "bye": "Goodbye! Have a great day. 👋",
    "what is python": "Python is a high-level, interpreted programming language known for its readability. 🐍",
    "rules": "My rules are simple: I look for keywords and phrases to give a predefined response. 📜",
    "help": "I can answer questions about Python, tell you about my rules, or just chat! 💬",
    "favorite color": "As an assistant, I don't have a favorite color, but I like blue! 💙",
    "tell me a joke": "Why was the Python code sad? Because it had too many bugs! 😂",
    "where are you from": "I exist in the digital cloud ☁️, ready to help wherever I'm needed.",
    "who created you": "I was created by a Developer Maheera Rehman learning Python concepts! 🧑‍💻",
    "i am bored": "I suggest trying the Hangman project we discussed earlier 🕹️, or asking me about a new topic!",
    "i need motivation": "The only way to do great work is to love what you do. Keep pushing! 💪",
    "give me a fact": "A single strand of spider silk is stronger than a steel wire of the same thickness. 🕷️"
}

def response_of_bot(user_question, rules):
    
    standardized_input = user_question.lower()
    
    # Keyword Check (Iterate through keys)
    for key, value in rules.items():
        if key in standardized_input:
            return value 

    # 2. Default Response if no rule is matched
    return "I'm still learning 🤖. Could you try rephrasing that?"


def chat_bot(rules):
    # 1. Initial Setup
    print('🤖 Welcome to the Basic Chatbot')
    print('You can ask me basic questions. Type "BYE" to exit.')

    # 2. Get User Name 
    user_name = input('Enter your name: ')
    print("-" * 30)

    
    while True:
        # Prompt uses the standardized user name
        user_input = input(f'\n{user_name}, how can I help you? ')
         
        if user_input.lower() == "bye":
            # Use the 'bye' response directly for a friendly exit
            print(f"Bot : {rules['bye']} ")
            break
    
        reply = response_of_bot(user_input, rules)
        print(f'Bot : {reply}')
        
    print("\nThanks for using the chat bot ✌️")

# Execute the main function, passing the rules dictionary
chat_bot(responses)