from src.main.gui.image_viewer.viewer import ImageViewer


class ImageViewerController:
    def __init__(self):
        self._initialise_viewer()

    def _initialise_viewer(self):
        self._viewer = ImageViewer()
        self._viewer.set_exit_callback(self.close)
        self._viewer.set_submit_callback(self.submit)
        self._viewer.set_skip_callback(self.skip)
        self._viewer.set_split_callback(self.split)

    def load(self, image_path: str) -> None:
        self._viewer.set_image(image_path)

    def close(self, event: any = None) -> None:
        self._viewer.close()

    def submit(self, event: any = None) -> None:
        print("SUBMIT")

    def skip(self, event: any = None) -> None:
        print("SKIP")

    def split(self, event: any = None) -> None:
        print("SPLIT")
