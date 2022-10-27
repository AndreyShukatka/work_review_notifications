import os
import logging

import requests
from dotenv import load_dotenv


def devman_request(url, devman_token):
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
            print(response.json())
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue


def main():
    load_dotenv()
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    devman_token = os.environ['DEVMAN_TOKEN']
    url = 'https://dvmn.org/api/long_polling/'
    devman_request(url, devman_token)


if __name__ == '__main__':
    main()
