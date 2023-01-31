import os
import shutil


def install_app_data() -> None:
    app_data_path = os.environ["LOCALAPPDATA"] + "\\G-Scan"

    if not os.path.exists(app_data_path):
        os.mkdir(app_data_path)

    for filename in os.listdir(app_data_path):
        filepath = os.path.join(app_data_path, filename)

        try:
            shutil.rmtree(filepath)

        except OSError:
            os.remove(filepath)