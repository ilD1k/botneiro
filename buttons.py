from telebot import types

#Меню емае
markup_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu_btn1 = types.KeyboardButton("Запустить GPT🔥")
menu_btn2 = types.KeyboardButton("👤Профиль")
markup_menu.add(menu_btn1, menu_btn2)

#Кнопки нейросетки
markup_promt = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Задать вопрос❓")
btn2 = types.KeyboardButton("Продолжить✏️")
btn3 = types.KeyboardButton("Вернуться в меню🏠")
markup_promt.add(btn1, btn2)
markup_promt.add(btn3)


# думаю тут пояснять не надо... ну ладно удаление кнопок
markup = types.ReplyKeyboardRemove()