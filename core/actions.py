import argparse

ARGUMENT_FILE = 'file'
ARGUMENT_AUTH = 'bot'
ARGUMENT_CHAT = 'chat'
ARGUMENT_MIN = 'minimal'


def get_arguments():
    parser = argparse.ArgumentParser(description='Sends video or image to telegram channel')
    parser.add_argument('-f', f'--{ARGUMENT_FILE}', required=True, help='path to video or image')
    parser.add_argument('-b', f'--{ARGUMENT_AUTH}', required=True, help='telegram auth token')
    parser.add_argument('-c', f'--{ARGUMENT_CHAT}', required=True, help='telegram channel id')
    parser.add_argument('-m', f'--{ARGUMENT_MIN}', default=10, help='Validation property minimal file size in Mb')
    return parser.parse_args()


def get_file_path(args):
    return getattr(args, ARGUMENT_FILE)


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
