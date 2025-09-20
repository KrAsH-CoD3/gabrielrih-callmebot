# Example of usage
import os
from dotenv import load_dotenv
from callmebot.whatsapp import send_message, send_free_notification

# Load environment variables
load_dotenv()

# Send the message
MESSAGE = "One line!\nAnother line\n*Bold text*\n_Italic text_."
API_KEY = os.getenv('CALLMEBOT_APIKEY')
PHONE_NUMBER = os.getenv('CALLMEBOT_PHONE_NUMBER')

if not API_KEY or not PHONE_NUMBER:
    raise Exception("You must set the CALLMEBOT_API_KEY and CALLMEBOT_PHONE_NUMBER as environment variables.")

# Deprecated `send_free_notification`
# isSuccess, response = send_free_notification(MESSAGE, PHONE_NUMBER, API_KEY, False)

# New `send_message`
isSuccess, response = send_message(MESSAGE, PHONE_NUMBER, API_KEY, False)

# Print response
print(f"{isSuccess}")
print(f"{response}")