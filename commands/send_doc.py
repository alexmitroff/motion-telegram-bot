from core.actions import get_arguments, get_input, get_auth_token, get_chat_id
from core.telegram_bot import TelegramBot
from core.validators import does_file_exist


def send_doc():
    args = get_arguments()
    file_path = get_input(args)
    does_file_exist(file_path)
    telegram_bot = TelegramBot(auth_token=get_auth_token(args), chat_id=get_chat_id(args))
    return telegram_bot.send_doc(file_path)


if __name__ == '__main__':
    send_doc()