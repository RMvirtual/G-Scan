import sys
from controller import ImageViewerController
from src.main.gui.app.app import GuiApplication


def main(image_path: str = None) -> None:
    """Main Loop for loading an image to test viewer functionality."""
    application = GuiApplication()
    viewer = ImageViewerController()

    if image_path:
        viewer.load(image_path)

    application.run()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])

    else:
        main()