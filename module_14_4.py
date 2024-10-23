from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

choise_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="Calories")],
        [InlineKeyboardButton(text="Формулы расчёта", callback_data="Formulas")]
    ]
)

buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Продукт 1", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 2", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 3", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")
        ]
    ], resize_keyboard=True
)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

initiate_db()
check_and_populate_products()
products = get_all_products()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products:
        id_, title, description, price = product
        img_path = f'photo/{id_}.jpg'
        with open(f'{img_path}', 'rb') as img:
            await message.answer_photo(img, caption=f'Название: {title} | Описание: {description} | Цена: {price}p')
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=choise_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        'Расчет по формуле Миффлина-Сан Жеора для мужчин = 10 * Вес(в кг) + 6.25 * Рост(в см) - 5 * Возраст + 5,\n '
        'Расчет по формуле Миффлина-Сан Жеора для женщин = 10 * Вес(в кг) + 6.25 * Рост(в см) - 5 * Возраст - 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.username}, я бот помогающий твоему здоровью!', reply_markup=start_menu)


#
@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Можете рассчитать норму калорий, чтобы понять какой продукт вам подходит))')
    with open('../module_14/99px_ru_animacii_7234_chernij_kot_tochit_pilochkoj_svoi_kogti.gif', 'rb') as file:
        await message.answer_video(file, buy_menu, reply_markup=buy_menu)


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories', state=None)
async def sex_form(call):
    await call.message.answer('Введите свой пол: ')
    await UserState.sex.set()
    await call.answer()


@dp.callback_query_handler(state=UserState.sex)
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша дневная норма калорий: {calories} ккал")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)