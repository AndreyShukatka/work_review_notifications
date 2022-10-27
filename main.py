import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    headers = {
        'Authorization': devman_token
    }
    url = 'https://dvmn.org/api/long_polling/'
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=5)
            print(response.json())
        except requests.exceptions.ReadTimeout:
            continue
        except ConnectionError:
            continue

if __name__ == '__main__':
    main()