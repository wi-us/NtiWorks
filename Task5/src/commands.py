import datetime
import string as str1
import random
import json
from math import sqrt
from aiogram import types


items = ['start', 'about', 'help', 'joke', 'math']


def countSomeSymbols(string):
    _value = str(string)
    _letters = len(_value)
    _symbols = 0
    _spaces = 0

    #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    for _puncts in str1.punctuation:
        _symbols += _value.count(_puncts)

    _spaces += _value.count(' ')
    _spaces += _value.count('  ')

    return f"<tg-spoiler>Символов:\t{_letters}\nЗнаков препинания:\t{_symbols}\nПробелов:\t{_spaces}</tg-spoiler>"
        
def start(bot, message):

    _text = "Привет!"

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")

def help(bot, message):
    
    _start = "/start - Приветствие"
    _help = "/help - Вывод всего моего функционала"
    _about = "/about - Узнать немного о создателе"
    _joke = "/joke - Шутеечка"
    _math = "/math - Сгенерирую тебе квадратное уравнение с ответом"

    _text = f"{_start}\n"
    _text += f"{_help}\n"
    _text += f"{_about}\n"
    _text += f"{_joke}\n"
    _text += f"{_math}\n"
    
    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")

def about(bot, message):
    _firstName = "Даниил"
    _secondName = "Варавинов"
    _thirdName = "Владимирович"
    _sex = "Male"
    _dob = "15.10.2002"
    _age = int((datetime.datetime.today() - datetime.datetime(2002, 10, 15)).days/365)
    _role = "Student"
    _group = "ИСТ-223901"
    _course = 2
    _debts = 1

    _text = f"Фамилия:\t{_secondName}\n"
    _text += f"Имя:\t{_firstName}\n"
    _text += f"Отчество:\t{_thirdName}\n"
    _text += f"Пол:\t{_sex}\n"
    _text += f"Дата рождения:\t{_dob}\n"
    _text += f"Возраст:\t{_age}\n\n"
    _text += f"Он:\t{_role}\n"
    _text += f"Группы:\t{_group}\n"
    _text += f"Курса:\t{_course}\n"
    _text += f"C:\t{_debts}\t:долгами"

    _text += "\n\nКонтакты:\n"
    _text += "email: wius.dv@gmail.com\n"
    _text += "tg: @wi_us\n"
    _text += "vk: https://vk.com/wiuss"

    _text += "\n\n" + countSomeSymbols(_text)

    #Кнопка

    markup = types.InlineKeyboardMarkup()
    winter = types.InlineKeyboardButton('Зима', url='https://ru.wikipedia.org/wiki/Зима')
    markup.add(winter)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=markup)
    #keyboard1 = [
    #    [
    #        types.InlineKeyboardButton(text = "Option 1", callback_data='1'),
    #        types.InlineKeyboardButton(text = "Option 2", callback_data='2'),
    #    ],
    #    [types.InlineKeyboardButton(text = "Option 3", callback_data='3')],
    #]

    #reply_markup = types.InlineKeyboardMarkup(keyboard1)
    #types.update.message.reply_text('Please choose:', reply_markup=reply_markup)

def joke(jokes, bot, message):
    if len(jokes) == 0:
        with open("NtiWorks//Task5//serializeText//anekdots.json", "r", encoding="UTF-8") as file:
            jokes = json.loads(file.read())
    
    _text = jokes[random.randint(0, len(jokes))]

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")

    return jokes

def math(bot, message):
    _min = -100
    _max = +100

    a = float(random.randint(_min, +_max))
    b = float(random.randint(_min, +_max))
    c = float(random.randint(_min, +_max))

    discr = b**2 - 4*a*c
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)

    _primer = f"{a} * x1^2 + {b} * x2 + {c} = 0"
    _text = f"Пример:\t{_primer}\n"

    _text += f"Ответ:\t"
    if discr > 0:
        _text += f"x1 = {x1} \nx2 = {x2}"

    elif discr == 0:
        _text += f"x = {x1}"
    else:
        _text += "Корней нет"

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")

def default(bot, message):
    _text = "Не знаю такую команду"

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")
