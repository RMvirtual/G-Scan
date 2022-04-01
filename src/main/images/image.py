import wand.image


def rotate_to_portrait(source: str, output: str) -> None:
    with wand.image.Image(filename=source, resolution=300) as image_stream:
        is_landscape = image_stream.width > image_stream.height

        if is_landscape:
            image_stream.rotate(270)

        image_stream.save(filename=output)
