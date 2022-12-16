from aiogram import Bot, Dispatcher
from decouple import config
import random

Token = config('Token')

bot = Bot(Token)
dp = Dispatcher(bot = bot)
ADMIN = [1154757842,]
DICES = ['🎲','🎯','🎳','🎰','⚽','🏀']
