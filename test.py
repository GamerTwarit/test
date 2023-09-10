import random

# Define a dictionary of user inputs and their corresponding responses
responses = {
    "hello": "Hey there! How's your day going?",
    "how are you": "I'm good, thinking about you. \U0001F60A",
    "what's up": "Not much, just missing you. \U0001F495",
    "how was your day": "It was okay, but it's always better when I get to talk to you. \U0001F497",
    "tell me a joke": "Sure! Why did the scarecrow win an award? Because he was outstanding in his field! \U0001F604",
    "tell me more": "I'd love to share more with you. What's on your mind?",
    "bye": "Aww, already? Okay, have a great day! \U0001F618",
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    response = responses.get(user_input, "I'm not sure how to respond to that.")
    
    # Check for follow-up responses based on context
    if user_input == "tell me more" and "last_response" in context:
        response = "You always make me want to share more. What else would you like to know?"
    
    # Store the last response in context for follow-up
    context["last_response"] = response
    
    return response

# Define a dictionary to store context for follow-up responses
context = {}

# Main conversation loop
print("Girlfriend Bot: Hey! How's your day going? Type 'bye' when you need to go. \U0001F495")
while True:
    user_input = input("You: ").lower()
    response = get_response(user_input)
    
    if user_input == 'bye':
        print("Girlfriend Bot: Aww, already? Okay, have a great day! \U0001F618")
        break

    # Check for specific emotional states
    if any(word in user_input for word in ["good", "fine", "bad", "sad", "happy"]):
        if any(word in user_input for word in ["good", "fine"]):
            response = "That's wonderful! I'm here for you if you want to chat. \U0001F601"
        else:
            possible_responses = [
                "I'm here to make your day better! Tell me, what's on your mind?",
                "I'm sorry to hear that. Anything I can do to cheer you up?",
                "I wish I could give you a hug right now. What's bothering you?",
                "Remember, tough times don't last, tough people do! How can I help?",
                "Sometimes a good chat can turn things around. What's been bothering you?",
                "I'm here to lend an ear. What's on your mind?",
                "Let's chat it out. I'm here to listen and support you.",
                "I'm here to brighten your day! What's been bringing you down?",
            ]
            response = random.choice(possible_responses)

    # Check for specific emotional states and provide responses
    emotional_states = ["feeling down", "having a tough day", "feeling low", "having a bad time",
                        "not feeling well", "feeling sad", "feeling blue", "not in a good mood",
                        "feeling unhappy", "feeling upset", "feeling gloomy", "feeling insecure",
                        "insecurity", "feeling lonely", "loneliness", "feeling stuck", "in a rut"]
    
    for state in emotional_states:
        if state in user_input:
            possible_responses = [
                "I'm here to brighten your day! What's been bothering you? Let's talk it out.",
                "I'm here to lift your spirits! What's on your mind?",
                "I'm here to make you smile! What's been going on?",
                "I'm sorry to hear that. Let's chat and see if I can help improve your day.",
            ]
            response = random.choice(possible_responses)

    print("Girlfriend Bot:", response)
