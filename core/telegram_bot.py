import telegram

from core.settings import TELEGRAM_BOT_AUTH, TELEGRAM_BOT_CHANNEL_ID


class TelegramBot:

    def __new__(cls):
        """ We need only one instance of telegram bot"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_BOT_AUTH)

    @staticmethod
    def get_basic_data():
        return {'chat_id': TELEGRAM_BOT_CHANNEL_ID}

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


telegram_bot = TelegramBot()
