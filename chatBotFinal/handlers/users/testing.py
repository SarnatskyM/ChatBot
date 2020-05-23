#Наши команды и сам тест
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, direction_menu, direction_menu2, answerButtons, answerButtonsTesting, answerButtonsAfterTest, answerButtonsTestingForStasQuestHard,answerButtonsTestingForStasQuest, answerButtonsTestingForStasQuest2, answerButtonsSoHardQuest, answerButtonsPromDes, answerButtonsAiro1, answerButtonsAiro3, answerButtonsAiroJoJo, answerButtonsAiro5
from .info import *
from loader import dp
from states.test import Media,Itkvant,Hitech,Airo,Robo,Bio,Math,Des

answerUser =["Да","да","yes","Yes", "Да ", "да "]
answerUserNo =["Нет", "нет","не","НЕТ","Нет ","нет ","no ","NO","No"]
    
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я твоя помощница. Нужна помощь с определением направления?\nНапишите команду /help", reply_markup=menu)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_007.webp", "rb")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я - Чат бот для помощи в определении направления в кванториуме. Пройдите тест, отвечая Да или Нет, и я помогу вам определиться!\nДля начала или повторного прохождения напишите /test", reply_markup=ReplyKeyboardRemove())
    await message.answer("Мои команды /kvant, /directions, /test", reply_markup=menu)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_025.webp", "rb")

@dp.message_handler(commands=['kvant'])
async def process_kvant_command(message: types.Message):
    await message.answer(
    	text = '''
    	«Кванториум-15» — часть федеральной сети детских технопарков. Мы занимаемся дополнительным образованием в области инженерно-технических и естественных наук.

У нас школьники 5-11 классов учатся
• разрабатывать собственные проекты,
• пользоваться современным оборудованием,
• применять свои разработки на практике.

В «Кванториуме» работают молодые преподаватели, которые прошли обучение в Сколково и продолжают постоянно повышать свою квалификацию. Мы говорим с детьми на одном языке и просто объясняем сложное.
''', 
    	)


@dp.message_handler(commands=['directions'])
async def process_directions_commnad(message: types.Message):
	await message.reply(
			text = '''
			Выберите одно из направлений и я вам дам информацию о нем!
			''' , reply_markup=direction_menu2
		)

@dp.message_handler(Text(equals=["-IT-Квантум","-Хайтек","-Аэроквантум","-Промышленный дизайн","-ПромРобоКвант","-Биоквантум","-Инженерная математика","-Медиа","Назад"]))
async def get_infoD(message: Message):
    direct = {
     info_itkvant : "-IT-Квантум",
     info_hitech : "-Хайтек",
     info_airkvant : "-Аэроквантум",
     info_promdesign : "-Промышленный дизайн",
     info_promrobokvant : "-ПромРобоКвант",
     info_biokvant : "-Биоквантум",
     info_inmath : "-Инженерная математика",
     info_media : "-Медиа",
     info_back : "Назад",
    }
    for key , val in direct.items():
        if message.text == val:
            await message.answer(key)

@dp.message_handler(Text(equals=["Сайт Кванториума!"]))
async def get_web(message: Message):
    await message.answer("Всю дополнительную информацию о направления можно посмотреть на сайте https://kvantorium15.ru/")

@dp.message_handler(Command("test"))
async def choice_test(message: types.Message):
    #it-kvant
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_006.webp", "rb", reply_markup=direction_menu)
    await message.answer("Выберите направления по которому хотите пройти тест!")


@dp.message_handler(state =None)
async def enter_test(message: types.Message):
    if message.text == "Медиа":
        await message.answer("Отвечайте на вопросы Да или Нет")
        await message.answer("Вопрос №1.\n───────────────\n"
        "Интересно, как делают интервью на каналах ВДудь и Ещёнепознер?", reply_markup=answerButtons)
        await Media.Q1.set()
    if message.text == "IT-Квант":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Хочешь попробовать себя разработке игр, приложений и сайтов?",reply_markup=answerButtons)
        await Itkvant.I1.set()
    if message.text == "Хайтек":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Хотели бы научится работать с 3D принтером, станком лазерной резки?", reply_markup=answerButtons)
        await Hitech.H1.set()
    if message.text == "Аэроквантум":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Знаешь почему летает самолет?", reply_markup= answerButtonsAiro1)
        await Airo.A1.set()
    if message.text == "Промышленный дизайн":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Тебе нравится рисовать ?", reply_markup=answerButtons)
        await Des.D1.set()
    if message.text == "ПромРобоКвант":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Пробовал ли ты уже программировать?", reply_markup= answerButtons)
        await Robo.R1.set()
    if message.text == "Биоквантум":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Ты интересуешься биологией?", reply_markup = answerButtons)
        await Bio.B1.set()
    if message.text == "Инженерная математика":
        await message.answer("Вопрос №1. \n───────────────\n"
        "Хотелось бы вам перестать думать шаблонами и научится здравому анализу?", reply_markup=answerButtonsTestingForStasQuest)
        await Math.M1.set()

@dp.message_handler(state=Media.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Хочешь узнать, как создают крутые медиапроекты и успешные блоги?")
    await Media.next()


@dp.message_handler(state=Media.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Знаешь как отличить фейковую новость от настоящей?")
    await Media.next()

@dp.message_handler(state=Media.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Хочешь узнать, чем сценарий \"Фиксиков\" отличается от сценария \"Вечернего Урганта\"?")
    await Media.next()

@dp.message_handler(state=Media.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Тебе предложили снять видеообзор на любимую игру. Для тебя это\n\n\n1.Круто! Это может стать началом моего блога об играх.\n\n2.Будет сложновато придумать, о чём рассказывать, но интересно попробовать.\n\n3.Неинтересно. Лучше потрачу это время на то, чтобы научиться делать игры самому!", reply_markup=answerButtonsTesting)
    await Media.next()

@dp.message_handler(state=Media.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    if message.text == "2 вариант":
        await state.update_data(answer5=1)
    if message.text == "3 вариант":
        await state.update_data(answer5=0)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "У вас во дворе собака родила щенят. Нужно найти для них хозяев. Что ты для этого сделаешь?\n\n\n1.Заберут щенков или нет - неизвестно. Лучше пока сделаю для них хорошую будку со встроенным дозатором корма\n\n2.Напишу волонтёрам, которые работают с бездомными животными. Они-то наверняка знают, что делать с щенками!\n\n3.Сделаю такие фотографии этих пёселей, чтобы всем сразу хотелось их взять домой. Выложу фото в соцсетях и попрошу всех, кто может, сделать репосты.")
    await Media.next()

@dp.message_handler(state=Media.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=0)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    if message.text == "3 вариант":
        await state.update_data(answer6=2)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Друзья решили запустить паблик в Вконтакте и пригласили тебя присоединиться. Чем будешь помогать?\n\n\n1.Может быть буду репостить у себя их мемы и комментить интересные посты. Создам активность подписчиков.\n\n2.Кто-то сказал мемы? Я в этом шарю! Буду делать публикации, которые станут собирать тысячи лайков.\n\n3.Сделаю такие фотографии этих пёселей, чтобы всем сразу хотелось их взять домой. Выложу фото в соцсетях и попрошу всех, кто может, сделать репосты.")
    await Media.next()

@dp.message_handler(state=Media.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=1)
    if message.text == "2 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=0)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Классный руководитель предложил написать статью для школьного сайта. Нужно разобраться, как отличать фейковые новости от реальных. Возьмёшься?\n\n\n1.Конечно! Обожаю разоблачать обманщиков и проверять факты! Ещё и рейтинг СМИ составлю по частоте публикации фейков!\n\n2.А как их отличать-то? По-моему, никто наверняка не знает. Ладно, если пятёрку по русскому поставят, то попробую.\n\n3.Вы сайт этот видели? Он даже со смартфона не открывается нормально. Лучше предложу классной сделать новый современный сайт.")
    await Media.next()

@dp.message_handler(state=Media.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    if message.text == "2 вариант":
        await state.update_data(answer8=1)
    if message.text == "3 вариант":
        await state.update_data(answer8=0)
    await message.answer("Вопрос №9.\n─────────────────\n"
                         "Тебе предложили подработку на лето. Можно пойти на ТВ в отдел новостей, в лабораторию института биологии или в мастерскую 3D-печати и лазерной резки. Платить везде будут одинаково. Что выберешь?\n\n\n1.Конечно на ТВ! Посмотрю как делают настоящие новости и сам попробую себя в роли корреспондента\n\n2.Пробирки, реактивы, микроскопы, биоматериалы - кажется я делаю первый шаг к Нобелевке в области физиологии и медицины!\n\n3D-принтеры - это же самые современные технологии. Уже дома и органы для пересадки на них печатают. Однозначно туда!")
    await Media.next()

@dp.message_handler(state=Media.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer9=2)
    if message.text == "2 вариант":
        await state.update_data(answer9=0)
    if message.text == "3 вариант":
        await state.update_data(answer9=0)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?",reply_markup=answerButtonsAfterTest)
    await Media.next()

@dp.message_handler(state=Media.Q0)
async def answer_q0(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8,answerM9]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
        if item == 3:
            k += 3
    await message.answer("Вам подходит направление Медиа на - {0}% ".format(100*k//12), reply_markup=ReplyKeyboardRemove())
    await message.answer("Удачи вам!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_031.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()

@dp.message_handler(state=Math.M1)
async def answer_a1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=5)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Нравится ли вам решать не стандартные задачи?")
    await Math.next()


@dp.message_handler(state=Math.M2)
async def answer_m2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=5)
    if message.text == "50/50":
        await state.update_data(answer2 =5)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Нравятся ли долгие вычисления и находить решение примеров?")
    await Math.next()

@dp.message_handler(state=Math.M3)
async def answer_m3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUserNo:
        await state.update_data(answer3 =5)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Интересны ли вам доказтельства теорем?", reply_markup=answerButtonsTestingForStasQuest2)
    await Math.next()

@dp.message_handler(state=Math.M4)
async def answer_m4(message: types.Message, state: FSMContext):
    if message.text == "Просто стараюсь из понять.":
        await state.update_data(answer4=10)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Знаешь ли ты?\n\n1.Я на седьмом этаже. Это как шестой, но на один повыше. Иногда залезаю на крышу.\n\n2.В прямоугольном треугольнике квадрат длины гипотенузы, равен сумме квадратов длин катетов.\n\n3.Вдоль ночных дорог шла, босиком не жалея ног. Сердце его теперь в твоих руках. Не потеряй его и не сломай.\n\n4.В прямоугольном треугольнике квадрат катета, равен сумме квадратов длин гипотенуз.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M5)
async def answer_m5(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer5=5)
    if message.text == "3 вариант":
        await state.update_data(answer5=10)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Конкатенация - это болезнь?\n\n1.Да. Это болезнь поджелудочной железы.\n\n2.Да. Это особое восполение слизестой.\n\n3.Нет. Это склеивания объектов\n\n4.Нет. Это термин дифферициального исчесления")
    await Math.next()

@dp.message_handler(state=Math.M6)
async def answer_m6(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer6=5)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Теорема Пифагора это частный случай теоремы косинусов?\n\n1.Теорма Пифагора это частный случай теоремы о синусах.\n\n2.Да.\n\n3.Что такое косинус?\n\n4.Наоброт. Теорема косинусов это частный случай теоремы Пифагора.")
    await Math.next()

@dp.message_handler(state=Math.M7)
async def answer_m7(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer7=5)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Трисс или Йеннифэр?\n\n1.Трисс\n\n2.Йеннифэр\n\n3.Не выбираю вовсе\n\n4.Обе")
    await Math.next()

@dp.message_handler(state=Math.M8)
async def answer_m8(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer8=10)
    if message.text == "2 вариант":
        await state.update_data(answer8 = 5)
    await message.answer("Вопрос №8.\n───────────────\n"
                         "Сколько будет 0,(3) + 0,(3) + 0,(3)?\n\n1.Один\n\n2.0,(9).\n\n3.0,9999999998.\n\n4.Я что калькуляор?.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M9)
async def answer_m9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer9=10)
    if message.text == "2 вариант":
        await state.update_data(answer9=5)
    await message.answer("Вопрос №9.\n───────────────\n"
                         "За столом сидели мужики и...?\n\n1.Ели.\n\n2.Решали задачи.\n\n3.Учили теоремы.\n\n4.Занимались робототехникой.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M10)
async def answer_m10(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer10=10)
    if message.text == "2 вариант":
        await state.update_data(answer10=5)
    await message.answer("Вопрос №10.\n───────────────\n"
                         "Смотрите ли вы канал \"Хауди Хо\"?", reply_markup=answerButtonsSoHardQuest)
    await Math.next()

@dp.message_handler(state=Math.M11)
async def answer_m11(message: types.Message, state: FSMContext):
    if message.text == "Не знаю кто это":
        await state.update_data(answer11=5)
    if message.text == "Нет":
        await state.update_data(answer11=5)
    if message.text == "Да":
        await state.update_data(answer11= -20)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup=answerButtonsAfterTest)
    await Math.next()

@dp.message_handler(state=Math.M12)
async def answer_m12(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    answerM10 = data.get("answer10")
    answerM11 = data.get("answer11")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8, answerM9, answerM10,answerM11]
    for item in ans:
        if item == 5:
            k += 5
        if item == 10:
            k += 10
        if item == 0:
            k += 0
        if item == -20:
            k -= 20
    await message.answer("Вам подходит направление Инженерная математика на - {0}% ".format(100*k//80), reply_markup=ReplyKeyboardRemove())
    await message.answer("Это было тяжело, но ты справился!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_046.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()

@dp.message_handler(state=Des.D1)
async def answer_d1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Ты хотел(а) бы создать какое нибудь новое изобретение для пользы людей, животных , растений?")
    await Des.next()


@dp.message_handler(state=Des.D2)
async def answer_d2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Промышленный дизайн занимается разработкой изделий декоративно прикладного характера")
    await Des.next()

@dp.message_handler(state=Des.D3)
async def answer_d3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text == "Нет":
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Промышленный дизайн занимается разработкой предметов, устройств акцентируя внимание не только на эстетике , но и на функционале")
    await Des.next()

@dp.message_handler(state=Des.D4)
async def answer_d4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Вопрос №5.\n─────────────────\n"
                         "Приходят ли тебе в голову идеи по разработке каких либо новых устройств, которые делают жизнь людей лучше ?")
    await Des.next()

@dp.message_handler(state=Des.D5)
async def answer_d5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №6.\n───────────────\n"
                         "Тебе подарили гаджет нового поколения. Что ты сделаешь в первую очередь", reply_markup=answerButtonsPromDes)
    await Des.next()


@dp.message_handler(state=Des.D6)
async def answer_d6(message: types.Message, state: FSMContext):
    if message.text == "2.В первую очередь обращу внимание на дизайн гаджета , экраны и интерфейс, цветовую гамму меню, удобство, эргономику":
        await state.update_data(answer6=2)
    if message.text == "1.Буду смотреть техническую начинку( емкость батареи, оперативку, функции и до.)":
        await state.update_data(answer6=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup=answerButtonsAfterTest)
    await Des.next()

@dp.message_handler(state=Des.D7)
async def answer_d7(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5, answerM6]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление Промышленный дизайн на - {0}% ".format(100*k//6),reply_markup=ReplyKeyboardRemove())
    await message.answer("А вы быстро!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_034.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()

@dp.message_handler(state=Itkvant.I1)
async def answer_i1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Знаете, что такое C++ или Unity?")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I2)
async def answer_i2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Обладаете ли вы базовыми навыками программирования?")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I3)
async def answer_i3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Интересует разработка компьтерных игр?")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I4)
async def answer_i4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Что такое датчики и для чего они используются?\n\n1.Детекторы, которые имеют возможность измерять некоторые физические качества, такие как давление или свет.\n\n2.Моторы, которые имеют возможность приводить некоторые детали в движения, такие как колеса или свет.\n\n3.И то и то\n\n4.Я не знаю", reply_markup=answerButtonsTestingForStasQuestHard)
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I5)
async def answer_i5(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Знаете, что такое переменная, тип переменной и область видимости переменной?\n\n1.Да\n\n2.Ну почти\n\n3.Что то слышал\n\n4.Нет")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I6)
async def answer_i6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=2)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Какие личностые требования должны быть к ученику?\n\n1.Навыки командной работы\n\n2.постоять за себя\n\n3.Генерировать различные идеи\n\n4.Чувство юмора")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I7)
async def answer_i7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=2)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?",reply_markup=answerButtonsAfterTest)
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I8)
async def answer_i8(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление IT-Квантум на - {0}% ".format(100*k//10), reply_markup=ReplyKeyboardRemove())
    await message.answer("Многообещающе!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_016.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()

@dp.message_handler(state=Hitech.H1)
async def answer_h1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Не боитесь ли \"работать руками\" по дому?  Можете забить гвоздь в стену, починить радиоприёмник , и т. п")
    await Hitech.next()


@dp.message_handler(state=Hitech.H2)
async def answer_h2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Может вы уже увлекаетесь обработкой разнообразных материалов : дерева, металла и других?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H3)
async def answer_h3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Согласны ли беспрекословно соблюдать технику безопасности и ложить вещи на свои места ( если нет, вас могут отчислить из Квантума)?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H4)
async def answer_h4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Вопрос №5.\n─────────────────\n"
                         "Известна ли вам хотя бы одна технология 3D-печати?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H5)
async def answer_h5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("Вопрос №6.\n─────────────────\n"
                         "Создавали ли вы 3D-модель?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H6)
async def answer_h6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Знаете ли вы разницу между векторной и растровой графикой?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H7)
async def answer_h7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Имеется ли аллергия на пыль?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H8)
async def answer_h8(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer8=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("Вопрос №9.\n───────────────\n"
                         "Вы случайно раздавили шнур от зарядного устройства телефона ножкой стула. От этого телефон перестал заряжаться. Что вы будете с этим делать?\n\n1.Попытаюсь починить и заизолировать\n\n2.Выкину в мусорку и куплю новый шнур в магазине\n\n3.Стащу у брата или сестру тайком", reply_markup = answerButtonsTesting)
    await Hitech.next()

@dp.message_handler(state=Hitech.H9)
async def answer_h9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    if message.text == "2 вариант":
        await state.update_data(answer5=1)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №10.\n─────────────\n"
                         "Знаете ли вы другое применение лазера, кроме резки и гравировки?\n\n1.А еще можно светить в глаза летчикам самолетов\n\n2.Да. В рекламе видел, как лазером варили кофе и кузов машины\n\n3.У лазера множество применений")
    await Hitech.next()

@dp.message_handler(state=Hitech.H10)
async def answer_h10(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    if message.text == "3 вариант":
        await state.update_data(answer6=2)
    await message.answer("Вопрос №11.\n─────────────────\n"
                         "У вас в 3D-ручке застраял пластик. Что вы будете с этим делать?\n\n1.Заменю ручку по гарантии\n\n2.Вскрою ручку и попробую исправить данную проблему\n\n3.Выкину и заставлю родителей купить новую")
    await Hitech.next()

@dp.message_handler(state=Hitech.H11)
async def answer_h11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=1)
    if message.text == "2 вариант":
        await state.update_data(answer6=2)
    await message.answer("Вопрос №12.\n─────────────────\n"
                         "Представьте, что вы уже в Хайтеке и к вам обратился кванторианец с просьбой найти колесо нестандартного диаметра, которого нет в кванториуме. Как вы ему поможете?\n\n1.Создадите модель и распечатаете на 3D-принтере\n\n2.Попросите переделать конструкцию так, чтобы обойтись имеющимися деталями\n\n3.Обратитесь к администрации докупить колеса?")
    await Hitech.next()

@dp.message_handler(state=Hitech.H12)
async def answer_h12(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=2)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    await message.answer("Вопрос №13.\n─────────────────\n"
                         "Медиаквантум решил снять сюжет о Хайтеке. Будучи в группе Паши, что вы будете делать?\n\n1.Проведу экскурсию, расскажу об имеющемся оборудовании и продемонстрирую работу некоторых из них\n\n2.Не люблю светиться, боюсь камер, спрячусь в \"грязной зоне\" под большим фрезером\n\n3.Позову Пашу, наверняка он все лучше меня расскажет о направлении Хайтек")
    await Hitech.next()


@dp.message_handler(state=Hitech.H13)
async def answer_h13(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup = answerButtonsAfterTest)
    await Hitech.next()

@dp.message_handler(state=Hitech.H14)
async def answer_h14(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerH1 = data.get("answer1")
    answerH2 = data.get("answer2")
    answerH3 = data.get("answer3")
    answerH4= data.get("answer4")
    answerH5 = data.get("answer5")
    answerH6 = data.get("answer6")
    answerH7 = data.get("answer7")
    answerH8 = data.get("answer8")
    answerH9 = data.get("answer9")
    answerH10 = data.get("answer10")
    answerH11 = data.get("answer11")
    answerH12 = data.get("answer12")
    answerH13 = data.get("answer13")
    ans=[answerH1, answerH2, answerH3, answerH4,answerH5,answerH6,answerH7,answerH8,answerH9,answerH10,answerH11,answerH12,answerH13]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
        if item == 3:
            k += 3
    await message.answer("Вам подходит направление Хайтек на - {0}% ".format(100*k//18), reply_markup=ReplyKeyboardRemove())
    await message.answer("Вы уже закончили??")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_027.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()

@dp.message_handler(state=Robo.R1)
async def answer_r1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Интересно ли было разобрать робота и узнать что внутри?")
    await Robo.next()

@dp.message_handler(state=Robo.R2)
async def answer_r2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3. \n───────────────\n"
                         "Ты уже пробовал собирать робота?")
    await Robo.next()

@dp.message_handler(state=Robo.R3)
async def answer_r3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4. \n───────────────\n"
                         "Боишься востания роботов?")
    await Robo.next()

@dp.message_handler(state=Robo.R4)
async def answer_r4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Вопрос №5. \n───────────────\n"
                         "Хотел бы работать с Илоном Маском?")
    await Robo.next()


@dp.message_handler(state=Robo.R5)
async def answer_r5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("Вопрос №6.\n────────────────\n"
                         "Хотел бы сделать робота который выполняет скучную роботенку? ")
    await Robo.next()

@dp.message_handler(state=Robo.R6)
async def answer_r6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Слышали ли ты про искуственный интелект?")
    await Robo.next()

@dp.message_handler(state=Robo.R7)
async def answer_r7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("Вопрос №8.\n───────────────\n"
                         "Часто не бывает возможности во время кормить питомца. Что ты сделаешь?\n\n1.Сделаю автоматизированную кормушку и мой питомец всегда будет сыт во время\n\n2.Посмотрю в интернете как можно решить данную проблему, и последую совету\n\n3.Попрошу кого-нибудь, чтобы не забывали кормить", reply_markup = answerButtonsTesting)
    await Robo.next()

@dp.message_handler(state=Robo.R8)
async def answer_r8(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    if message.text == "2 вариант":
        await state.update_data(answer8=1)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №9.\n─────────────\n"
                         "Тебе предлжили учавствовать в гонке роботов\n\n1.Лучше я пойду нарисую робота\n\n2.Сложнова то наверное. Но я попробую\n\n3.СУПЕР! Сделаю своего робота и поучавствую в соревнованиях")
    await Robo.next()

@dp.message_handler(state=Robo.R9)
async def answer_r9(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer9=1)
    if message.text == "3 вариант":
        await state.update_data(answer9=2)
    await message.answer("Вопрос №10.\n─────────────────\n"
                         "Твои друзья собирают робота и предложили помочь. Что ты сделаешь?\n\n1.Буду собирать корпус и механизмы\n\n2.Буду программировать и паять\n\n3.Придумаю красивый дизайн")
    await Robo.next()

@dp.message_handler(state=Robo.R10)
async def answer_r10(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer10=1)
    if message.text == "2 вариант":
        await state.update_data(answer10=2)
    await message.answer("Вопрос №11.\n─────────────────\n"
                         "Ты сделал робота но он странно себя ведет и сходит с ума. Что ты сделаешь?\n\n1.Попробую найти ошибку в программе и проверю правильность подключения датчиков\n\n2.Выключу. Подожду. И снова включу.\n\n3.Пойду соберу другого робота")
    await Robo.next()

@dp.message_handler(state=Robo.R11)
async def answer_r11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer11=2)
    if message.text == "2 вариант":
        await state.update_data(answer11=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup = answerButtonsAfterTest)
    await Robo.next()

@dp.message_handler(state=Robo.R12)
async def answer_r12(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    answerM10 = data.get("answer10")
    answerM11 = data.get("answer11")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8,answerM9, answerM10,answerM11]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление ПромРобоКвантум на - {0}% ".format(100*k//15), reply_markup= ReplyKeyboardRemove())
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_047.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()
    

@dp.message_handler(state=Airo.A1)
async def answer_a0(message: types.Message, state: FSMContext):
    if message.text == "3.Из-за подъемной силы, на которую влияют тяга и форма крыла":
        await state.update_data(answer1=3)
    if message.text == "1.Из-за формы подъемной силы":
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Знаешь разницу между геликоптером(вертолетом), конвертопланом и квадрокоптером?", reply_markup = answerButtonsTestingForStasQuest)
    await Airo.next()


@dp.message_handler(state=Airo.A2)
async def answer_a2(message: types.Message, state: FSMContext):
    global answerUserNo
    if message.text in answerUserNo:
        await state.update_data(answer2=3)
    if message.text == "50/50":
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Ты хочешь найти себе крутую команду единомышленников и друзей?", reply_markup= answerButtonsAiro3)
    await Airo.next()

@dp.message_handler(state=Airo.A3)
async def answer_a3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=3)
    if message.text == "Я люблю работать один":
        await state.update_data(answer3= 1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Любишь ли ты возится с железками и проводами?", reply_markup = answerButtons)
    await Airo.next()

@dp.message_handler(state=Airo.A4)
async def answer_a4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=3)
    if message.text == "Я люблю работать один":
        await state.update_data(answer4= 1)
    await message.answer("Вопрос №5.\n─────────────────\n"
                         "Смотришь канал AlexGyver?", reply_markup = answerButtonsAiro5)
    await Airo.next()

@dp.message_handler(state=Airo.A5)
async def answer_a5(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await state.update_data(answer5=3)
    if message.text == "Да, я на него давно подписан!":
        await state.update_data(answer5= 3)
    await message.answer("Вопрос №6.\n─────────────────\n"
                         "Хочешь залететь туда, куда не заберется ни один робот?\n\n1.Да, куда-нибудь в горы или за густой лес\n\n2.Ну не знаю, а когда отпустят домой?\n\n3.Хочу дрон, который отнесет робота, куда я захочу", reply_markup = answerButtonsTesting)
    await Airo.next()

@dp.message_handler(state=Airo.A6)
async def answer_a6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=1)
    if message.text == "2 вариант":
        await state.update_data(answer6=3)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Что выберешь?\n\n1.Собрать крутой коптер, который решит чью-то проблему\n\n2.Я хочу просто полетать на дроне\n\n3.Я вообще не сам выбирал, меня родителм отдали")
    await Airo.next()

@dp.message_handler(state=Airo.A7)
async def answer_a7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=3)
    if message.text == "3 вариант":
        await state.update_data(answer7=1)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Приходилось ли тебе раньше паять?", reply_markup = answerButtons)
    await Airo.next()

@dp.message_handler(state=Airo.A8)
async def answer_a8(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer8=3)
    await message.answer("Вопрос №9.\n─────────────────\n"
                         "Пробовал ли ты уже программировать?")
    await Airo.next()

@dp.message_handler(state=Airo.A9)
async def answer_a9(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer9=3)
    await message.answer("Вопрос №10.\n─────────────────\n"
                         "Хочешь научиться программированию, и даже программировать дронов и роботов?")
    await Airo.next()

@dp.message_handler(state=Airo.A10)
async def answer_a10(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer10=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("Вопрос №11.\n───────────────\n"
                         "Какое слово подходит под определение? Угловые движения летательного аппарата относительно вертикальной оси , а также небольшие изменения курса вправо или влево.\n\n1.Рыскание\n\n2.Крен\n\n3.Щеночки!", reply_markup = answerButtonsTesting)
    await Airo.next()

@dp.message_handler(state=Airo.A11)
async def answer_a11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer11=5)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №12.\n─────────────\n"
                         "JoJo?", reply_markup = answerButtonsAiroJoJo)
    await Airo.next()

@dp.message_handler(state=Airo.A12)
async def answer_a12(message: types.Message, state: FSMContext):
    if message.text == "ORA ORA ORA!!!!":
        await state.update_data(answer12=3)
    if message.text == "Какёин":
        await state.update_data(answer12=3)
    if message.text == "Чиво?":
        await state.update_data(answer12=1)
    await message.answer("Вопрос №13.\n─────────────────\n"
                         "Ты закончил работу и пора идти домой, твои действия?\n\n1.Попрощаюсь и пойду помой. Дом, милый дом!\n\n2.Уберу все по местам и приведу рабочее пространство в порядок, попрощаюсь. Пойду домой!\n\n3.Пойду домой! Ура!", reply_markup= answerButtonsTesting)
    await Airo.next()

@dp.message_handler(state=Airo.A13)
async def answer_a13(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer13=3)
    await message.answer("Вопрос №14.\n─────────────────\n"
                         "Твой дрон странно себя ведет, после того как ты его собрал. Что будешь делать?\n\n1.Попробую найти ошибку в программе и проверю правильность подключения датчиков.\n\n2.Выключу. Подожду. И снова включу.\n\n3.Пойду домой, все равно не вышло")
    await Airo.next()

@dp.message_handler(state=Airo.A14)
async def answer_a14(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer14=3)
    await message.answer("Вопрос №15.\n─────────────────\n"
                         "Твои друзья собирают робота и предложили помочь. Что ты сделаешь?\n\n1.Буду программировать и паять\n\n2.Буду собирать корпус и механизмы\n\n3.Узнаю в какая помощь им требуется, а после начну заниматься ей.")
    await Airo.next()

@dp.message_handler(state=Airo.A15)
async def answer_a15(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer15=1)
    if message.text == "3 вариант":
        await state.update_data(answer15=3)
    if message.text == "1 вариант":
        await state.update_data(answer15=1)
    await message.answer("Вопрос №16.\n─────────────────\n"
                         "Тебе нужно, чтобы твой дрон завис на одной позиции, что ты сделаешь для этого?\n\n1.Привяжу его веревочкой, так он точно не сбежит\n\n2.Установлю и запрограммирую GPS датчики, чтобы по ним дрон определял свое положение и корректировал его.\n\n3.Поставлю на этой позиции метки, установлю на дрон камеру, по которой дрон будет считывать метки и корректировать свое положение относительно них.")
    await Airo.next()

@dp.message_handler(state=Airo.A16)
async def answer_a16(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer16=5)
    if message.text == "3 вариант":
        await state.update_data(answer16=3)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup = answerButtonsAfterTest)
    await Airo.next()

@dp.message_handler(state=Airo.A17)
async def answer_a17(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    answerM10 = data.get("answer10")
    answerM11 = data.get("answer11")
    answerM12 = data.get("answer12")
    answerM13 = data.get("answer13")
    answerM14 = data.get("answer14")
    answerM15 = data.get("answer15")
    answerM16 = data.get("answer16")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8,answerM9,answerM10, answerM11, answerM12, answerM13, answerM14,answerM15,answerM16]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
        if item == 3:
            k += 3
        if item == 5:
            k += 5
    await message.answer("Вам подходит направление АэроКвантум на - {0}% ".format(100*k//49), reply_markup=ReplyKeyboardRemove())
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_006.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()


@dp.message_handler(state=Bio.B1)
async def answer_b1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Хочешь узнать, есть ли жизнь в луже и какая она?")
    await Bio.next()


@dp.message_handler(state=Bio.B2)
async def answer_b2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Тебе интересно, как работает микроскоп?")
    await Bio.next()

@dp.message_handler(state=Bio.B3)
async def answer_b3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Тебе интересно, что обитает у тебя на руках?")
    await Bio.next()

@dp.message_handler(state=Bio.B4)
async def answer_b4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Ты хочешь узнать, как получается сметана?")
    await Bio.next()

@dp.message_handler(state=Bio.B5)
async def answer_b5(message: types.Message, state: FSMContext):
    if message.text in answerUser:
        await state.update_data(answer5=1)
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Тебе интересна генетика?")
    await Bio.next()

@dp.message_handler(state=Bio.B6)
async def answer_b6(message: types.Message, state: FSMContext):
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Тебе интересна микробиология?")
    await Bio.next()


@dp.message_handler(state=Bio.B7)
async def answer_b7(message: types.Message, state: FSMContext):
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup = answerButtonsAfterTest)
    await Bio.next()

@dp.message_handler(state=Bio.B8)
async def answer_b8(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7]
    for item in ans:
        if item == 1:
            k += 1
    await message.answer("Вам подходит направление БиоКвантум на - {0}% ".format(100*k//7), reply_markup= ReplyKeyboardRemove())
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_032.webp","rb")
    await message.answer("Для повторного прохождения напиште \"/test\" или \"/help\"")
    await state.finish()


