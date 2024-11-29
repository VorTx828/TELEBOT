import telebot
import threading as th

TOKEN = '8101296963:AAGKmU4KbCmP6jb8tDHPVrtmSsqP6zdUHhc'
bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш Telegram-бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Напишите /start, чтобы начать.")

if __name__ == '__main__':
    bot.polling(none_stop=True)