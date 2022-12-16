from aiogram import types, Dispatcher
from config import bot
from config import ADMIN,DICES
import random

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if not message.from_user.id in ADMIN:
            await message.answer('ты не админ')
        elif not message.reply_to_message:
            await message.answer('комнда должна быть ответом')
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id,revoke_messages='тебя удолили из группы. лох')
            await message.answer(f'{message.from_user.full_name} удолил {message.reply_to_message.from_user.full_name}')

    else:
        await message.answer('пишт в группе')

async def pin(message: types.Message):
    if message.text == '.pin':
        if message.chat != 'private':
            if not message.reply_to_message:
                await message.answer('комнда должна быть ответом')
            else:
                await bot.pin_chat_message(message.chat.id, message.message_id)
        else:
            await message.answer('пиши в группе')

async def game(message: types.Message):
    if message.text.startswith('game'):
        if message.chat != 'private':
            if not message.from_user.id in ADMIN:
                await message.answer('ты не админ')
            else:
                await bot.send_dice(message.chat.id, emoji= random.choices(DICES))
        else:
            await message.answer('пиши в группе')
def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(ban, commands=['ban'])
    dp.register_message_handler(pin,text = '!pin')
    dp.register_message_handler(game, text = 'game')