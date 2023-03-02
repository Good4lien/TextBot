import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

API_TOKEN = '*'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#клавиатура с кнопками
keyboard = types.ReplyKeyboardMarkup()
button_1 = types.KeyboardButton(text="Улица")
keyboard.add(button_1)
button_2 = "Клуб"
keyboard.add(button_2)
button_3 = "Транспорт"
keyboard.add(button_3)
button_4 = "Кафе"
keyboard.add(button_4)
button_5 = "ТЦ"
keyboard.add(button_5)
button_6 = "Парк"
keyboard.add(button_6)
button_7 = "Пляж"
keyboard.add(button_7)
button_8 = "Директ"
keyboard.add(button_8)
button_9 = "Разное"
keyboard.add(button_9)

#Обработка входящих сообщений
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЭто пикап-бот от Романа!\n"
                         "Выбери место, а я тебе скину фразу для знакомства.\n😜", reply_markup=keyboard)

@dp.message_handler(Text(equals="Улица"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Улица'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Клуб"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Клуб'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Транспорт"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Транспорт'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Кафе"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Кафе'), reply_markup=keyboard)

@dp.message_handler(Text(equals="ТЦ"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('ТЦ'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Парк"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Парк'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Пляж"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Пляж'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Директ"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Директ'), reply_markup=keyboard)

@dp.message_handler(Text(equals="Разное"))
async def with_puree(message: types.Message):
    await message.answer(text.answer('Разное'), reply_markup=keyboard)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)