#
# Sending free messages by WhatsApp
#
# API references:
#   https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
#
# <gabrielrih>
#

import requests

DEBUG_MODE = False # It simulates the send message function but in fact it doesn't send the message

def sendFreeMessage(message, apiKey, phoneNumber):
    http_code, response = _callAPI(apiKey, phoneNumber, message)
    isSuccess = False
    if http_code == 200:
        isSuccess = True
    return isSuccess, response # if error, returns the last error

def _callAPI(apiKey, phoneNumber, message):
    
    if DEBUG_MODE == False:
        payload = {'phone': phoneNumber, 'text': message, 'apikey': apiKey}
        response = requests.get('https://api.callmebot.com/whatsapp.php', params=payload)
        return response.status_code, response.text
    else:
        return 200, "Success!"