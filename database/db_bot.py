import random
import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных запущена")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id TEXT PRIMARY KEY, "
               "name TEXT, age INTEGER,direction TEXT,"
               "group TEXT, photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentor_table VALUES "
                       "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentor_table").fetchall()
    random_user = random.choice(result)
    await message.answer_photo(
        random_user[5],
        caption=f"{random_user[0]}\n{random_user[1]} {random_user[2]} "
                f"{random_user[3]} {random_user[3]}"
    )

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentor_table").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentor_table WHERE id = ?", tuple(user_id))
    db.commit()