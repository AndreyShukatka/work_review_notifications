import os
from time import sleep
import textwrap
import logging

import telegram
import requests
from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):

    def __init__(self, telegram_token, tgm_id):
        super().__init__()
        tg_bot = telegram.Bot(token=telegram_token)
        self.chat_id = tgm_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def send_message_bot(telegram_token, tgm_id, review_answer):
    bot = telegram.Bot(token=telegram_token)
    lesson_title = review_answer['new_attempts'][0]['lesson_title']
    lesson_url = review_answer['new_attempts'][0]['lesson_url']
    if review_answer['new_attempts'][0]['is_negative']:
        bot.send_message(
            text=textwrap.dedent(
                f'''
                У вас проверили работу "{lesson_title}"
                {lesson_url}
 
                К сожалению в работе нашлись ошибки
                '''
            ),
            chat_id=tgm_id
        )
    else:
        bot.send_message(
            text=textwrap.dedent(
                f'''У вас проверили работу "{lesson_title}"'

                Преподавателю всё понравилось,
                можно приступать к следующему уроку!'''
            ),
            chat_id=tgm_id
        )


def main():
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    tgm_id = os.environ['TGM_ID']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': devman_token
    }
    params = {}
    seconds = 20
    logger = logging.getLogger('tg_Logger')
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(telegram_token, tgm_id))
    logger.info('Бот запущен!')
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            review_answer = response.json()
            if review_answer['status'] == 'timeout':
                timestamp = review_answer['timestamp_to_request']
            else:
                timestamp = review_answer['last_attempt_timestamp']
                send_message_bot(telegram_token, tgm_id, review_answer)
            params = {
                'timestamp': str(timestamp)
            }

        except requests.exceptions.ReadTimeout:
            logger.exception('Время ожидания ответа превышено!')
            continue
        except requests.exceptions.ConnectionError:
            logger.exception('Нет соединения с сервером!')
            sleep(seconds)
            continue
        except Exception:
            logger.warning("Бот упал с ошибкой:")
            logger.exception('')
            continue


if __name__ == '__main__':
    main()
