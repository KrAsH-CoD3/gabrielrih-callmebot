#
# Example of usage
#
# <gabrielrih>
#

from callMeBot.sendFreeMessage import sendFreeMessage

isSuccess, response = sendFreeMessage("One line!\nAnother line.")
print(f"{isSuccess}")
print(f"{response}")