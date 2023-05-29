from utils import get_picture_of_the_day
import telebot
import os

TOKEN = os.getenv('telegram_token')

bot = telebot.TeleBot(TOKEN)

WELCOME_MESSAGE = "Hello there! I am a bot made by Siddharth.. \nSend me the command /pic and I will send you NASA's pic of the day"


@bot.message_handler(func=lambda mesg: True)
def check_bharti(message):
  if message.text == "bharti-t71402":
    bot.send_message(
      message.chat.id,
      "Heyyy Bhartiiiiii! How're you doing! my owner loves railing youuuuuuu")


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(message, WELCOME_MESSAGE)


@bot.message_handler(commands=['pic'])
def get_picture(message):
  chat_id = message.chat.id
  pic_url, description = get_picture_of_the_day()
  bot.send_photo(chat_id, pic_url, caption=description)


bot.infinity_polling()
