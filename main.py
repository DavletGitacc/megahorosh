import asyncio

from aiogram.utils import executor
import logging
from handlers import client,callback,extra,admin,fsm_admin,uvedomlenie
from config import dp
from parser import cinema
# from database import db_bot

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_admin.register_handlers_fsm(dp)

uvedomlenie.register_handlers_notification(dp)
extra.register_handlers_extra(dp)

async def on_startup(_):
    asyncio.create_task(uvedomlenie.scheduler())
#     db_bot.sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates = True, on_startup=on_startup)