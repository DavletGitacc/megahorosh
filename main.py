from aiogram.utils import executor
import logging
from handlers import client,callback,extra,admin,fsm_admin
from config import dp


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_admin.register_handlers_fsm(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates = True)