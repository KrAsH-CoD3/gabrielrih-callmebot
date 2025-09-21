# Example of usage
import os
from dotenv import load_dotenv
from callmebot import send_message, send_free_notification

# Load environment variables
load_dotenv()

# Send the message
# Single-line message
# MESSAGE = "One line!\nAnother line\n*Bold text*\n_Italic text_."

# Multi-line message
MESSAGE = """One line!
Another line
*Bold text*
_Italic text_."""
API_KEY = os.getenv('CALLMEBOT_APIKEY')
PHONE_NUMBER = os.getenv('CALLMEBOT_PHONE_NUMBER')

if not API_KEY or not PHONE_NUMBER:
    raise Exception("You must set the CALLMEBOT_API_KEY and CALLMEBOT_PHONE_NUMBER as environment variables.")

# DEPRECATED: `send_free_notification`
# is_success, response = send_free_notification(MESSAGE, PHONE_NUMBER, API_KEY, False)

# NEW: `send_message`
is_success, response = send_message(MESSAGE, PHONE_NUMBER, API_KEY)

# Print response
print(f"{is_success}")
print(f"{response}")