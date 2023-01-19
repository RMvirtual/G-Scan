import sys
from controller import ImageViewerController


def main(image_path: str) -> None:
    _ = ImageViewerController()


if __name__ == '__main__':
    main(sys.argv[1])
