import sys
from src.main.gui.image_viewer.viewer import ImageViewer
from src.main.gui.app.app import GuiApplication


def main(image_path: str) -> None:
    print("Application started.")
    gui_application = GuiApplication()
    viewer = ImageViewer()
    viewer.set_exit_callback(viewer.close)
    # viewer.set_image(image_path)

    gui_application.run()
    print("Application ended.")


if __name__ == '__main__':
    main(sys.argv[1])
