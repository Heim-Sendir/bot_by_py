import telebot

# Вставь сюда свой токен
API_TOKEN = '727421163:AAGdQxls1CdRAJIrDpXa5HwAmfsMd5w5-7k'

bot = telebot.TeleBot(API_TOKEN)


# Простая функция для ответа на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Запуск бота
print("Bot is starting...")
bot.polling()
