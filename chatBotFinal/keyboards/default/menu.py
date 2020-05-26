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
            KeyboardButton(text="-IT-Квантум"),
            KeyboardButton(text="-Хайтек"),
            KeyboardButton(text="-Аэроквантум")
        ],
        [
            KeyboardButton(text="-Промышленный дизайн"),
            KeyboardButton(text="-ПромРобоКвант"),
            KeyboardButton(text="-Биоквантум")
        ],
        [
            KeyboardButton(text="-Инженерная математика"),
            KeyboardButton(text="-Медиа")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)


answerButtons = ReplyKeyboardMarkup(    #key = 0
    keyboard=[
            [
                KeyboardButton(text="Да"),
                KeyboardButton(text="Нет")
            ]
    ],
    resize_keyboard=True
)

answerButtonsTesting = ReplyKeyboardMarkup(   # key = 1
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

answerButtonsTestingForStasQuestHard = ReplyKeyboardMarkup(    # key = 2
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

answerButtonsTestingForStasQuest=ReplyKeyboardMarkup(    # key = 3
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

answerButtonsTestingForStasQuest2 = ReplyKeyboardMarkup(   # key = 4
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

answerButtonsSoHardQuest = ReplyKeyboardMarkup(  # key = 5
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


answerButtonsPromDes = ReplyKeyboardMarkup(    # key = 6
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

answerButtonsAiro1 = ReplyKeyboardMarkup(   #key = 8
    keyboard=[
        [
            KeyboardButton(text="Из-за формы подъемной силы")
        ],
        [
            KeyboardButton(text="Понятия не имею")
        ],
        [
            KeyboardButton(text = "Из-за подъемной силы, на которую влияют тяга и форма крыла")
        ]
    ],
    resize_keyboard=True
)

answerButtonsAiro3 = ReplyKeyboardMarkup(    #key = 9
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
        [
            KeyboardButton(text = "Я люблю работать один")
        ]
    ],
    resize_keyboard=True
)

answerButtonsAiroJoJo = ReplyKeyboardMarkup(   #key = 10
    keyboard=[
        [
            KeyboardButton(text="ORA ORA ORA!!!!"),
            KeyboardButton(text="Какёин")
        ],
        [
            KeyboardButton(text = "Чиво?")
        ]
    ],
    resize_keyboard=True
)

answerButtonsAiro5 = ReplyKeyboardMarkup(  #key = 11
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
        [
            KeyboardButton(text = "Да, я на него давно подписан!")
        ]
    ],
    resize_keyboard=True
)
