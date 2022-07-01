## SET UP THE ENVIRONMENT

- First of all you must allow your phone number to receive messages.
When you do it you'll receive a API Key for each phone number allowed.
Reference: https://www.callmebot.com/blog/free-api-whatsapp-messages/

- Then, you must inform the phone numbers and the api key in the configuration file.
This config file must be created using the name "config.yml" in the "callMeBot" folder.
The structure must be like this and you can set more than one phone number:

```yaml
- phone: +555598741585
  apikey: 152879
- phone: +555599958758
  apikey: 485178
```

- When you do it, you're ready to go!


## HOW TO USE IT?
In this repo we have the "example.py" filename. Using this file you can see the usage of it.