import os


def does_file_exist(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        raise IOError(f"'{file_path}' does not exists!")


def is_file_valid(file_path, minimal_file_size):
    return os.path.getsize(file_path) > minimal_file_size
