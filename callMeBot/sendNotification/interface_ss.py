#
# Interface for calling it from Shell Script
#
# Usage in Shell Script:
#       response=$(python3 interface_ss.py /etc/callMeBot/config.yml "This is the message") 
#
# <gabrielrih>
#
from sendFreeMessage import sendFreeMessage
import sys

# Recieve parameters
CONFIG_FULL_FILENAME = sys.argv[1]
MESSAGE_TO_BE_SENT = sys.argv[2]

def main():
    isSuccess, message = sendFreeMessage(MESSAGE_TO_BE_SENT, CONFIG_FULL_FILENAME)
    response = str(isSuccess) + '|' + message
    print(response) # this print in recover in Shell Script

if __name__ == "__main__":
    main()