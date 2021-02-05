from core.actions import get_arguments, get_file_path, get_auth_token, get_chat_id, get_video_preview_path
from core.telegram_bot import TelegramBot
from core.validators import does_file_exist


def send_video_preview():
    args = get_arguments()
    file_path = get_file_path(args)
    does_file_exist(file_path)
    preview_path = get_video_preview_path(file_path)
    does_file_exist(preview_path)
    telegram_bot = TelegramBot(auth_token=get_auth_token(args), chat_id=get_chat_id(args))
    return telegram_bot.send_image(preview_path)


if __name__ == '__main__':
    send_video_preview()
