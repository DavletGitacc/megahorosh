from aiogram import types, Dispatcher
from config import bot
from config import ADMIN

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('ты не админ')
        elif not message.reply_to_message:
            await message.answer('комнда должна быть ответом')
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id,revoke_messages='тебя удолили из группы. лох')
            await message.answer(f'{message.from_user.full_name} удолил {message.reply_to_message.from_user.full_name}')

    else:
        await message.answer('пишт в группе')

def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix = '!/')

