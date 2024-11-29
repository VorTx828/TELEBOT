import telebot
import threading as th

TOKEN = '8101296963:AAGKmU4KbCmP6jb8tDHPVrtmSsqP6zdUHhc'
bot = telebot.TeleBot(TOKEN)
subscribed_users = set()

def Notifications():
    while True:
        input()
        photo_path = 'C:\\Users\\Viacheslav\\Pictures\\1.png'  # Замените на путь к вашему изображению
        with open(photo_path, 'rb') as photo:
            for user_id in subscribed_users:
                try:
                    bot.send_photo(user_id, photo)
                except Exception as e:
                    print(f"Не удалось отправить фото пользователю {user_id}: {e}")


tr = th.Thread(target=Notifications)
tr.start()



@bot.message_handler(commands=['start'])
def send_welcome(message):
    subscribed_users.add(message.chat.id)
    bot.reply_to(message, "Привет! Я ваш Telegram-бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Напишите /start, чтобы начать.")

if __name__ == '__main__':
    bot.polling(none_stop=True)