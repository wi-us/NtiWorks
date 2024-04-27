import datetime
import string as str1
import random
import json
from math import sqrt
from telebot import types
import keyboards as kbrds

items = ['start', 'about', 'help', 'joke', 'math', 'menu']



def countSomeSymbols(string):
    _value = str(string)
    _letters = len(_value)
    _symbols = 0
    _spaces = 0

    #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    for _puncts in str1.punctuation:
        _symbols += _value.count(_puncts)

    _spaces += _value.count("\n")
    _spaces += _value.count(' ')
    _spaces += _value.count('  ')

    return f"<tg-spoiler>Символов:\t{_letters}\nЗнаков препинания:\t{_symbols}\nПробелов:\t{_spaces}</tg-spoiler>"
        
def default(bot, message):
    _text = "Не знаю такую команду"

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML")

def start(bot, message):

    _text = "Привет!"

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())

def menu(bot, message):
    pass

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

    #Кнопки
    _markup = types.InlineKeyboardMarkup()
    _btnHelp = types.InlineKeyboardButton('Помощь', url='https://t.me//wi_us')
    _btnAbout = types.InlineKeyboardButton('Мой создатель', url='https://vk.com/wiuss')
    _btnJoke = types.InlineKeyboardButton('Выдать базу', url='https://t.me//wi_us')
    _btnMath = types.InlineKeyboardButton('Квадратное уравнение', url='https://vk.com/wiuss')

    _markup.add(_btnAbout, _btnHelp, _btnJoke, _btnMath, row_width=2)
    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getInlineKeyboard_Menu())


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
    _text += "tg: @wi_us\n"
    _text += "vk: https://vk.com/wiuss"

    _text += "\n\n" + countSomeSymbols(_text)

    #Кнопки
    _markup = types.InlineKeyboardMarkup()
    _vk = types.InlineKeyboardButton('ВКонтакте', url='https://vk.com/wiuss')
    _tg = types.InlineKeyboardButton('Telegram', url='https://t.me//wi_us')
    _markup.add(_vk)
    _markup.add(_tg)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=_markup)

def joke(jokes, bot, message):
    if len(jokes) == 0:
        with open("NtiWorks//Task5//serializeText//anekdots.json", "r", encoding="UTF-8") as file:
            jokes = json.loads(file.read())
            
    _text = jokes[random.randint(0, len(jokes))]

    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Joke())

    return jokes

def math(bot, message):
    
    def findDiscr(a, b, c):
        discr = b**2 - 4*a*c
        if a != 0:   
            if discr > 0:
                x1 = round((-b + sqrt(discr)) / (2 * a), 4)
                x2 = round((-b - sqrt(discr)) / (2 * a), 4)

                return f"x1 = {x1}, x2 = {x2}"
            elif discr == 0:
                x1 = round((-b + sqrt(discr)) / (2 * a), 4)

                return f"x = {x1}"
            else:
                return "Нет корней!"
        else:
            return "0"


    _min = -10
    _max = +10

    a = float(random.randint(_min, +_max))
    if a == 0:
        a = float(random.randint(_min, +_max))

    b = float(random.randint(_min, +_max))
    c = float(random.randint(_min, +_max))

    _primer = f"{a} * x1^2 + {b} * x2 + {c} = 0"
    _text = f"Пример:\t{_primer}\n"
    _text += f"Ответ:\t"


    #Кнопки

    _markup = types.InlineKeyboardMarkup()
    _answer1 = types.InlineKeyboardButton(f"{findDiscr(a, b, c)}", callback_data='correct')
    _answer2 = types.InlineKeyboardButton(f"{findDiscr(float(random.randint(_min, +_max)), float(random.randint(_min, +_max)), float(random.randint(_min, +_max)))}", callback_data='false')
    _answer3 = types.InlineKeyboardButton(f"{findDiscr(float(random.randint(_min, +_max)), float(random.randint(_min, +_max)), float(random.randint(_min, +_max)))}", callback_data='false')
    _answer4 = types.InlineKeyboardButton(f"{findDiscr(float(random.randint(_min, +_max)), float(random.randint(_min, +_max)), float(random.randint(_min, +_max)))}", callback_data='false')


    _arr = [_answer1, _answer2, _answer3, _answer4]
    random.shuffle(_arr)

    for i in range(4):
        _markup.add(_arr[i])

    #_markup.add(_answer1, _answer2, _answer3, _answer4, row_width=2)

    _text += "\n\n" + countSomeSymbols(_text)
    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=_markup)


def getDescrHelp(bot, message):
    _text = "Команда /help перечислит список команд с кратким описанием"
    
    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())

def getDescrAbout(bot, message):
    _text = "Команда /about расскажет о великом человеке, создавшем меня"
    
    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())


def getDescrJoke(bot, message):
    _text = "Команда /joke выдаст базу"
    
    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())


def getDescrMath(bot, message):
    _text = "Команда /math посчитает корни квадратного уравнения"
    
    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())

def getMathAnswer(bot, message, isRight):
    _text = ""
    if isRight == True:
        _text = "Ты чертовски прав!"
    else:
        _text = "Неверно! Учи уроки!"

    _text += "\n\n" + countSomeSymbols(_text)

    bot.send_message(message.chat.id, _text, parse_mode="HTML", reply_markup=kbrds.getReplyKeyboard_Menu())
