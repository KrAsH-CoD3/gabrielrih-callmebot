#
# Example of usage
#
# <gabrielrih>
#

from callMeBot.sendNotification.sendFreeMessage import sendFreeMessage

# Send the message
CONFIG_FULL_FILENAME = './config/config.yml'
MESSAGE_TO_BE_SENT = "One line!\nAnother line."
isSuccess, response = sendFreeMessage(MESSAGE_TO_BE_SENT, CONFIG_FULL_FILENAME)

# Print response
print(f"{isSuccess}")
print(f"{response}")