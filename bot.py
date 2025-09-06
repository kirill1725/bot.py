from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    KeyboardButton, 
    Message, 
    ReplyKeyboardMarkup,
)
import dotenv
import os


dotenv.load_dotenv()

# Создаем объекты бота и диспетчера
token = os.getenv('BOT_TOKEN')
bot = Bot(token)
dp = Dispatcher()

button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение',
        peply_marcup=keyboard
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


def run():
    dp.run_polling(bot)


if __name__ == '__main__':
<<<<<<< HEAD
    run()
=======
    run()
>>>>>>> a58e689 (create a new project)
