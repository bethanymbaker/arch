from datetime import datetime
import os
import pytz
import requests
import math

_API_KEY = "1822e8e83c88668a8bc04f575acfa32b"
_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'


def query_api(city):
    try:
        print(_API_URL.format(city, _API_KEY))
        data = requests.get(_API_URL.format(city, _API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data


