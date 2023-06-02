from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from parser1.parser import parser
from config import bot, dp
from database import db_bot
from keyboard.client_kb import markup1

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text ='привет',
                           reply_markup = markup1)
async def quiz_1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Next', callback_data='button1')
    markup.add(button1)
    question = 'Какое сейчас время'
    answers = [
        '22.00',
        '23.00',
        '2.00',
        'не простое',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=3,
        open_period=10,
        reply_markup = markup
    )
async def photo(message: types.Message):
    photo = open('media/meme.jpg','rb')
    await bot.send_photo(message.from_user.id,photo = photo)


async def get_wheels(message: types.Message):
    wheels = parser()
    for i in wheels:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n\n"
            f"{i['price']}\n\n"
            f"{i['size']}\n\n"
        )

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(start,commands=['start'])
    dp.register_message_handler(quiz_1,commands=['quiz'])
    dp.register_message_handler(photo,commands=['meme'])
    dp.register_message_handler(get_wheels, commands=['parser'])
