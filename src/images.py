import wand.image
import wx

from views.metrics.aspect_ratio import scale_with_ratio


class Image:
    def __init__(self, img):
        self.img = img


def rotate_to_portrait(source: str, output: str) -> None:
    with wand.image.Image(filename=source, resolution=300) as image_stream:
        is_landscape = image_stream.width > image_stream.height

        if is_landscape:
            image_stream.rotate(270)

        image_stream.save(filename=output)


def toBitmap(image_path: str) -> wx.Bitmap:
    return wx.Bitmap(toImage(image_path))


def toImage(image_path: str) -> wx.Image:
    return wx.Image(name=image_path)


def toScaledImage(image_path: str, width: int, height: int) -> wx.Image:
    image = toImage(image_path)

    return _scaledImage(image, width, height)


def toScaledImagePreserveAspectRatio(image_path: str, width: int, height: int):
    image = toImage(image_path)

    width, height = scale_with_ratio(
        image, width, height)

    return toScaledImage(image_path, width, height)


def _scaledImage(image: wx.Image, width: int, height: int) -> wx.Image:
    return image.Scale(
        width=width, height=height, quality=wx.IMAGE_QUALITY_HIGH)
