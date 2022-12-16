from aiogram import types, Dispatcher
from config import bot, dp,DICES
import random




@dp.message_handler()
async def echo(message:types.Message):
    if message.chat.type != 'private':
        bad_words = ['лох','темик','монгол','иди','пошел','че','кто','али','я','адис','нах','энен','ска','сук'
                     ,'бл','катись','пи','ан','ваг','ху']
        username = f'@{message.from_user.username}' if message.from_user.username is not None else message.from_user.full_name
        for i in bad_words:
            if i in message.text.lower().replace(' ',''):
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f'не матерись {username}, сам ты {i}!')
    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'dice':
        dice1 = await bot.send_dice(message.chat.id, emoji= '🎰')







def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)