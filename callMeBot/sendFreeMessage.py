#
# Sending free messages by WhatsApp
#
# API references:
#   https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
#
# <gabrielrih>
#

import requests
import yaml

CONFIG_FULL_FILENAME = 'callMeBot/config.yml'
DEBUG_MODE = True # It simulates the send message function but in fact it doesn't send the message

def sendFreeMessage(message):
    configs, error  = _getConfigs()
    if error:
        return False, error

    for config in configs: # Send the message for each phone number configured
        http_code, response = _callAPI(config['apikey'], config['phone'], message)
        if http_code == 200:
            isSuccess = True
        else:
            isSuccess = False
            break
    return isSuccess, response # if error, returns the last error

def _getConfigs():
    try:
        with open(CONFIG_FULL_FILENAME) as f:
            configs = yaml.load(f, Loader=yaml.FullLoader)
        return configs, None
    except:
        error = "ERROR: Config file wasn't found! Check if the config file exists and if it has the right name."
        return None, error

def _callAPI(apiKey, phoneNumber, message):
    
    if DEBUG_MODE == False:
        payload = {'phone': phoneNumber, 'text': message, 'apikey': apiKey}
        response = requests.get('https://api.callmebot.com/whatsapp.php', params=payload)
        return response.status_code, response.text
    else:
        return 200, "Success!"