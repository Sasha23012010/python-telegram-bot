import telebot
from telebot.util import content_type_service

token = '7838430929:AAE9AWSdfN1B115_WAxHb\dQtr792RZYb088'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def botmessege(message):
    mes = message.text + ' - Цу написав класний хлопець! '
    bot.send_message(message.chat.id, mes)

bot.polling()