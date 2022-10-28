import os
from time import sleep

import telegram
import requests
from dotenv import load_dotenv


def send_message_bot(telegram_token, my_tgm_id, json_response):
    bot = telegram.Bot(token=telegram_token)
    lesson_title = json_response['new_attempts'][0]['lesson_title']
    lesson_url = json_response['new_attempts'][0]['lesson_url']
    if json_response['new_attempts'][0]['is_negative']:
        bot.send_message(
            text=f'''
У вас проверили работу "{lesson_title}"
{lesson_url}
 
К сожалению в работе нашлись ошибки
            ''',
            chat_id=my_tgm_id
        )
    else:
        bot.send_message(
            text=f'''
У вас проверили работу "{lesson_title}"'

Преподавателю всё понравилось, '
можно приступать к следующему уроку!
            ''',
            chat_id=my_tgm_id
        )


def main():
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    my_tgm_id = os.environ['MY_ID']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': devman_token
    }
    params = {}
    seconds = 20
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            review_answer = response.json()
            if review_answer['status'] == 'timeout':
                timestamp = review_answer['timestamp_to_request']
            else:
                timestamp = review_answer['last_attempt_timestamp']
                send_message_bot(telegram_token, my_tgm_id, review_answer)
            params = {
                'timestamp': str(timestamp)
            }
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            sleep(20)
            continue


if __name__ == '__main__':
    main()
