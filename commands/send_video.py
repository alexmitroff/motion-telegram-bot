from core.actions import get_file_path
from core.validators import is_file_exists


def send_video():
    file_path = get_file_path()
    is_file_exists(file_path)
    print(f"Run send-video script! File path: '{file_path or None}'")


if __name__ == '__main__':
    send_video()
