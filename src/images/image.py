import wand.image
import PIL
import pdf.extractor


class Image:
    def __init__(self, img):
        self.img = img


def rotate_to_portrait(source: str, output: str) -> None:
    with wand.image.Image(filename=source, resolution=300) as image_stream:
        is_landscape = image_stream.width > image_stream.height

        if is_landscape:
            image_stream.rotate(270)

        image_stream.save(filename=output)


def from_pdf(source: str) -> PIL.Image:
    extractor = .pdf.extractor.PdfExtractor()