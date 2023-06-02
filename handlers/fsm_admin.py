from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN
from keyboard import client_kb
import uuid
from database.db_bot import sql_command_insert

class FSMadmin(StatesGroup):
    name = State()
    age = State()
    direct = State()
    group = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('ты не админ')
        else:
            global gen_id
            gen_id = uuid.uuid1()
            await message.answer(f'твой id {gen_id}')
            await FSMadmin.name.set()
            await message.answer('Твое имя?',reply_markup=client_kb.cancle_markup)
    else:
        await message.answer('пиши в личке!!!')

async def new_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = gen_id
        data['name'] = message.text
    await FSMadmin.next()
    await message.answer('сколько лет?')


async def new_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пиши только числа')
    elif int(message.text) < 9 or int(message.text) > 51:
        await message.answer('Возрастные ограничения')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMadmin.next()
        await message.answer('Напрaвление?', reply_markup=client_kb.markup2)


async def new_napr(message: types.Message, state: FSMContext):
    if message.text not in ['Backend', 'Frontend', 'UX-UI', 'Android', 'IOS']:
        await message.answer('Выбери из списка!!!')
    else:
        async with state.proxy() as data:
            data['direct'] = message.text
        await FSMadmin.next()
        await message.answer('Какая группа?', reply_markup=client_kb.cancle_markup)


async def new_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMadmin.next()
    await message.answer('PHOTO?')


async def new_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(data['photo'], caption=f"{data['id']}\n"
                                                          f"{data['name']}\n{data['age']}\n"
                                                          f"{data['direct']}\n{data['group']}\n"
                                   )
        await FSMadmin.next()
        await message.answer('Всё нормально?', reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Мы сохранили твою анкету',reply_markup= client_kb.markup1)
    elif message.text.lower == 'нет':
        await state.finish()
        await message.answer('да пошел ты',reply_markup= client_kb.markup1)
    else:
        await message.answer('не понятно')


async def cancle_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('да пошел ты',reply_markup=client_kb.markup1)


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancle_fsm, state='*', commands='cancle')
    dp.register_message_handler(cancle_fsm, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(new_name, state=FSMadmin.name)
    dp.register_message_handler(new_age, state=FSMadmin.age)
    dp.register_message_handler(new_napr, state=FSMadmin.direct)
    dp.register_message_handler(new_group, state=FSMadmin.group)
    dp.register_message_handler(new_photo, state=FSMadmin.photo,content_types=['photo'])
    dp.register_message_handler(submit, state=FSMadmin.submit)
