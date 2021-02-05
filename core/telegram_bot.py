import telegram


class TelegramBot:

    def __init__(self, auth_token, chat_id):
        self.bot = telegram.Bot(token=auth_token)
        self.chat_id = chat_id

    def get_basic_data(self):
        return {'chat_id': self.chat_id}

    def send_message(self, text):
        request_data = self.get_basic_data()
        request_data['text'] = text
        response = self.bot.sendMessage(**request_data)
        return response.text == text

    def send_image(self, file_path):
        request_data = self.get_basic_data()
        request_data['photo'] = open(file_path, 'rb')
        response = self.bot.sendPhoto(**request_data)
        if hasattr(response, 'photo'):
            return hasattr(response.photo, 'file_size')

    def send_video(self, file_path):
        request_data = self.get_basic_data()
        request_data['video'] = open(file_path, 'rb')
        response = self.bot.sendVideo(**request_data)
        if hasattr(response, 'video'):
            return hasattr(response.video, 'file_size')
