#!/usr/local/bin/python3

import requests
import datetime
from config import config

def languages_request():
    base_url = 'https://wakatime.com/api/v1/'
    summary_url = 'users/current/summaries'
    api_key = config['api_key']
    today = datetime.date.today()
    week_ago = today + datetime.timedelta(days = - 7)
    end_day = str(today.year) + '-' +  str(today.month) + '-' +  str(today.day)
    start_day = str(week_ago.year) + '-' + str(week_ago.month) + '-' + str(week_ago.day)
    payload = {'api_key':api_key, 'start': start_day, 'end': end_day}
    r = requests.get(base_url + summary_url, params = payload)
    data = r.json()['data'][0]['languages']
    return data


if __name__ == '__main__':
    data = languages_request()
    print(data)
