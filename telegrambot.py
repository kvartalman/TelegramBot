# Приступим к работе!

import telebot
bot = telebot.TeleBot('5943669544:AAErEBN8Qqa1mUWbhLWMXcIDQneW2m9oqi4')


@bot.message_handler(commands=['start', 'help'])  # Обработка входящих команд /start и /help
def send_welcome(message):
    bot.reply_to(message, 'Приветствую, авантюрист!')


@bot.message_handler(func=lambda x: True)        # Обрабатываем любое сообщение, поэтому функция всегда True
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


