class Admin:
    def __init__(self, bot, users_data):
        self.bot = bot
        self.users_data = users_data

    def register_admin_handlers(self):
        @self.bot.message_handler(commands=['admin'])
        def admin_panel(message):
            if message.from_user.id not in admin_ids:
                self.bot.send_message(message.chat.id,
                                      "У вас нет доступа к этой команде.")
                return
            self.bot.send_message(message.chat.id,
                                  "Добро пожаловать в админскую панель!")

        @self.bot.message_handler(commands=['view_appointments'])
        def view_appointments(self, message):
        if not self.is_admin(message.from_user.id):
            self.bot.send_message(message.chat.id, "У вас нет доступа к этой команде.")
            return

        if not self.users_data.data:
            self.bot.send_message(message.chat.id, "Записей нет.")
            return

        response = "Список всех записей:\n"
        for user_id, data in self.users_data.data.items():
            response += f"Пользователь {data.get('name', 'Без имени')} ({data.get('phone', 'Без телефона')}), дата: {data.get('date', 'Не указана')}, время: {data.get('time', 'Не указано')}\n"

        self.bot.send_message(message.chat.id, response)
