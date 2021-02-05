import os

from core.settings import TELEGRAM_MIN_FILE_SIZE_BYTES


def is_file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        raise IOError(f"'{file_path}' does not exists!")


def is_file_valid(file_path):
    return os.path.getsize(file_path) > TELEGRAM_MIN_FILE_SIZE_BYTES
