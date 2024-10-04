import telebot
from config import API_TOKEN
from users_data import UsersData
from admin import Admin


class MyBot:
    def __init__(self):
        self.bot = telebot.TeleBot(API_TOKEN)
        self.users_data = UsersData()
        self.admin = Admin(self.bot, self.users_data)
        self.register_handlers()

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_command(message):
            self.bot.send_message(message.chat.id,
                                  "Привет! Я бот для записи на приём!")

        # Регистрируем админские команды
        self.admin.register_admin_handlers()

    def run(self):
        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    my_bot = MyBot()
    my_bot.run()
