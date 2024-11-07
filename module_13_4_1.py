from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
ikb = InlineKeyboardMarkup()

with open(file='Besm1Firstbot.sig', mode='r', encoding='cp1251') as f:
    api = f.read()
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
