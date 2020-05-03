#Наши команды и сам тест
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test

answerUser =["Да","да","yes","Yes", "Да ", "да "]
    
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
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1="Да")
    #promdesign
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Хочешь реализовать проект всей своей жизни?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2="Да")
    #hitech
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Нравится высокотехнологичное оборудование и хочешь научиться с ним работать?")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3="Да")
    #promkvant
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Хочешь сконструировать и запрограммировать своего робота?")
    await Test.next()

@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4="Да")
    #biokvant
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Хочешь изучать микробиологии, генетику, клетки и ткани?")
    await Test.next()

@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5="Да")
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Хочешь познать всю сущность математики?")
    await Test.next()

@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6="Да")
    #media
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Увлекаешься обработкой фото и видеомонтажом?")
    await Test.next()

@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7="Да")
    #airkvant
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Хочешь собрать и настроить свой летательный аппарат?")
    await Test.next()

@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer8="Да")
    await message.answer("Спасибо за ваши ответы!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?")
    await Test.next()

@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    data = await state.get_data()
    itkvant = data.get("answer1")
    promdesign = data.get("answer2")
    hitech = data.get("answer3")
    promkvantum = data.get("answer4")
    biokvantum = data.get("answer5")
    inmath = data.get("answer6")
    media = data.get("answer7")
    airkvant = data.get("answer8")
    d = {
     "Вам подходит направление - ПромДизайн" : promdesign,
     "Вам подходит направление - ПромРобоКвантум" : promkvantum,
     "Вам отлично подходит - АйтиКвантум" : itkvant,
     "Вас заинтересует направление - Хайтек" : hitech,
     "Вам подходит направление - АэроКвантум" : airkvant,
     "Вам подходит направление - БиоКвантум" : biokvantum,
     "Вам подходит направление - МедиаКвант" : media,
     "Вам будут рады на направлении - Инженерная математика" : inmath
    }
    for key , val in d.items():
        if val == "Да":
            await message.answer(key)
    await message.answer("Дальше выбор за вами!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_021.webp","rb")
    await state.finish()

@dp.message_handler()
async def some_message(message: types.Message):
    await message.answer("Извините, я не понимаю вас. Напише /help и я помогу вам!")

