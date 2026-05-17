# -----------------------------------------
# Basic Chatbot Project
# CodeAlpha Python Internship
# -----------------------------------------

# Function to reply to user messages
def chatbot_reply(user_input):

    # Convert input to lowercase
    # so HELLO and hello are treated same
    user_input = user_input.lower()

    # Greeting response
    if user_input == "hello":
        return "Hi!"

    # Asking chatbot condition
    elif user_input == "how are you":
        return "I am fine, thanks!"

    # Asking chatbot name
    elif user_input == "what is your name":
        return "I am a Python Chatbot."

    # Goodbye response
    elif user_input == "bye":
        return "Goodbye!"

    # Default response for unknown input
    else:
        return "Sorry, I don't understand."


# Welcome message
print("===== BASIC CHATBOT =====")
print("Type 'bye' to exit the chatbot.")

# Infinite loop to keep chatbot running
while True:

    # Take user input
    user_message = input("You: ")

    # Get chatbot response
    response = chatbot_reply(user_message)

    # Print chatbot response
    print("Bot:", response)

    # Stop chatbot if user types bye
    if user_message.lower() == "bye":
        break


# Ending message
print("Chatbot closed.")