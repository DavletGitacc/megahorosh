from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

Token = config('Token')

bot = Bot(Token)
dp = Dispatcher(bot = bot,storage=storage)
ADMIN = [1407934008]
DICES = ['🎲','🎯','🎳','🎰','⚽','🏀']
