# Sending free messages by WhatsApp
import requests

def send_free_notification(message, phoneNumber, apiKey, enableFakeMode = False):
    if enableFakeMode == False:
        http_code, response = _callAPI(apiKey, phoneNumber, message)
        if http_code == 200:
            isSuccess = True
        else:
            isSuccess = False
        return isSuccess, response
    else: # It simulates success without actually send the notification
        return True, "Success"

def _callAPI(apiKey, phoneNumber, message):
    payload = {'phone': phoneNumber, 'text': message, 'apikey': apiKey}
    url = "https://api.callmebot.com/whatsapp.php"
    response = requests.get(url, params=payload)
    return response.status_code, response.text