import wand.image


def rotate_to_portrait(source: str, output: str) -> None:
    with wand.image.Image(
            filename=source, resolution=300) as img_simulator:
        if img_simulator.width > img_simulator.height:
            img_simulator.rotate(270)
            img_simulator.save(filename=output)
        else:
            img_simulator.save(filename=output)
