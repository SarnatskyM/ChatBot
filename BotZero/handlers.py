from main import bot, dp
from aiogram import Bot, types
from aiogram.types import Message, CallbackQuery
from keyboards import ListOfButtons
from config import admin_id
from filters import *

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я твоя помощница. Нужна помощь с определением направления?\nНапишите команду /help")
    

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я - Чат бот для помощи в определении направления в кванториуме. Пройдите тест, отвечая Да или Нет, и я помогу вам определиться!\nДля начала или повторного прохождения напишите /test")
    await message.reply("Мои команды /help, /start, /kvant, /directions", reply = False)

@dp.message_handler(commands=['kvant'])
async def process_kvant_command(message: types.Message):
    await message.reply(
    	text = '''
    	!КВАНТОРИУМ_15 - это

	•бесплатное инженерно-техническое дополнительное образование для 5-11 классов

	•среда развития технических способностей и изобретальского мышления

	•молодые преподаватели, прошедшие обучение в Сколково

	•площадка с высокотехнологичным оборудованием
	проектное обучение

	•проблемно-ориентированный подход

	•внедрение разработок в действующий бизнес
''', reply = False
    	)

@dp.message_handler(commands=['directions'])
async def process_directions_commnad(message: types.Message):
	await message.reply(
			text = '''
			Всю дополнительную информацию о направления можно посмотреть на сайте https://kvantorium15.ru/
			''' 

		)

@dp.message_handler(commands=['test'])
async def process_test_command(message: types.Message):
    await message.reply("Давай попробуем подобрать тебе направление подготовки.\nПоехали?", reply = False)

