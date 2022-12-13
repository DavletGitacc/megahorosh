from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from decouple import config
import logging
Token = config('Token')

bot = Bot(Token)
dp = Dispatcher(bot = bot)

@dp.message_handler(commands = ['start'])
async def comands(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'type /quiz to start quiz'
                                                              f' /meme to get photo'
                                                              f' /audio to get good song')

@dp.message_handler(commands = ['quiz'])
async def quiz_1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Next', callback_data='button1')
    markup.add(button1)
    question = 'Какое слово надо использовать после слова "Бургер'
    answers = [
        'Кинг',
        'Кортошка Фри',
        'Супер',
        'Пицца',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=0,
        open_period=15,
        reply_markup = markup
    )

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

@dp.message_handler(commands = ['meme'])
async def Burger_King(message: types.Message):
    photo = open('media/Бургеркинг_говно.jpg','rb')
    await bot.send_photo(message.from_user.id,photo = photo)

@dp.message_handler(commands = ['audio'])
async def Burger_King_audio1(message: types.Message):
    photo = open('media/murder brg.mp3','rb')
    markup1 = InlineKeyboardMarkup()
    buttonaud = InlineKeyboardButton('Next', callback_data='buttonaud')
    markup1.add(buttonaud)
    await bot.send_audio(message.from_user.id,audio = photo,reply_markup=markup1)

@dp.callback_query_handler(text = 'buttonaud')
async def Burger_Kind_audio2(call: types.CallbackQuery):
    audio = open('media/ng brg.mp3', 'rb')
    await bot.send_audio(call.from_user.id, audio=audio)

@dp.message_handler()
async def echo(message:types.Message):
    await bot.send_message(chat_id = message.from_user.id,text = int(message.text)**2)
    await bot.send_message(chat_id = message.from_user.id,text = message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates = True)