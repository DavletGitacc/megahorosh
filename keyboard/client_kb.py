from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

markup1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard = True,
    row_width=3
)
start_b = KeyboardButton('/strat',)
meme_b = KeyboardButton('/meme',)
quiz_b = KeyboardButton('/quiz',)
reg_b = KeyboardButton('/reg',)

markup1.add(start_b,meme_b,aud_b,quiz_b,reg_b)

back = KeyboardButton('Backend')
front = KeyboardButton('Frontend')
uxui = KeyboardButton('UX-UI')
android = KeyboardButton('Android')
ios = KeyboardButton('IOS')
markup2 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back,front,uxui,android,ios,KeyboardButton('cancle'))

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(KeyboardButton('да'),KeyboardButton('нет'))

cancle_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('/cancle'))