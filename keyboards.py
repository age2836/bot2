from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button1 = InlineKeyboardButton("🙎‍♀ Девушка", url="https://m-loves.ru")
button2 = InlineKeyboardButton("🙎‍♂ Парень", callback_data='boy')
otvet = InlineKeyboardMarkup(row_width=2).add(button1, button2)

button1 = InlineKeyboardButton("18-30", callback_data='kto')
button2 = InlineKeyboardButton("31-42", callback_data='kto')
button3 = InlineKeyboardButton("43 и старше", callback_data='kto')
otvet1 = InlineKeyboardMarkup(row_width=3).add(button1, button2, button3)

button1 = InlineKeyboardButton("🙎‍♂ Мужчин", url="https://m-loves.ru")
button2 = InlineKeyboardButton("🙎‍♀ Девушек", callback_data='1')
otvet2 = InlineKeyboardMarkup(row_width=2).add(button1, button2)

#button1 = InlineKeyboardButton("Написать", urls[nomer])
#button2 = InlineKeyboardButton("➡", callback_data='down')
#otvet3 = InlineKeyboardMarkup(row_width=2).add(button1, button2)

#button1 = InlineKeyboardButton("⬅", callback_data='up')
#button2 = InlineKeyboardButton("Написать", url="https://m-loves.ru")
#button3 = InlineKeyboardButton("➡", callback_data='down')
#otvet4 = InlineKeyboardMarkup(row_width=3).add(button1, button2, button3)

button1 = InlineKeyboardButton("⬅", callback_data='up')
button2 = InlineKeyboardButton("Написать", url="https://m-loves.ru")
otvet5 = InlineKeyboardMarkup(row_width=2).add(button1, button2)
