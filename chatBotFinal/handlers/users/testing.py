#Наши команды и сам тест
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, direction_menu, direction_menu2, answerButtons, answerButtonsTesting, answerButtonsAfterTest, answerButtonsTestingForStasQuestHard,answerButtonsTestingForStasQuest, answerButtonsTestingForStasQuest2, answerButtonsSoHardQuest, answerButtonsPromDes, answerButtonsAiro1, answerButtonsAiro3, answerButtonsAiroJoJo, answerButtonsAiro5
from .questions import *
from loader import dp
from states.test import Media,Itkvant,Hitech,Airo,Robo,Bio,Math,Des

#handler commands
@dp.message_handler(commands=['start','help','kvant','directions','test'])
async def process_start_commands(message: types.Message):
    if message.text == "/start":
        await message.reply(hello_User, reply_markup=menu)
        await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_007.webp", "rb")
    elif message.text == "/help":
        await message.reply(helpForUser, reply_markup=ReplyKeyboardRemove())
        await message.answer("Мои команды /kvant, /directions, /test", reply_markup=menu)
        await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_025.webp", "rb")
    elif message.text == "/kvant":
        await message.answer(info_aboutKvant, parse_mode="HTML")
    elif message.text == "/directions":
        await message.reply(text = '''<b>Выберите одно из направлений и я вам дам информацию о нем!</b>''' , reply_markup=direction_menu2, parse_mode="HTML")
    else:
        await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_006.webp", "rb", reply_markup=direction_menu)
        await message.answer("Выберите направления по которому хотите пройти тест!")


#Клавиатура /directions и ссылка на сайт
@dp.message_handler(Text(equals=["-IT-Квантум","-Хайтек","-Аэроквантум","-Промышленный дизайн","-ПромРобоКвант","-Биоквантум","-Инженерная математика","-Медиа","Назад","Сайт Кванториума!"]))
async def get_infoDirOrWeb(message: Message):
    if message.text == "Сайт Кванториума!":
        await message.answer("Всю дополнительную информацию о направления можно посмотреть на сайте https://kvantorium15.ru/")
    else:
        direct = {info_itkvant : "-IT-Квантум",info_hitech : "-Хайтек",info_airkvant : "-Аэроквантум",info_promdesign : "-Промышленный дизайн",info_promrobokvant : "-ПромРобоКвант",info_biokvant : "-Биоквантум",info_inmath : "-Инженерная математика",info_media : "-Медиа",info_back : "Назад",}
        for key , val in direct.items():
            if message.text == val:
                await message.answer(key,parse_mode="HTML")

#Начало теста. Определение теста (есть картинка отражающая данную функцию)
@dp.message_handler(state =None)
async def enter_test(message: types.Message):
    if message.text == "Медиа":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>"+ M[0], reply_markup=answerButtons, parse_mode="HTML")
        await Media.first()   #установка первого стейта направления
    if message.text == "IT-Квант":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + I[0],reply_markup=answerButtons, parse_mode="HTML")
        await Itkvant.first()
    if message.text == "Хайтек":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + H[0], reply_markup=answerButtons, parse_mode="HTML")
        await Hitech.H1.set()
    if message.text == "Аэроквантум":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>"+ A[0], reply_markup= answerButtonsAiro1, parse_mode="HTML")
        await Airo.A1.set()
    if message.text == "Промышленный дизайн":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + D[0], reply_markup=answerButtons, parse_mode="HTML")
        await Des.D1.set()
    if message.text == "ПромРобоКвант":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + R[0], reply_markup= answerButtons, parse_mode="HTML")
        await Robo.R1.set()
    if message.text == "Биоквантум":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + B[0], reply_markup = answerButtons, parse_mode="HTML")
        await Bio.B1.set()
    if message.text == "Инженерная математика":
        await message.answer("<b>Вопрос №1.\n───────────────\n</b>" + IM[0], reply_markup=answerButtonsTestingForStasQuest, parse_mode="HTML")
        await Math.M1.set()

@dp.message_handler(state=Media.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + M[1], parse_mode="HTML")
    await Media.next()   


@dp.message_handler(state=Media.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + M[2], parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + M[3], parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("<b>Вопрос №5.\n───────────────\n</b>" + M[4], reply_markup=answerButtonsTesting, parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("<b>Вопрос №6.\n─────────────\n</b>"+ M[5], parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=0)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    if message.text == "3 вариант":
        await state.update_data(answer6=2)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + M[6], parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=1)
    if message.text == "2 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=0)
    await message.answer("<b>Вопрос №8.\n─────────────\n</b>" + M[7], parse_mode="HTML")
    await Media.next()

@dp.message_handler(state=Media.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    if message.text == "2 вариант":
        await state.update_data(answer8=1)
    if message.text == "3 вариант":
        await state.update_data(answer8=0)
    await message.answer("<b>Вопрос №9.\n─────────────\n</b>" + M[8], parse_mode="HTML")
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
    await message.answer(question_afterTest,reply_markup=answerButtonsAfterTest)
    await Media.next()

@dp.message_handler(state=Media.Q10)
async def answer_q0(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 1:
            k +=1
        elif item == 2:
            k += 2
        elif item == 3:
            k+= 3
    await message.answer("Вам подходит направление Медиа на - {0}% ".format(100*k//12), reply_markup=ReplyKeyboardRemove())
    await message.answer("Удачи вам!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_031.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()


@dp.message_handler(state=Math.M1)
async def answer_a1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=5)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>"+ IM[1], parse_mode="HTML")
    await Math.next()


@dp.message_handler(state=Math.M2)
async def answer_m2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=5)
    if message.text == "50/50":
        await state.update_data(answer2 =5)
    await message.answer("Вопрос №3.\n────────────────\n"  + IM[2], parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M3)
async def answer_m3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUserNo:
        await state.update_data(answer3 =5)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + IM[3], reply_markup=answerButtonsTestingForStasQuest2, parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M4)
async def answer_m4(message: types.Message, state: FSMContext):
    if message.text == "Просто стараюсь из понять.":
        await state.update_data(answer4=10)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("<b>Вопрос №5.\n───────────────\n</b>"+ IM[4], reply_markup=answerButtonsTestingForStasQuestHard, parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M5)
async def answer_m5(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer5=5)
    if message.text == "3 вариант":
        await state.update_data(answer5=10)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    await message.answer("<b>Вопрос №6.\n─────────────\n</b>" + IM[5], parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M6)
async def answer_m6(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer6=5)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>"+ IM[6], parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M7)
async def answer_m7(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer7=5)
    await message.answer("<b>Вопрос №8.\n─────────────\n</b>"+ IM[7], parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M8)
async def answer_m8(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer8=10)
    if message.text == "2 вариант":
        await state.update_data(answer8 = 5)
    await message.answer("<b>Вопрос №9.\n─────────────\n</b>"  + IM[8], reply_markup=answerButtonsTestingForStasQuestHard, parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M9)
async def answer_m9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer9=10)
    if message.text == "2 вариант":
        await state.update_data(answer9=5)
    await message.answer("<b>Вопрос №10.\n─────────────\n</b>" + IM[9], reply_markup=answerButtonsTestingForStasQuestHard, parse_mode="HTML")
    await Math.next()

@dp.message_handler(state=Math.M10)
async def answer_m10(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer10=10)
    if message.text == "2 вариант":
        await state.update_data(answer10=5)
    await message.answer("<b>Вопрос №11.\n─────────────\n</b>" + IM[10], reply_markup=answerButtonsSoHardQuest, parse_mode="HTML")
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
    await message.answer(question_afterTest, reply_markup=answerButtonsAfterTest)
    await Math.next()

@dp.message_handler(state=Math.M12)
async def answer_m12(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 5:
            k += 5
        if item == 10:
            k += 10
        if item == -20:
            k -= 20
    await message.answer("Вам подходит направление Инженерная математика на - {0}% ".format(100*k//80), reply_markup=ReplyKeyboardRemove())
    await message.answer("Это было тяжело, но ты справился!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_046.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()

@dp.message_handler(state=Des.D1)
async def answer_d1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + D[1], parse_mode="HTML")
    await Des.next()


@dp.message_handler(state=Des.D2)
async def answer_d2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + D[2], parse_mode="HTML")
    await Des.next()

@dp.message_handler(state=Des.D3)
async def answer_d3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text == "Нет":
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</>" + D[3], parse_mode="HTML")
    await Des.next()

@dp.message_handler(state=Des.D4)
async def answer_d4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("<b>Вопрос №5.\n─────────────────\n</b>" + D[4], parse_mode="HTML")
    await Des.next()

@dp.message_handler(state=Des.D5)
async def answer_d5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("<b>Вопрос №6.\n───────────────\n</b>" + D[5], reply_markup=answerButtonsPromDes, parse_mode="HTML")
    await Des.next()


@dp.message_handler(state=Des.D6)
async def answer_d6(message: types.Message, state: FSMContext):
    if message.text == "2.В первую очередь обращу внимание на дизайн гаджета , экраны и интерфейс, цветовую гамму меню, удобство, эргономику":
        await state.update_data(answer6=2)
    if message.text == "1.Буду смотреть техническую начинку( емкость батареи, оперативку, функции и до.)":
        await state.update_data(answer6=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest, reply_markup=answerButtonsAfterTest)
    await Des.next()

@dp.message_handler(state=Des.D7)
async def answer_d7(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление Промышленный дизайн на - {0}% ".format(100*k//6),reply_markup=ReplyKeyboardRemove())
    await message.answer("А вы быстро!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_034.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()

@dp.message_handler(state=Itkvant.I1)
async def answer_i1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + I[1], parse_mode="HTML")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I2)
async def answer_i2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + I[2], parse_mode="HTML")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I3)
async def answer_i3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + I[3], parse_mode="HTML")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I4)
async def answer_i4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("<b>Вопрос №5.\n───────────────\n</b>" + I[4], reply_markup=answerButtonsTestingForStasQuestHard, parse_mode="HTML")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I5)
async def answer_i5(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    await message.answer("<b>Вопрос №6.\n─────────────\n</b>" + I[5], parse_mode="HTML")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I6)
async def answer_i6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=2)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + I[6], parse_mode="HTML")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I7)
async def answer_i7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=2)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest,reply_markup=answerButtonsAfterTest)
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I8)
async def answer_i8(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление IT-Квантум на - {0}% ".format(100*k//10), reply_markup=ReplyKeyboardRemove())
    await message.answer("Многообещающе!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_016.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()

@dp.message_handler(state=Hitech.H1)
async def answer_h1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + H[1], parse_mode="HTML")
    await Hitech.next()


@dp.message_handler(state=Hitech.H2)
async def answer_h2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + H[2], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H3)
async def answer_h3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + H[3], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H4)
async def answer_h4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("<b>Вопрос №5.\n─────────────────\n</b>" + H[4], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H5)
async def answer_h5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("<b>Вопрос №6.\n─────────────────\n</b>" + H[5], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H6)
async def answer_h6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + H[6], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H7)
async def answer_h7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer("<b>Вопрос №8.\n─────────────\n</b>" + H[7], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H8)
async def answer_h8(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer8=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("<b>Вопрос №9.\n─────────────\n</b>" + H[8], reply_markup = answerButtonsTesting, parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H9)
async def answer_h9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    if message.text == "2 вариант":
        await state.update_data(answer5=1)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    await message.answer("<b>Вопрос №10.\n─────────────\n</b>" + H[9], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H10)
async def answer_h10(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    if message.text == "3 вариант":
        await state.update_data(answer6=2)
    await message.answer("<b>Вопрос №11.\n─────────────\n</b>" + H[10], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H11)
async def answer_h11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=1)
    if message.text == "2 вариант":
        await state.update_data(answer6=2)
    await message.answer("<b>Вопрос №12.\n─────────────\n</b>" + H[11], parse_mode="HTML")
    await Hitech.next()

@dp.message_handler(state=Hitech.H12)
async def answer_h12(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=2)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    await message.answer("<b>Вопрос №13.\n─────────────\n</b>" + H[12], parse_mode="HTML")
    await Hitech.next()


@dp.message_handler(state=Hitech.H13)
async def answer_h13(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest, reply_markup = answerButtonsAfterTest)
    await Hitech.next()

@dp.message_handler(state=Hitech.H14)
async def answer_h14(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
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
    await message.answer(infoAboutCommand)
    await state.finish()

@dp.message_handler(state=Robo.R1)
async def answer_r1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + R[1], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R2)
async def answer_r2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3. \n───────────────\n</b>" + R[2], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R3)
async def answer_r3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4. \n───────────────\n</b>" + R[3], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R4)
async def answer_r4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("<b>Вопрос №5. \n───────────────\n</b>" + R[4], parse_mode="HTML")
    await Robo.next()


@dp.message_handler(state=Robo.R5)
async def answer_r5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("<b>Вопрос №6. \n───────────────\n</b>" + R[5], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R6)
async def answer_r6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + R[6], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R7)
async def answer_r7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("<b>Вопрос №8.\n─────────────\n</b>" + R[7], reply_markup = answerButtonsTesting, parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R8)
async def answer_r8(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    if message.text == "2 вариант":
        await state.update_data(answer8=1)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    await message.answer("<b>Вопрос №9.\n─────────────\n</b>" + R[8], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R9)
async def answer_r9(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer9=1)
    if message.text == "3 вариант":
        await state.update_data(answer9=2)
    await message.answer("<b>Вопрос №10.\n─────────────\n</b>" + R[9], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R10)
async def answer_r10(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer10=1)
    if message.text == "2 вариант":
        await state.update_data(answer10=2)
    await message.answer("<b>Вопрос №11.\n─────────────\n</b>" + R[10], parse_mode="HTML")
    await Robo.next()

@dp.message_handler(state=Robo.R11)
async def answer_r11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer11=2)
    if message.text == "2 вариант":
        await state.update_data(answer11=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest, reply_markup = answerButtonsAfterTest)
    await Robo.next()

@dp.message_handler(state=Robo.R12)
async def answer_r12(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление ПромРобоКвантум на - {0}% ".format(100*k//15), reply_markup= ReplyKeyboardRemove())
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_047.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()
    

@dp.message_handler(state=Airo.A1)
async def answer_a0(message: types.Message, state: FSMContext):
    if message.text == "3.Из-за подъемной силы, на которую влияют тяга и форма крыла":
        await state.update_data(answer1=3)
    if message.text == "1.Из-за формы подъемной силы":
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + A[1], reply_markup = answerButtonsTestingForStasQuest, parse_mode="HTML")
    await Airo.next()


@dp.message_handler(state=Airo.A2)
async def answer_a2(message: types.Message, state: FSMContext):
    global answerUserNo
    if message.text in answerUserNo:
        await state.update_data(answer2=3)
    if message.text == "50/50":
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + A[2], reply_markup= answerButtonsAiro3, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A3)
async def answer_a3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=3)
    if message.text == "Я люблю работать один":
        await state.update_data(answer3= 1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + A[3], reply_markup = answerButtons, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A4)
async def answer_a4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=3)
    await message.answer("<b>Вопрос №5.\n─────────────────\n</b>" + A[4], reply_markup = answerButtonsAiro5, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A5)
async def answer_a5(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await state.update_data(answer5=3)
    if message.text == "Да, я на него давно подписан!":
        await state.update_data(answer5= 3)
    await message.answer("<b>Вопрос №6.\n─────────────────\n</b>" + A[5], reply_markup = answerButtonsTesting, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A6)
async def answer_a6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=1)
    if message.text == "2 вариант":
        await state.update_data(answer6=3)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + A[6], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A7)
async def answer_a7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=3)
    if message.text == "3 вариант":
        await state.update_data(answer7=1)
    await message.answer("<b>Вопрос №8.\n─────────────\n</b>" + A[7], reply_markup = answerButtons, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A8)
async def answer_a8(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer8=1)
    await message.answer("<b>Вопрос №9.\n─────────────\n</b>" + A[8], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A9)
async def answer_a9(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer9=3)
    await message.answer("<b>Вопрос №10.\n─────────────\n</b>" + A[9], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A10)
async def answer_a10(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer10=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Ответом будет являться вариант ответа!")
    await message.answer("<b>Вопрос №11.\n─────────────\n</b>" + A[10], reply_markup = answerButtonsTesting, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A11)
async def answer_a11(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer11=5)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    await message.answer("<b>Вопрос №12.\n─────────────\n</b>" + A[11], reply_markup = answerButtonsAiroJoJo, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A12)
async def answer_a12(message: types.Message, state: FSMContext):
    if message.text == "ORA ORA ORA!!!!":
        await state.update_data(answer12=3)
    if message.text == "Какёин":
        await state.update_data(answer12=3)
    if message.text == "Чиво?":
        await state.update_data(answer12=1)
    await message.answer("<b>Вопрос №13.\n─────────────\n</b>" + A[12], reply_markup= answerButtonsTesting, parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A13)
async def answer_a13(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer13=3)
    await message.answer("<b>Вопрос №14.\n─────────────────\n</b>" + A[13], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A14)
async def answer_a14(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer14=3)
    await message.answer("<b>Вопрос №15.\n─────────────────\n</b>" + A[14], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A15)
async def answer_a15(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer15=1)
    if message.text == "3 вариант":
        await state.update_data(answer15=3)
    if message.text == "1 вариант":
        await state.update_data(answer15=1)
    await message.answer("<b>Вопрос №16.\n─────────────────\n</b>" + A[15], parse_mode="HTML")
    await Airo.next()

@dp.message_handler(state=Airo.A16)
async def answer_a16(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer16=5)
    if message.text == "3 вариант":
        await state.update_data(answer16=3)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest, reply_markup = answerButtonsAfterTest)
    await Airo.next()

@dp.message_handler(state=Airo.A17)
async def answer_a17(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
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
    await message.answer(infoAboutCommand)
    await state.finish()


@dp.message_handler(state=Bio.B1)
async def answer_b1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("<b>Вопрос №2. \n───────────────\n</b>" + B[1], parse_mode="HTML")
    await Bio.next()


@dp.message_handler(state=Bio.B2)
async def answer_b2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("<b>Вопрос №3.\n────────────────\n</b>" + B[2], parse_mode="HTML")
    await Bio.next()

@dp.message_handler(state=Bio.B3)
async def answer_b3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("<b>Вопрос №4.\n─────────────────\n</b>" + B[3], parse_mode="HTML")
    await Bio.next()

@dp.message_handler(state=Bio.B4)
async def answer_b4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("<b>Вопрос №5.\n───────────────\n</b>" + B[4], parse_mode="HTML")
    await Bio.next()

@dp.message_handler(state=Bio.B5)
async def answer_b5(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer5=1)
    await message.answer("<b>Вопрос №6.\n─────────────\n</b>" + B[5], parse_mode="HTML")
    await Bio.next()

@dp.message_handler(state=Bio.B6)
async def answer_b6(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer6=1)
    await message.answer("<b>Вопрос №7.\n─────────────\n</b>" + B[6], parse_mode="HTML")
    await Bio.next()


@dp.message_handler(state=Bio.B7)
async def answer_b7(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer7=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer(question_afterTest, reply_markup = answerButtonsAfterTest)
    await Bio.next()

@dp.message_handler(state=Bio.B8)
async def answer_b8(message: types.Message, state: FSMContext):
    k = 0
    data = await state.get_data()
    ans = [data.get(f"answer{n}") for n in range(len(data))]
    for item in ans:
        if item == 1:
            k += 1
    await message.answer("Вам подходит направление <b>БиоКвантум</b> на - {0}% ".format(100*k//7), reply_markup= ReplyKeyboardRemove(), parse_mode="HTML")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_032.webp","rb")
    await message.answer(infoAboutCommand)
    await state.finish()


