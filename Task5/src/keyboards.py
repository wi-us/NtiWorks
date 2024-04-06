from telebot import types
import telebot

def getReplyKeyboard_Start():
    _markup = types.ReplyKeyboardMarkup()
    _start = types.KeyboardButton('/start')
    _markup.add(_start)

    return _markup

def getReplyKeyboard_Menu():
    _markup = types.ReplyKeyboardMarkup()
    _help = types.KeyboardButton('/help')
    _about = types.KeyboardButton('/about')
    _joke = types.KeyboardButton('/joke')
    _math = types.KeyboardButton('/math')

    _markup.add(_help, _about, _joke, _math, row_width=2)

    return _markup

def getInlineKeyboard_Menu():
    _markup = types.InlineKeyboardMarkup()
    _btnHelp = types.InlineKeyboardButton('Помощь', callback_data="getHelp")
    _btnAbout = types.InlineKeyboardButton('Мой создатель', callback_data="getAbout")
    _btnJoke = types.InlineKeyboardButton('Выдать базу', callback_data="getJoke")
    _btnMath = types.InlineKeyboardButton('Квадратное уравнение', callback_data="getMath")

    _markup.add(_btnAbout, _btnHelp, _btnJoke, _btnMath, row_width=2)
    return _markup

def getReplyKeyboard_Joke():
    _markup = types.ReplyKeyboardMarkup()
    #_help = types.KeyboardButton('/help')
    #_about = types.KeyboardButton('/about')
    #_joke = types.KeyboardButton('/joke')
    #_math = types.KeyboardButton('/math')
    _more = types.KeyboardButton('Хочу ещё!')
    _menu = types.KeyboardButton('Меню')

    #_markup.add(_help, _about, _joke, _math, _more, row_width=2)
    _markup.add(_more, _menu, row_width=2)
    return _markup