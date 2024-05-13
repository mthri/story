import logging

import requests

from django.conf import settings


def send_message_to_telegram_channel(message: str, channel_id: int) -> None:
    if not settings.SEND_NOTIFICATION:
        return None
        
    try:
        data = {
            'chat_id': channel_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(f'https://api.telegram.org/bot{settings.TLG_BOT}/sendMessage',
                                 data=data, timeout=10)
        response = response.json()
    except Exception as ex:
        logging.exception(ex)
