from core.actions import get_arguments, get_input, get_auth_token, get_chat_id
from core.telegram_bot import TelegramBot


def send_message():
    args = get_arguments()
    message = get_input(args)
    telegram_bot = TelegramBot(auth_token=get_auth_token(args), chat_id=get_chat_id(args))
    return telegram_bot.send_message(message)


if __name__ == '__main__':
    send_message()
