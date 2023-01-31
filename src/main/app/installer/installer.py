import os
import shutil


def install_app_data() -> None:
    app_data_path = os.environ["LOCALAPPDATA"] + "\\G-Scan"

    if not os.path.exists(app_data_path):
        os.mkdir(app_data_path)

    for filename in os.listdir(app_data_path):
        file_path = os.path.join(app_data_path, filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
