from aiogram import executor, types
from module_13_4_1 import UserState, dp

@dp.message_handler(text='Калории')
async def set_age(message:types.message):
    await message.answer(f'Введи свой возраст')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введи свой рост (см)')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введи свой вес (кг)')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await message.answer(f'Ты мужчина или женщина?')
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    await message.answer(f'Твоя норма калорий =  {await mifflin_san_geor(**data)}.\n\n'
                         f'До свиданья!\nТы, ежели чего, заходи!')
    await state.finish()

async def mifflin_san_geor(age, growth, weight, gender):
    '''
    Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5. 1
    Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
    :param age: - возраст, лет
    :param growth: - рост, см
    :param weight: - вес, кг
    :param gender: - м(ужчина) или ж(енщина)
    :return: - суточная норма калорий, кал
    '''
    try:
        res = (10 * float(weight) * 10 +  6.25 * float(growth)
                +  5 * float(age)
                + (5.1 if gender[0].lower() == 'м' else (-161 if gender[0].lower() == 'ж' else None)))
    except Exception as e:
        res = f'...Упссс! Неправильные данные привели к ошибке: "{e}". Не могу рассчитать...'
    finally:
        return res

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот, который заботится о твоём здоровье.\n"
                         "Пока что я умею только считать суточную норму калорий.\n"
                         "Если хочешь, чтобы я посчитал, введи слово 'Калории'.")

@dp.message_handler(lambda message: message.text and any([gs_ in message.text.lower() for gs_ in
                                                          ['привет', "здорово", "здравствуй", "салют",
                                                           'hi', 'hello', 'how are you', 'how do you do']]))
async def greeting_messages(message):
    await message.answer(f"Привет, если не шутишь!")

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введи команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
