# Приступим к работе!

import telebot
bot = telebot.TeleBot('')  # Input your token


@bot.message_handler(commands=['start', 'help'])  # Обработка входящих команд /start и /help
def send_welcome(message):
    bot.reply_to(message, 'Приветствую, авантюрист!')


@bot.message_handler(func=lambda x: True)        # Обрабатываем любое сообщение, поэтому функция всегда True
def echo_all(message):
    if message.text == 'Чел ты':
        bot.reply_to(message, 'Скорее чел ты')
    elif message.text == 'Офф с позором':
        bot.reply_to(message, 'Офф с позором? Это офф с супер честью!')
    else:
        bot.reply_to(message, 'Я ещё пока ничего не умею, но скоро научусь')


bot.infinity_polling()


#123