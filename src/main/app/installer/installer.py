import os


def install_app_data() -> None:
    app_data_path = os.environ["LOCALAPPDATA"] + "\\G-Scan"

    exists = False

    if not exists:
        os.mkdir(app_data_path)