#Наши команды и сам тест
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test

promdesign =0
promkvantum=0
biokvantum=0
inmath=0
media=0
itkvant=0
hitech=0
airkvant=0
    
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я твоя помощница. Нужна помощь с определением направления?\nНапишите команду /help")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_007.webp", "rb")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я - Чат бот для помощи в определении направления в кванториуме. Пройдите тест, отвечая Да или Нет, и я помогу вам определиться!\nДля начала или повторного прохождения напишите /test")
    await message.reply("Мои команды /kvant, /directions, /test", reply = False)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_025.webp", "rb")

@dp.message_handler(commands=['kvant'])
async def process_kvant_command(message: types.Message):
    await message.reply(
    	text = '''
    	«Кванториум-15» — часть федеральной сети детских технопарков. Мы занимаемся дополнительным образованием в области инженерно-технических и естественных наук.

У нас школьники 5-11 классов учатся
• разрабатывать собственные проекты,
• пользоваться современным оборудованием,
• применять свои разработки на практике.

В «Кванториуме» работают молодые преподаватели, которые прошли обучение в Сколково и продолжают постоянно повышать свою квалификацию. Мы говорим с детьми на одном языке и просто объясняем сложное.
''', reply = False
    	)


@dp.message_handler(commands=['directions'])
async def process_directions_commnad(message: types.Message):
	await message.reply(
			text = '''
			Всю дополнительную информацию о направления можно посмотреть на сайте https://kvantorium15.ru/
			''' 
		)

@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    #it-kvant
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_006.webp", "rb")
    await message.answer("Отлично. Я задам тебе пару вопросов. Отвечай на них 'Да' или 'Нет'\n"
                         "Вопрос №1. \n────────────────\n"
                         "Хочешь создавать свои игры и сайты?? "
                         )
    await Test.Q1.set()



@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global itkvant
    if message.text == "Да":
        itkvant = 1
    #promdesign
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Хочешь реализовать проект всей своей жизни?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global promdesign
    if message.text == "Да":
        promdesign = 1
    #hitech
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Нравится высокотехнологичное оборудование и хочешь научиться с ним работать?")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global hitech
    if message.text == "Да":
        hitech = 1
    #promkvant
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Хочешь сконструировать и запрограммировать своего робота?")
    await Test.next()

@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global promkvantum
    if message.text == "Да":
        promkvantum = 1
    #biokvant
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Хочешь изучать микробиологии, генетику, клетки и ткани?")
    await Test.next()

@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    global biokvantum
    if message.text == "Да":
        biokvantum = 1
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Хочешь познать всю сущность математики?")
    await Test.next()

@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    global inmath
    if message.text == "Да":
        inmath = 1
    #media
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Увлекаешься обработкой фото и видеомонтажом?")
    await Test.next()

@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    global media
    if message.text == "Да":
        media = 1
    #airkvant
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Хочешь собрать и настроить свой летательный аппарат?")
    await Test.next()

@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    global airkvant
    if message.text == "Да":
        airkvant = 1
    await message.answer("Спасибо за ваши ответы!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?")
    await Test.next()

@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    global promdesign, promkvantum, itkvant, hitech, airkvant, biokvantum, media, inmath
    if promdesign == 1:
        await message.answer("Вам подходит направление - ПромДизайн")
    if promkvantum == 1:
        await message.answer("Вам подходит направление - ПромКвантум")
    if itkvant == 1:
        await message.answer("Вам отлично подходит - АйтиКвантум")
    if hitech == 1:
        await message.answer("Вас заинтересует направление - Хайтек")
    if airkvant == 1:
        await message.answer("Вам подходит направление - АэроКвантум")
    if biokvantum == 1:
        await message.answer("Вам подходит направление - БиоКвантум")
    if media == 1:
        await message.answer("Вам подходит направление - МедиаКвант")
    if inmath == 1:
        await message.answer("Вам будут рады на направлении - Инженерная математика")
    if inmath == 0 and promdesign == 0 and promkvantum == 0 and itkvant == 0 and hitech ==0 and airkvant ==0 and biokvantum == 0 and media == 0:
        await message.answer("Извините, но вам не подходит ни одно из направлений. Но вы можете попробовать любое, там везде рады новичкам!")
    await message.answer("Дальше выбор за вами!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_021.webp","rb")
    promdesign = 0
    promkvantum = 0
    biokvantum = 0
    inmath = 0
    media = 0
    itkvant = 0
    hitech = 0
    airkvant = 0
    await state.finish()