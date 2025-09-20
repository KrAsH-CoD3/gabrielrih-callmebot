"""WhatsApp messaging module using CallMeBot API."""

import requests
import warnings
from typing import Tuple

# Create a session for connection reuse
_session = requests.Session()


def send_message(
    message: str, 
    phone_number: str, 
    api_key: str, 
    enable_fake_mode: bool = False
) -> Tuple[bool, str]:
    """
    Send a free WhatsApp message using CallMeBot API.
    
    Args:
        message: The message text to send
        phone_number: The recipient's phone number
        api_key: CallMeBot API key
        enable_fake_mode: If True, simulates sending without actual API call
        
    Returns:
        Tuple of (success_status, response_message)
    """
    if enable_fake_mode:
        return True, "Success (fake mode)"
    
    status_code, response = _call_api(api_key, phone_number, message)
    is_success = status_code == 200
    return is_success, response


def _call_api(api_key: str, phone_number: str, message: str) -> Tuple[int, str]:
    """
    Make API call to CallMeBot service.
    
    Args:
        api_key: CallMeBot API key
        phone_number: The recipient's phone number
        message: The message text to send
        
    Returns:
        Tuple of (status_code, response_text)
    """
    payload = {
        'phone': phone_number, 
        'text': message, 
        'apikey': api_key
    }
    url = "https://api.callmebot.com/whatsapp.php"
    
    try:
        response = _session.get(url, params=payload, timeout=30)
        return response.status_code, response.text
    except requests.RequestException as e:
        return 0, f"Request failed: {str(e)}"


def send_free_notification(
    message: str, 
    phone_number: str, 
    api_key: str, 
    enable_fake_mode: bool = False
) -> Tuple[bool, str]:
    """
    Send a free WhatsApp notification using CallMeBot API.
    
    .. deprecated:: 1.0.2
        Use :func:`send_message` instead. This function will be removed in a future version.
    
    Args:
        message: The message text to send
        phone_number: The recipient's phone number
        api_key: CallMeBot API key
        enable_fake_mode: If True, simulates sending without actual API call
        
    Returns:
        Tuple of (success_status, response_message)
    """
    warnings.warn(
        "send_free_notification is deprecated and will be removed in a future version. "
        "Use `send_message` instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return send_message(message, phone_number, api_key, enable_fake_mode)