from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from keyboards import inline_menu, inline_about_menu, inline_finish_menu, inline_finish_back, inline_important_menu
from handlers.messages import greeting, entertainment, review, fund, food, address, grade, phone, plug


class FSMClient(StatesGroup):
    feedback = State()


# Общие функции и глобальные команды
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, greeting, reply_markup=inline_menu)


@dp.callback_query_handler(text='back_menu')
async def show_menu(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '📋 Главное меню:', reply_markup=inline_menu)
        await message.answer()
    except TypeError:
        pass


@dp.callback_query_handler(text='phone')
async def show_phone(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, phone, reply_markup=inline_finish_back)
    await callback.answer()


# Левая ветка
@dp.callback_query_handler(text='about')
async def about_list(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, '❓ Что из списка Вас интересует?', reply_markup=inline_about_menu)
    await callback.answer()


@dp.callback_query_handler(text='short')
async def show_review(callback: types.CallbackQuery):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('media/review/review1.jpg'))
    media.attach_photo(types.InputFile('media/review/review2.jpg'))
    media.attach_photo(types.InputFile('media/review/review3.jpg'))
    media.attach_photo(types.InputFile('media/review/review4.jpg'))

    await bot.send_media_group(callback.message.chat.id, media=media)
    await bot.send_message(callback.from_user.id, review, reply_markup=inline_finish_menu)
    await callback.answer()


@dp.callback_query_handler(text='entertainment')
async def show_entertainment(callback: types.CallbackQuery):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('media/entertainment/entertainment1.jpg'))
    media.attach_photo(types.InputFile('media/entertainment/entertainment2.jpg'))
    media.attach_photo(types.InputFile('media/entertainment/entertainment3.jpg'))
    media.attach_photo(types.InputFile('media/entertainment/entertainment4.jpg'))

    await bot.send_media_group(callback.message.chat.id, media=media)

    await bot.send_message(callback.from_user.id, entertainment, reply_markup=inline_finish_menu)
    await callback.answer()


@dp.callback_query_handler(text='fund')
async def show_fund(callback: types.CallbackQuery):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('media/fund/fund1.jpg'))
    media.attach_photo(types.InputFile('media/fund/fund2.jpg'))
    media.attach_photo(types.InputFile('media/fund/fund3.jpg'))
    media.attach_photo(types.InputFile('media/fund/fund4.jpg'))

    await bot.send_media_group(callback.message.chat.id, media=media)

    await bot.send_message(callback.from_user.id, fund, reply_markup=inline_finish_menu)
    await callback.answer()


@dp.callback_query_handler(text='food')
async def show_food(callback: types.CallbackQuery):
    photo = open('media/food/food.jpg', 'rb')

    await bot.send_photo(callback.message.chat.id, photo=photo)

    await bot.send_message(callback.from_user.id, food, reply_markup=inline_finish_menu)
    await callback.answer()


# Средняя ветка
@dp.callback_query_handler(text='date')
async def show_dates(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, plug, reply_markup=inline_finish_menu)
    await callback.answer()


# Правая ветка
@dp.callback_query_handler(text='important')
async def show_important(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Выберите из списка интересующую Вас тему:', reply_markup=inline_important_menu)
    await callback.answer()


# @dp.callback_query_handler(text='price')
# async def show_price(callback: types.CallbackQuery):
#     await bot.send_message(callback.from_user.id, 'Цена аренды базы на неделю...', reply_markup=inline_finish_menu)
#     await callback.answer()


@dp.callback_query_handler(text='address')
async def show_address(callback: types.CallbackQuery):
    photo = open('media/contacts/map.PNG', 'rb')

    await bot.send_photo(callback.message.chat.id, photo=photo)

    await bot.send_message(callback.from_user.id, address, reply_markup=inline_finish_menu)
    await callback.answer()


@dp.callback_query_handler(text='review', state=None)
async def show_feedback(callback: types.CallbackQuery):

    await bot.send_message(callback.from_user.id, grade)

    await FSMClient.feedback.set()


@dp.message_handler(state=FSMClient.feedback)
async def get_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        msg = message.text

    await bot.send_message(998820262, f'Пользователь с id {message.from_user.id} оставил отзыв: {msg}')
    await bot.send_message(message.from_user.id, '✅ Спасибо за Ваш отзыв!!!\n\nБудем рады увидеть Вас снова в Спартак Отеле😁', reply_markup=inline_finish_back)

    await state.finish()


def registration_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(show_menu, commands=['menu'])
