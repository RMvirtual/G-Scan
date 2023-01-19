from src.main.gui.image_viewer.viewer import ImageViewer
from src.main.gui.app.app import GuiApplication


class ImageViewerController:
    def __init__(self):
        print("Application started.")
        self._application = GuiApplication()
        self._viewer = ImageViewer()
        self._viewer.set_exit_callback(self.close)
        self._application.run()
        print("Application ended.")

    def load(self, image_path: str) -> None:
        self._viewer.set_image(image_path)

    def close(self, event: any = None) -> None:
        self._viewer.close()
