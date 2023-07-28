from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Главное меню
inline_button_about = InlineKeyboardButton(text='Расскажи общую информацию о базе', callback_data='about')
inline_button_important = InlineKeyboardButton(text='Узнать важные сведения о базе', callback_data='important')
inline_button_date = InlineKeyboardButton(text='Узнать какие есть свободные даты', callback_data='date')
inline_button_review = InlineKeyboardButton(text='Оставить отзыв', callback_data='review')

inline_menu = InlineKeyboardMarkup(row_width=1)
inline_menu.add(inline_button_about).add(inline_button_date).add(inline_button_important).add(inline_button_review)

# Общая инфа о базе
inline_button_short = InlineKeyboardButton(text='Что такое Спартак Отель?', callback_data='short')
inline_button_entertainment = InlineKeyboardButton(text='Какие развлечения есть на базе?', callback_data='entertainment')
inline_button_fund = InlineKeyboardButton(text='Какой у нас номерной фонд?', callback_data='fund')
inline_button_food = InlineKeyboardButton(text='Расскажите о питании', callback_data='food')

inline_about_menu = InlineKeyboardMarkup(row_width=1)
inline_about_menu.add(inline_button_short).add(inline_button_entertainment).add(inline_button_fund).add(inline_button_food)

# Финиш ветки
inline_phone = InlineKeyboardButton(text='Узнать номер телефона для записи', callback_data='phone')
inline_back = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_menu')

inline_finish_menu = InlineKeyboardMarkup(row_width=1)
inline_finish_menu.add(inline_phone).add(inline_back)

inline_finish_back = InlineKeyboardMarkup(row_width=1)
inline_finish_back.add(inline_back)

# Важное меню
# inline_price = InlineKeyboardButton(text='Узнать цену', callback_data='price')
inline_address = InlineKeyboardButton(text='Узнать адрес', callback_data='address')

inline_important_menu = InlineKeyboardMarkup(row_width=1)
inline_important_menu.add(inline_address).add(inline_phone)
