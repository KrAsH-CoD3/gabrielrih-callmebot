# Example of usage
import os
from callmebot.messages import send_free_notification

# Send the message
MESSAGE = "One line!\nAnother line."
API_KEY = os.getenv('CALLMEBOT_API_KEY')
PHONE_NUMBER = os.getenv('CALLMEBOT_PHONE_NUMBER')
if not API_KEY or not PHONE_NUMBER:
    raise Exception("You must set the CALLMEBOT_API_KEY and CALLMEBOT_PHONE_NUMBER as environment variables.")
isSuccess, response = send_free_notification(MESSAGE, PHONE_NUMBER, API_KEY, False)

# Print response
print(f"{isSuccess}")
print(f"{response}")