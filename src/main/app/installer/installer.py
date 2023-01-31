import os
import shutil


def install_app_data() -> None:
    make_app_data_directory()
    empty_app_data()


def make_app_data_directory():
    if not os.path.exists(app_data_path()):
        os.mkdir(app_data_path)


def empty_app_data():
    for filename in os.listdir(app_data_path()):
        file_path = os.path.join(app_data_path, filename)
        delete_file(file_path)


def delete_file(file_path):
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")


def app_data_path() -> str:
    return os.environ["LOCALAPPDATA"] + "\\G-Scan"