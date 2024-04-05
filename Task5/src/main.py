import commands
import telebot

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

            case __:
                commands.default(bot=bot, message=message)


bot.infinity_polling()