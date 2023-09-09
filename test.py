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

# Define a dictionary to store context for follow-up responses
context = {}

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

# Main conversation loop
print("Girlfriend Bot: Hey! How's your day going? Type 'bye' when you need to go. \U0001F495")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Girlfriend Bot: Aww, already? Okay, have a great day! \U0001F618")
        break
    response = get_response(user_input)
    
    if "how are you" in user_input:
        if "good" in user_input or "fine" in user_input:
            response = "That's wonderful! I'm here for you if you want to chat. \U0001F601"
        elif "not good" in user_input or "not great" in user_input:
            # Additional possible responses for when the user is feeling down
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
    
    elif "feeling down" in user_input or "having a tough day" in user_input:
        possible_responses = [
            "I'm here to brighten your day! What's been bothering you? Let's talk it out.",
            "I'm here to lift your spirits! What's on your mind?",
            "I'm here to make you smile! What's been going on?",
            "I'm sorry to hear that. Let's chat and see if I can help improve your day.",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling low" in user_input or "having a bad time" in user_input:
        possible_responses = [
            "I'm here to lift your spirits! What's bothering you? I'm all ears.",
            "I'm here to make your day better! What's been weighing on you?",
            "I'm sorry to hear that. Let's talk it out. What's been going on?",
        ]
        response = random.choice(possible_responses)
    
    elif "not feeling well" in user_input or "feeling sad" in user_input:
        possible_responses = [
            "I'm here to cheer you up! What's been bothering you lately? Share with me.",
            "I'm here to brighten your mood! What's on your mind?",
            "I'm sorry to hear that. How can I help improve your mood?",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling blue" in user_input or "having a rough day" in user_input:
        possible_responses = [
            "I'm here to turn things around for you! What's going on that's got you down?",
            "I'm here to provide some positivity! What's been bothering you today?",
            "I'm here to make your day brighter! Let's talk and lift your spirits.",
        ]
        response = random.choice(possible_responses)
    
    elif "not in a good mood" in user_input or "feeling unhappy" in user_input:
        possible_responses = [
            "I'm here to bring some positivity into your day! What's troubling you right now?",
            "I'm here to make you smile! Tell me, what's on your mind?",
            "I'm here to listen and support you. What's been bothering you lately?",
        ]
       
    print(response)
