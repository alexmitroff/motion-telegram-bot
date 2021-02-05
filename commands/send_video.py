from core.actions import get_arguments, get_file_path, get_auth_token, get_chat_id
from core.telegram_bot import TelegramBot
from core.validators import does_file_exist


def send_video():
    args = get_arguments()
    file_path = get_file_path(args)
    does_file_exist(file_path)
    telegram_bot = TelegramBot(auth_token=get_auth_token(args), chat_id=get_chat_id(args))
    return telegram_bot.send_video(file_path)


if __name__ == '__main__':
    send_video()
