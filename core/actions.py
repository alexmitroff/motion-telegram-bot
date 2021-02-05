import argparse

FILE_ARGUMENT = 'file'


def get_arguments():
    parser = argparse.ArgumentParser(description='Sends video or image to telegram channel')
    parser.add_argument('-f', f'--{FILE_ARGUMENT}', required=True, help='path to video or image')
    return parser.parse_args()


def get_file_path():
    args = get_arguments()
    return getattr(args, FILE_ARGUMENT, '')
