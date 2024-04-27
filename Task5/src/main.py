import commands
import telebot
import keyboards as kbrds
TOKEN = '7188212020:AAGn0EdEKiGhdlwf1KZ3PtyePxAZwduvuDI'

bot = telebot.TeleBot(TOKEN)
jokes = []



@bot.message_handler(commands=commands.items)
def start_message(message):
        match message.text:
            case '/start':
                commands.start(bot=bot, message=message)

            case '/help':
                commands.help(bot=bot, message=message)  

            case '/about':
                commands.about(bot=bot, message=message)

            case '/joke':
                commands.joke(jokes, bot=bot, message=message)

            case '/math':
                commands.math(bot=bot, message=message)

            case '/menu':
                commands.math(bot=bot, message=message)

            case __:
                commands.default(bot=bot, message=message)

@bot.message_handler(content_types=['text'])
def func(message):
    match message.text:
        case 'Хочу ещё!':
            commands.joke(jokes, bot=bot, message=message)
        case 'Меню':
            commands.start(bot=bot, message=message)

@bot.callback_query_handler(func=lambda call: call.data)
def test(call):
    match call.data:
        case 'getHelp':
            commands.getDescrHelp(bot=bot, message=call.message)

        case 'getAbout':
            commands.getDescrAbout(bot=bot, message=call.message)

        case 'getJoke':
            commands.getDescrJoke(bot=bot, message=call.message)

        case 'getMath':
            commands.getDescrMath(bot=bot, message=call.message)

        case 'correct':
            commands.getMathAnswer(bot=bot, message=call.message, isRight=True)

        case 'false':
            commands.getMathAnswer(bot=bot, message=call.message, isRight=False)

                       
bot.infinity_polling()
