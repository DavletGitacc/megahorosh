from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, dp

@dp.callback_query_handler(text = 'button1')
async def quiz_2(call: types.CallbackQuery):
    question = 'Что такое Бургер Кинг?'
    answers = [
        'Вкусно и точка',
        'Сеть фаст фуда',
        'гоДно',
        'гоВно'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=3,
        open_period=15,
    )
@dp.callback_query_handler(text = 'buttonaud')
async def Burger_Kind_audio2(call: types.CallbackQuery):
    audio = open('media/ng brg.mp3', 'rb')
    await bot.send_audio(call.from_user.id, audio=audio)

def register_handlers_callback(dp : Dispatcher):
    dp.register_callback_query_handler(quiz_2, text = 'button1')
    dp.register_callback_query_handler(Burger_Kind_audio2,text = 'buttonaud')