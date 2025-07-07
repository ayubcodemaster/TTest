from decimal import Decimal
from random import randint
from config import TOKEN

from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio
import requests
from yandex_geocoder import Client

from zayavka_database import save_db

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}
channel = "@zayavkalar_kanali"

print('Hello')
email = ""
password = ""

def get_eskiz_token(email, password):
    url = "https://notify.eskiz.uz/api/auth/login"
    payload = {
        'email': email,
        'password': password
    }
    headers = {}
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:  #OK
        # return response.json().get('data', {}).get('token', {})
        return response.json()['data']['token']
