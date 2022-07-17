# Example of usage
from callmebot.messages import sendFreeMessage

# Send the message
MESSAGE_TO_BE_SENT = "One line!\nAnother line."
API_KEY = "595804"
PHONE_NUMBER = "+555599620760"
isSuccess, response = sendFreeMessage(MESSAGE_TO_BE_SENT, API_KEY, PHONE_NUMBER)

# Print response
print(f"{isSuccess}")
print(f"{response}")