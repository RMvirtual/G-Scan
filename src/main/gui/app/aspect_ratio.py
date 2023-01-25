import wx


def aspectRatio(width: int, height: int) -> float:
    return float(width) / float(height)


def scaleDimensionsToRatio(
        ratio: float, width: int, height: int) -> tuple[int, int]:
    is_too_wide = aspectRatioCorrectness(ratio, width, height)["too wide"]

    if is_too_wide:
        width = height * ratio

    else:
        height = width / ratio

    return width, height


def best_fit(
        image: wx.Image, width: int, height: int) -> tuple[int, int]:
    return scaleDimensionsToRatio(aspectRatioFromImage(image), width, height)

def aspectRatioFromImage(image: wx.Image) -> float:
    return aspectRatio(image.GetWidth(), image.GetHeight())

def aspectRatioCorrectness(
        ratio: float, width: int, height: int) -> dict[str, bool]:
    new_ratio = aspectRatio(width, height)

    return {
        "preserved": new_ratio == ratio,
        "too wide": new_ratio > ratio,
        "too tall": new_ratio < ratio
    }
