import os
import shutil
from src.main import file_system


def install_app_data() -> None:
    make_app_data_directory()
    empty_app_data()
    create_default_user_settings()


def make_app_data_directory():
    if not os.path.exists(file_system.app_data_directory()):
        os.mkdir(app_data_path)


def empty_app_data():
    for filename in os.listdir(file_system.app_data_directory()):
        file_path = os.path.join(file_system.app_data_directory(), filename)
        delete_file(file_path)


def delete_file(file_path):
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")


def create_default_user_settings():
    defaults_path = file_system.config_directory() + "\\user_defaults.json"
    out_path = file_system.app_data_directory() + "\\user_settings.json"

    shutil.copyfile(src=defaults_path, dst=out_path)
