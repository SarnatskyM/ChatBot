#Машина состояний или же другими словами наша команда /test
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.helper import Helper, HelperMode, ListItem


class Media(Helper):
    mode = HelperMode.snake_case

    Q1 = ListItem()
    Q2 = ListItem()
    Q3 = ListItem()
    Q4 = ListItem()
    Q5 = ListItem()
    Q6 = ListItem()
    Q7 = ListItem()
    Q8 = ListItem()
    Q9 = ListItem()

class Itkvant(StatesGroup):
    I1 = State()
    I2 = State()
    I3 = State()
    I4 = State()
    I5 = State()
    I6 = State()
    I7 = State()
    I8 = State()

class Hitech(StatesGroup):
    H1 = State()
    H2 = State()
    H3 = State()
    H4 = State()
    H5 = State()
    H6 = State()
    H7 = State()
    H8 = State()
    H9 = State()
    H10 = State()
    H11 = State()
    H12 = State()
    H13 = State()
    H14 = State()

class Airo(StatesGroup):
    A1 = State()
    A2 = State()
    A3 = State()
    A4 = State()
    A5 = State()
    A6 = State()
    A7 = State()
    A8 = State()
    A9 = State()
    A10 = State()
    A11 = State()
    A12 = State()
    A13 = State()
    A14 = State()
    A15 = State()
    A16 = State()
    A17 = State()

class Des(StatesGroup):
    D1 = State()
    D2 = State()
    D3 = State()
    D4 = State()
    D5 = State()
    D6 = State()
    D7 = State()

class Robo(StatesGroup):
    R1 = State()
    R2 = State()
    R3 = State()
    R4 = State()
    R5 = State()
    R6 = State()
    R7 = State()
    R8 = State()
    R9 = State()
    R10 = State()
    R11 = State()
    R12 = State()

class Bio(StatesGroup):
    B1 = State()
    B2 = State()
    B3 = State()
    B4 = State()
    B5 = State()
    B6 = State()
    B7 = State()
    B8 = State()

class Math(StatesGroup):
    M1 = State()
    M2 = State()
    M3 = State()
    M4 = State()
    M5 = State()
    M6 = State()
    M7 = State()
    M8 = State()
    M9 = State()
    M10 = State()
    M11 = State()
    M12 = State()