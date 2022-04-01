import wx


def scaleDimensionsToRatio(
        ratio: float, width: int, height: int) -> tuple[int, int]:
    is_too_wide = aspectRatioCorrectness(ratio, width, height)["too wide"]

    if is_too_wide:
        width = height * ratio

    else:
        height = width / ratio

    return width, height


def scaleDimensionsToImageAspectRatio(
        image: wx.Image, width: int, height: int) -> tuple[int, int]:
    return scaleDimensionsToRatio(aspectRatioFromImage(image), width, height)


def aspectRatioFromImage(image: wx.Image) -> float:
    """Returns an image's aspect ratio (how many pixels wide for every
    pixel in height).
    """
    return aspectRatio(image.GetWidth(), image.GetHeight())


def aspectRatio(width: int, height: int) -> float:
    """Returns a ratio of how many pixels wide for every pixel in
    height.
    """
    return float(width) / float(height)


def aspectRatioCorrectness(
        ratio: float, width: int, height: int) -> dict[str, bool]:
    """Returns a dictionary of reported concerning whether the new width
    and height dimensions provided will match a provided aspect ratio.
    """
    new_ratio = aspectRatio(width, height)

    return {
        "preserved": new_ratio == ratio,
        "too wide": new_ratio > ratio,
        "too tall": new_ratio < ratio
    }
