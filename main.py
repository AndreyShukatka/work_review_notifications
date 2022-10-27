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
    response = requests.get(url, headers=headers)
    print(response.text)

if __name__ == '__main__':
    main()