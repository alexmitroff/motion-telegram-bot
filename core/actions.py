import argparse

ARGUMENT_INPUT = 'input'
ARGUMENT_AUTH = 'bot'
ARGUMENT_CHAT = 'chat'
ARGUMENT_MIN = 'minimal'


def get_arguments():
    parser = argparse.ArgumentParser(description='Sends message, video or image to telegram channel')
    parser.add_argument('-i', f'--{ARGUMENT_INPUT}', required=True, help='Something you want to sent to telegram chat.'
                                                                         'This could be a text, path to image '
                                                                         'or path to video')
    parser.add_argument('-b', f'--{ARGUMENT_AUTH}', required=True, help='Telegram bot auth token')
    parser.add_argument('-c', f'--{ARGUMENT_CHAT}', required=True, help='Telegram chat id')
    parser.add_argument('-m', f'--{ARGUMENT_MIN}', default=10, help='A minimal file size.'
                                                                    'Used to filter important videos')
    return parser.parse_args()


def get_input(args):
    return getattr(args, ARGUMENT_INPUT)


def get_auth_token(args):
    return getattr(args, ARGUMENT_AUTH)


def get_chat_id(args):
    return getattr(args, ARGUMENT_CHAT)


def get_minimal_file_size(args):
    return getattr(args, ARGUMENT_MIN)


def get_video_preview_path(video_file_path, preview_extention='jpg'):
    video_file_path_parts = video_file_path.split('.')
    video_file_path_parts[-1] = preview_extention
    return '.'.join(video_file_path_parts)
