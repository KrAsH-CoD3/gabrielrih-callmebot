#!/bin/bash
#
# Send free messages by Whats App
#
# Before start you must to set up:
#   https://www.callmebot.com/blog/free-api-whatsapp-messages/
#
# gabrielrih <gabrielrih@gmail.com>
#

# Parameters
PHONE_NUMBER="putYourPhoneNumberHere"
MESSAGE="putYourMessageHere"
API_KEY="putYourApiKeyHere"

# Send message
BASE_URL="https://api.callmebot.com/whatsapp.php"
curl -X POST -G \
    $BASE_URL \
    --data-raw "apikey=$API_KEY" \
    --data-urlencode "phone=$PHONE_NUMBER" \
    --data-urlencode "text=$MESSAGE"