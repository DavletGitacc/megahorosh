from aiogram.utils import executor
import logging
from handlers import client,callback,extra,admin,fsm_admin
from config import dp
from database import db_bot

fsm_admin.register_handlers_fsm(dp)

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)

async def on_startup(_):
    db_bot.sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates = True,on_startup=on_startup)