from core.actions import get_file_path
from core.telegram_bot import telegram_bot
from core.validators import does_file_exist


def send_image():
    file_path = get_file_path()
    does_file_exist(file_path)
    return telegram_bot.send_image(file_path)


if __name__ == '__main__':
    send_image()
