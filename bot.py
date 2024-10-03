import telebot
from telebot import types
from datetime import datetime, timedelta

API_TOKEN = '727421163:AAGdQxls1CdRAJIrDpXa5HwAmfsMd5w5-7k'
bot = telebot.TeleBot(API_TOKEN)

users_data = {}  # Словарь для хранения данных пользователей


# Шаг 1: Запрос контакта
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button = types.KeyboardButton('Отправить контакт', request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, 'Пожалуйста, отправьте свой контакт',
                     reply_markup=markup)


# Шаг
# 2: Обработка контакта и запрос имени
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    contact = message.contact.phone_number
    # Сохраняем номер телефона
    users_data[message.chat.id] = {'phone': contact}
    bot.send_message(message.chat.id, f'Спасибо! Ваш номер: {contact}')
    bot.send_message(message.chat.id, 'Теперь введите своё имя:')
    bot.register_next_step_handler(message, get_name)


# Шаг 3: Обработка имени и выбор времени
def get_name(message):
    name = message.text
    users_data[message.chat.id]['name'] = name  # Сохраняем имя
    bot.send_message(message.chat.id, f'Спасибо, {name}!'
                     ' Теперь выберите дату для записи:')

    # Создание inline-клавиатуры для выбора даты
    markup = types.InlineKeyboardMarkup()

    # Получаем текущую дату и генерируем даты для текущего месяца
    today = datetime.today()
    for i in range(7):  # Позволим выбирать из следующих 7 дней
        day = today + timedelta(days=i)
        day_str = day.strftime("%d-%m-%Y")  # Форматируем дату для показа
        button = types.InlineKeyboardButton(day_str, callback_data=day_str)
        markup.add(button)

    bot.send_message(message.chat.id, "Выберите дату:", reply_markup=markup)


# Шаг 4: Обработка нажатий на inline-кнопки
def callback_query(call):
    chat_id = call.message.chat.id

    # Если пользователь выбрал дату
    if call.data.startswith('date_'):
        selected_date = call.data.split('_')[1]  # Получаем выбранную дату
        users_data[chat_id]['date'] = selected_date  # Сохраняем выбранную дату
        bot.send_message(chat_id,
                         f"Вы выбрали дату: {selected_date}. Теперь "
                         "выберите время:")

        # Создаём inline-кнопки для выбора времени
        markup = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton(
            "14:00",
            callback_data='time_14:00'
            )
        button_2 = types.InlineKeyboardButton(
            "16:30",
            callback_data='time_16:30'
            )
        markup.add(button_1, button_2)

        bot.send_message(chat_id, "Выберите время:", reply_markup=markup)

    # Если пользователь выбрал время
    elif call.data.startswith('time_'):
        # Получаем выбранное время
        selected_time = call.data.split('_')[1]
        # Сохраняем выбранное время
        users_data[chat_id]['time'] = selected_time

        # Подтверждаем запись
        bot.send_message(chat_id, f"Запись подтверждена на {users_data[chat_id]['date']} в {selected_time}!")


bot.polling()
