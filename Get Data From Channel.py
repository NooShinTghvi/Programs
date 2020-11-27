import configparser
import json
from datetime import datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)


# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


def createClient():
    # Reading Configs
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Setting configuration values
    api_id = int(config['Telegram']['api_id'])
    api_hash = str(config['Telegram']['api_hash'])
    phone = int(config['Telegram']['phone'])
    username = str(config['Telegram']['username'])
    user_input_channel = str(config['Telegram']['telegram_url'])

    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash)
    print(client)
    return client, phone, user_input_channel


async def main(phone: int, user_input_channel: str):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    my_channel = await client.get_entity(user_input_channel)

    """
    message starts from last until message which ID is ONE
    if U want get messages until specific message with id x,
    put x - 1 in "last_id_saved" variable.
    """
    last_id_saved = 0
    all_messages = []  # messages save

    is_total_count_limit = False  # if U want size of received messages be limited
    total_count_limit = 0  # size of limit received messages

    offset_id = 0
    limit = 10  # count of messages in every request
    while True:
        print("Current Offset ID is:", offset_id, "; Total Messages:", len(all_messages))
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            min_id=last_id_saved,
            max_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_id = messages[len(messages) - 1].id
        if is_total_count_limit and len(all_messages) >= total_count_limit:
            break

    with open('channel_messages.json', 'w') as outfile:
        json.dump(all_messages, outfile, cls=DateTimeEncoder)


if __name__ == '__main__':
    client, phone, user_input_channel = createClient()
    with client:
        client.loop.run_until_complete(main(phone, user_input_channel))
