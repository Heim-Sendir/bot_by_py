import telebot
from telebot import types


# Вставь сюда свой токен
API_TOKEN = '727421163:AAGdQxls1CdRAJIrDpXa5HwAmfsMd5w5-7k'

bot = telebot.TeleBot(API_TOKEN)


# Простая функция для ответа на любое сообщение
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['start'])  # Обработка команды /start
def send_welcome(message):
    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # Кнопка для отправки контакта
    button = types.KeyboardButton('Отправить контакт', request_contact=True)
    # Добавляем кнопку на клавиатуру
    markup.add(button)
    # Сообщение с кнопкой
    bot.send_message(message.chat.id,
                     'Пожалуйста, отправьте свой контакт',
                     reply_markup=markup)


# Запуск бота
print("Bot is starting...")
bot.polling()
