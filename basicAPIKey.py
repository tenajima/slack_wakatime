#!/usr/local/bin/python3

import requests
import datetime
from config import config
import base64

def languages_request():
    base_url = 'https://wakatime.com/api/v1/'
    stats_url = 'users/current/stats/last_7_days'
    api_key = config['api_key']
    auth = base64.b64encode(config['api_key'].encode('utf-8')).decode()
    header = {'Authorization': 'Basic {}'.format(auth)}
    r = requests.get(base_url + stats_url, headers = header)
    data = r.json()
    return data


if __name__ == '__main__':
    data = languages_request()
    print(data)
