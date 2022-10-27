import os
import logging

import telegram
import requests
from dotenv import load_dotenv


def connect_bot(telegram_token):
    bot = telegram.Bot(token=telegram_token)
    update = bot.get_updates()
    bot.send_message(text='Hi', chat_id=update[0]['message']['chat']['id'])
    print(update[0])


def request_devman(url, devman_token):
    headers = {
        'Authorization': devman_token
    }
    params = {}
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            json_response = response.json()
            if json_response['status'] == 'timeout':
                timestamp = json_response['timestamp_to_request']
            else:
                timestamp = json_response['last_attempt_timestamp']
            params = {
                'timestamp': str(timestamp)
            }
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue


def main():
    load_dotenv()
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    devman_token = os.environ['DEVMAN_TOKEN']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    url = 'https://dvmn.org/api/long_polling/'
    # request_devman(url, devman_token)
    connect_bot(telegram_token)


if __name__ == '__main__':
    main()
