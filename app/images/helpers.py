from PIL import Image

MAX_THUMBNAIL_SIZE = 200
MAX_IMAGE_SIZE = 1024


def resize_logo(instance):

    width = instance.avatar.width
    height = instance.avatar.height

    filename = instance.avatar.path

    max_size = max(width, height)

    if max_size > MAX_THUMBNAIL_SIZE:
        image = Image.open(filename)
        image = image.resize(
            (round(width / max_size * MAX_THUMBNAIL_SIZE),
             round(height / max_size * MAX_THUMBNAIL_SIZE)),
            Image.ANTIALIAS
        )
        image.save(filename)


def resize_image(instance):

    width = instance.file.width
    height = instance.file.height

    filename = instance.file.path

    max_size = max(width, height)

    if max_size > MAX_IMAGE_SIZE:
        image = Image.open(filename)
        image = image.resize(
            (round(width / max_size * MAX_IMAGE_SIZE),
             round(height / max_size * MAX_IMAGE_SIZE)),
            Image.ANTIALIAS
        )
        image.save(filename)
