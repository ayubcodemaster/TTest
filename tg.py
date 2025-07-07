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
