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
        response = requests.get(url, headers=headers)
        print(response.json())

if __name__ == '__main__':
    main()