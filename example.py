#
# Example of usage
#
# <gabrielrih>
#

from callMeBot.sendFreeMessage import sendFreeMessage

CONFIG_FULL_FILENAME = './config.yml'
isSuccess, response = sendFreeMessage("One line!\nAnother line.", CONFIG_FULL_FILENAME)
print(f"{isSuccess}")
print(f"{response}")