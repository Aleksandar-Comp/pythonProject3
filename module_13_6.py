from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
butt_1 = KeyboardButton(text='Рассчитать')
butt_2 = KeyboardButton(text='Информация')
kb.row(butt_1, butt_2)


logging.basicConfig(
    filename='tg-bot.log', filemode='w', encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    level=logging.INFO)


def decor_log(func, message, txt):
    async def log_writer(*args, **kwargs):
        logging.info(f'Получено сообщение от {message["from"]["first_name"]}: {message["text"]}')
        rez = await func(*args, **kwargs)
        logging.info(f'Отправлен ответ: {txt}')
        return rez

    return log_writer


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

class UserData():
    DATA = {}


@dp.message_handler(commands=['start'])
async def start(message):
    txt = ('Привет! Я бот помогающий твоему здоровью. Хотите узнать сколько калорий '
           'Вам нужно потреблять в день для здорового питания? Нажмите на кнопку "Рассчитать".')
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt, reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_gender(message):
    print(f'Сообщение от {message["from"]["first_name"]}')
    UserData.DATA[message["from"]["first_name"]] = {}
    txt = 'Введите свой пол (М/Ж):'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    txt = 'Введите свой возраст:'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    txt = 'Введите свой рост:'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    txt = 'Введите свой вес:'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    UserData.DATA[message["from"]["first_name"]] |= await state.get_data()
    print(UserData.DATA)

    data = UserData.DATA[message["from"]["first_name"]]
    try:
        if data['gender'].upper() == 'Ж':
            calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161
        elif data['gender'].upper() == 'М':
            calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
        else:
            raise ValueError
        imb = round(float(data['weight']) / (float(data['growth']) / 100) ** 2, 1)
    except ValueError or ZeroDivisionError:
        txt = 'Вы ввели ошибочные данные'
    else:
        txt = (f'Ваша норма калорий по формуле Миффлина-Сан Жеора: {calories} калорий\n\n'
               f'Индекс массы тела (ИМТ): {imb} кг/кв.м\n\n'
               f'В соответствии с рекомендациями ВОЗ разработана следующая интерпретация показателей ИМТ:\n\n'
               f'16 и менее - Выраженный дефицит массы тела\n\n'
               f'16-18,5 - Недостаточная (дефицит) масса тела\n\n'
               f'18,5—25 - Норма\n\n'
               f'25—30 - Избыточная масса тела (предожирение)\n\n'
               f'30—35 - Ожирение 1 степени\n\n'
               f'35—40 - Ожирение 2 степени\n\n'
               f'40 и более - Ожирение 3 степени')
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)
    await state.finish()


@dp.message_handler(text='Информация')
async def info(message):
    txt = 'Я - невероятно крутой бот, который знает секрет как похудеть!'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)

@dp.message_handler()
async def all_massages(message):
    txt = 'Введите команду /start, чтобы начать общение.'
    message.answer = decor_log(message.answer, message, txt)
    await message.answer(txt)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)