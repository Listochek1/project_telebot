from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,Message,ContentType
from markups import *
from aiogram.dispatcher.filters import Text
import asyncio
from contextlib import suppress
from aiogram.utils.exceptions import MessageCantBeDeleted,MessageToDeleteNotFound
from aiogram.utils.markdown import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)


HELP_COMMAND = """
Помощь 🆘 - список команд</em>
/start - старт бота
Описание - описание бота
Курсы 🎓 - отправка нашего фото"""

async def on_startup(_):
    print('Я запустился!')



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text='Добро пожаловать!',
                           reply_markup=mainMenu)
    await message.delete()


@dp.message_handler(Text(equals="Помощь 🆘"))
async def command_help(message: types.Message):
    await message.answer(text=help_text,
                         reply_markup=back)
    await message.delete()



@dp.message_handler(Text(equals="📈 Подписка"))
async def command_menu(message: types.Message):
    await message.answer(text=sub_text,
                         reply_markup=back)
    await message.delete()
    

@dp.message_handler(Text(equals="Отзывы 🔔"))
async def command_menu(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('review1.jpg'))
    media.attach_photo(types.InputFile('review2.jpg'))
    media.attach_photo(types.InputFile('review3.jpg'))
    media.attach_photo(types.InputFile('review4.png'))
    media.attach_photo(types.InputFile('review5.png'))
    media.attach_photo(types.InputFile('review6.png'))
    await bot.send_media_group(message.chat.id, media=media)

    await message.delete()




@dp.message_handler(Text(equals="Курсы 🎓"))
async def command_menu(message: types.Message):
    await message.answer(curse_text,
                         reply_markup=back)
    await message.delete()



@dp.message_handler(Text(equals="◀️ Назад"))
async def command_menu(message: types.Message):
    await message.answer(text="Вы вернулись в главное меню",reply_markup=mainMenu)
    await message.delete()



# @dp.message_handler()
# async def send_cat(message: types.Message):
#     if message.text == '❤️':
#         await bot.send_sticker(chat_id=message.from_user.id,
#                                sticker="CAACAgQAAxkBAAEFO9hiyZapnjUwZ0cgIelk-Qe49P2R5gACWAADzjkIDRhMYBsy9QjTKQQ")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)