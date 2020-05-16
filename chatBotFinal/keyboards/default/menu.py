from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сайт Кванториума!")
        ]
    ],
    resize_keyboard=True
)

direction_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IT-Квант"),
            KeyboardButton(text="Хайтек"),
            KeyboardButton(text="Аэроквантум")
        ],
        [
            KeyboardButton(text="Промышленный дизайн"),
            KeyboardButton(text="ПромРобоКвант"),
            KeyboardButton(text="Биоквантум")
        ],
        [
            KeyboardButton(text="Инженерная математика"),
            KeyboardButton(text="Медиа")
        ]
    ],
    resize_keyboard=True
)

direction_menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="•IT-Квантум"),
            KeyboardButton(text="•Хайтек"),
            KeyboardButton(text="•Аэроквантум")
        ],
        [
            KeyboardButton(text="•Промышленный дизайн"),
            KeyboardButton(text="•ПромРобоКвант"),
            KeyboardButton(text="•Биоквантум")
        ],
        [
            KeyboardButton(text="•Инженерная математика"),
            KeyboardButton(text="•Медиа")
        ],
        [
            KeyboardButton(text="•Назад")
        ]
    ],
    resize_keyboard=True
)


answerButtons = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="Да"),
                KeyboardButton(text="Нет")
            ]
    ],
    resize_keyboard=True
)

answerButtonsTesting = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="1 вариант"),
                KeyboardButton(text="2 вариант")
            ],
            [
                KeyboardButton(text="3 вариант")
            ]
    ],
    resize_keyboard=True
)

answerButtonsTestingForStasQuestHard = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="1 вариант"),
                KeyboardButton(text="2 вариант")
            ],
            [
                KeyboardButton(text="3 вариант"),
                KeyboardButton(text="4 вариант")
            ]
    ],
    resize_keyboard=True
)

answerButtonsTestingForStasQuest=ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="Да"),
          KeyboardButton(text="Нет")  
        ],
        [
            KeyboardButton(text="50/50")
        ]
    ],
    resize_keyboard=True
)

answerButtonsTestingForStasQuest2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да. Я их постоянно учу, очень полезно их запоминать."),
        ],
        [
            KeyboardButton(text="Нет. Если работает, зачем замарачиваться и думать о лишнем. Лучше подумать об решении проблем.")
        ],
        [
            KeyboardButton(text="Просто стараюсь их понять.")
        ]
    ],
    resize_keyboard=True
)

answerButtonsAfterTest = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="Да!!!!!!!!!!")
            ]
    ],
    resize_keyboard=True
)

answerButtonsSoHardQuest = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
        [
            KeyboardButton(text= "Не знаю кто это")
        ]
    ],
    resize_keyboard=True
)


answerButtonsPromDes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.Буду смотреть техническую начинку( емкость батареи, оперативку, функции и до.)")
        ],
        [
            KeyboardButton(text="2.В первую очередь обращу внимание на дизайн гаджета , экраны и интерфейс, цветовую гамму меню, удобство, эргономику")
        ]
    ],
    resize_keyboard=True
)

