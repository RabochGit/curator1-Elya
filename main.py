import telebot

bot = telebot.TeleBot('6748839980:AAHlgIwY4tBefU3xNPFxVoeNRL9r9O3jG84')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Рада видеть тебя здесь. Какой бы дизайн ты хотел?)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'В каких цветах?')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'Есть ли какие-то примечания к работе? Может исходные материалы, логотипы и тд.')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Задание принято!')


bot.infinity_polling()