from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = '7881922196:AAFY_Aij-5ug3ec7n-Xms_Nsitv0B68t9v0'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler(lambda message: message.text and 'hello' in message.text.lower()
                                    or 'привет' in message.text.lower())
async def greeting_messages(message):
    print(f'Сам {message["text"]}!')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
