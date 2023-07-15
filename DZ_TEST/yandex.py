import requests
import os
from dotenv import load_dotenv, find_dotenv


class Yandex:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return {
            'Countent-Type': 'applecation/json',
            'Authorization': 'OAuth {}'.format(self.token),
        }

    def create_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        respons = requests.put(f'{folder_url}/?path={path}', headers=headers)
        return respons.status_code

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    ya = Yandex(os.getenv('Token_yandex'))
    folder = (ya.create_folder('яндекс папка'))
    print(folder)