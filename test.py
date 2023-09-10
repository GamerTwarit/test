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

# Main conversation loop
print("Girlfriend Bot: Hey! How's your day going? Type 'bye' when you need to go. \U0001F495")
while True:
    user_input = input("You: ").lower()  # Convert user input to lowercase for case-insensitive matching
    
    if user_input == 'bye':
        print("Girlfriend Bot: Aww, already? Okay, have a great day! \U0001F618")
        break
    
    # Check if the user input is in the responses dictionary
    if user_input in responses:
        response = responses[user_input]
    else:
        response = "I'm not sure how to respond to that. \U0001F60C"  # Default response for unknown input
    
    print("Girlfriend Bot:", response)
    
    if user_input == "bad" or user_input == "very bad" or user_input == "extremely bad" or user_input == "worst":
        print("Girlfriend: I'm here to brighten your day! What's been bringing you down?")
    
    if user_input == "good" or user_input == "great" or user_input == "amazing" or user_input == "best":
        print("Girlfriend: oh cool, how are you ? ")
    
    if user_input == "mid" or user_input == "meh" or user_input == "fine" or user_input == "okay":
        print("Girlfriend: oh wanna do something naughty?")    

    if "how are you" in user_input:
        print("Girlfriend: how are you? i always feel good when i chat with you babe")
        if "good" in user_input or "fine" in user_input:
            response = "That's wonderful! I'm here for you if you want to chat. \U0001F601"
        elif "not good" in user_input or "not great" in user_input:
            # Additional possible responses for when the user is feeling down
            possible_responses = [
                "Girlfriend: I'm here to make your day better! Tell me, what's on your mind?",
                "Girlfriend: I'm sorry to hear that. Anything I can do to cheer you up?",
                "Girlfriend: I wish I could give you a hug right now. What's bothering you?",
                "Girlfriend: Remember, tough times don't last, tough people do! How can I help?",
                "Girlfriend: Sometimes a good chat can turn things around. What's been bothering you?",
                "Girlfriend: I'm here to lend an ear. What's on your mind?",
                "Girlfriend: Let's chat it out. I'm here to listen and support you.",
                "Girlfriend: I'm here to brighten your day! What's been bringing you down?",
            ]
            response = random.choice(possible_responses)
    
    elif "feeling down" in user_input or "having a tough day" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to brighten your day! What's been bothering you? Let's talk it out.",
            "Girlfriend: I'm here to lift your spirits! What's on your mind?",
            "Girlfriend: I'm here to make you smile! What's been going on?",
            "Girlfriend: I'm sorry to hear that. Let's chat and see if I can help improve your day.",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling low" in user_input or "having a bad time" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to lift your spirits! What's bothering you? I'm all ears.",
            "Girlfriend: I'm here to make your day better! What's been weighing on you?",
            "Girlfriend: I'm sorry to hear that. Let's talk it out. What's been going on?",
        ]
        response = random.choice(possible_responses)
    
    elif "not feeling well" in user_input or "feeling sad" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to cheer you up! What's been bothering you lately? Share with me.",
            "Girlfriend: I'm here to brighten your mood! What's on your mind?",
            "Girlfriend: I'm sorry to hear that. How can I help improve your mood?",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling blue" in user_input or "having a rough day" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to turn things around for you! What's going on that's got you down?",
            "Girlfriend: I'm here to provide some positivity! What's been bothering you today?",
            "Girlfriend: I'm here to make your day brighter! Let's talk and lift your spirits.",
        ]
        response = random.choice(possible_responses)
    
    elif "not in a good mood" in user_input or "feeling unhappy" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to bring some positivity into your day! What's troubling you right now?",
            "Girlfriend: I'm here to make you smile! Tell me, what's on your mind?",
            "Girlfriend: I'm here to listen and support you. What's been bothering you lately?",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling upset" in user_input or "feeling gloomy" in user_input:
        possible_responses = [
            "Girlfriend: I'm here to brighten your mood! What's bothering you? Let's chat.",
            "Girlfriend: I'm here to turn that frown upside down! What's going on?",
            "Girlfriend: I'm here to provide support and a listening ear. What's on your mind?",
        ]
        response = random.choice(possible_responses)
    
    # Add more emotional states and responses here
    elif "feeling insecure" in user_input or "insecurity" in user_input:
        possible_responses = [
            "Girlfriend: You're amazing just the way you are! What's been making you feel insecure?",
            "Girlfriend: You're special and unique! What's been bothering you?",
            "Girlfriend: Don't be too hard on yourself. What's been making you feel this way?",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling lonely" in user_input or "loneliness" in user_input:
        possible_responses = [
            "Girlfriend: You're not alone; I'm here for you! What's been making you feel lonely?",
            "Girlfriend: I'm here to keep you company. What's on your mind?",
            "Girlfriend: Feeling lonely is tough. Let's chat and make you feel better!",
        ]
        response = random.choice(possible_responses)
    
    elif "feeling stuck" in user_input or "in a rut" in user_input:
        possible_responses = [
            "Girlfriend: Let's work together to get you out of that rut! What's been holding you back?",
            "Girlfriend: Feeling stuck can happen to anyone. What's been bothering you?",
            "Girlfriend: I'm here to help you break free!"
        ]
        response = random.choice(possible_responses)
    
    print("Girlfriend:", response)
