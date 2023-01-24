from src.main.app.pdf_viewer.controller import ImageViewerController
from src.main.gui.app import GuiApplication


def main(image_path: str = None) -> None:
    application = GuiApplication()
    viewer = ImageViewerController()

    if image_path:
        viewer.load(image_path)

    application.run()


if __name__ == '__main__':
    main()
