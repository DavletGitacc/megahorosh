from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

markup1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard = True,
    row_width=3
)
start_b = KeyboardButton('/strat',)
meme_b = KeyboardButton('/meme',)
aud_b = KeyboardButton('/audio',)

share_location = KeyboardButton('Share location', request_location= True)
share_contact = KeyboardButton('Share Contact', request_contact=True)

markup1.add(start_b,meme_b,share_contact,share_location)