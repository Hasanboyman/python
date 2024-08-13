from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Replace these with your own values
api_id = '25221873'  # Replace with your actual API ID
api_hash = '6b9b455b58e19a006eb8ed906c84b370'  # Replace with your actual API hash
phone_number = '+33 7 57 05 53 11'  # Your phone number

with TelegramClient(StringSession(), api_id, api_hash) as client:
    client.start(phone=phone_number)
    session_string = client.session.save()
    print(f'Session string: {session_string}')
