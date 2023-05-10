# Приступим к работе!
from venv import logger


import telebot as telebot
bot = telebot.TeleBot('')  # Input your token


@bot.message_handler(commands=['start', 'help'])  # Обработка входящих команд /start и /help
def send_welcome(message):
    bot.reply_to(message, 'Приветствую, авантюрист!')
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardMarkup(text='Серёга', url='https://vk.com/serhioofficialpage')
    markup.add(button1)
    bot.send_message(message.from_user.id, 'Моя страничка вк')


@bot.message_handler(func=lambda x: True)        # Обрабатываем любое сообщение, поэтому функция всегда True
def echo_all(message):
    if message.text == 'Чел ты':
        bot.reply_to(message, 'Скорее чел ты')
    elif message.text == 'Офф с позором':
        bot.reply_to(message, 'Офф с позором? Это офф с супер честью!')
    else:
        bot.reply_to(message, 'Я ещё пока ничего не умею, но скоро научусь')


@bot.message_handler(content_types=['document'])
def make_doc_reaction(message):
    bot.reply_to(message, 'Благодарю за отправленный документ!')


@bot.message_handler(content_types=['audio'])
def make_audio_reaction(message):
    bot.reply_to(message, 'Благодарю за отправленный аудиофайл!')


# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):
#     logger.info(call)


bot.infinity_polling()



