from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


api = "8172838769:AAEB3sFRHDh-mpNM7Uc23WmlfM-lTu_dg7k"
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start_messange(message):
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text="Хэй!")
async def all_massages(message):
    print("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)