class UsersData:
    def __init__(self):
        self.data = {}  # Здесь храним данные пользователей

    def ensure_user_exists(self, user_id):
        if user_id not in self.data:
            self.data[user_id] = {}

    def save_user_data(self, user_id, key, value):
        self.data[user_id][key] = value
