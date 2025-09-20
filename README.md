# CallMeBot

A Python package for sending free WhatsApp messages using the CallMeBot API.

## Setup

1. **Register your phone number** at [CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) to get your API key.

2. **Install the package:**
   
   Using pip:
   ```bash
   pip install git+https://github.com/gabrielrih/callmebot.git@1.0.2
   ```
   
   Using uv:
   ```bash
   uv add git+https://github.com/gabrielrih/callmebot.git@1.0.2
   ```

## Usage

```python
from callmebot import send_message

# Send a message
success, response = send_message(
    message="Hello from Python!",
    phone_number="+1234567890",
    api_key="your_api_key_here"
)

if success:
    print("Message sent successfully!")
else:
    print(f"Failed to send: {response}")
```

See `example.py` for a complete working example.