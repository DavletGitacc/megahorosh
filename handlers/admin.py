from aiogram import types, Dispatcher
from config import bot
from config import ADMIN,DICES
import random
from database.db_bot import sql_command_delete, sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def pin(message: types.Message):
        if message.chat != 'private':
            if not message.reply_to_message:
                await message.answer('комнда должна быть ответом')
            else:
                await bot.pin_chat_message(message.chat.id, message.message_id)
        else:
            await message.answer('пиши в группе')

async def game(message: types.Message):
        if message.chat != 'private':
            if not message.from_user.id in ADMIN:
                await message.answer('ты не админ')
            else:
                await bot.send_dice(message.chat.id, emoji= random.choices(DICES))
        else:
            await message.answer('пиши в группе')

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("ты не админ!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer_photo(
                user[6],
                caption=f"{user[2]} {user[3]} {user[4]} "
                        f"{user[5]}\n{user[1]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"delete {user[2]}",
                                         callback_data=f"delete {user[0]}")))
async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Вы удалили эту анкету", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)

def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(pin,commands= ['pin'])
    dp.register_message_handler(game,commands= ['game'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))