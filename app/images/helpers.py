from PIL import Image

MAX_THUMBNAIL_SIZE = 200

def resize_logo(instance):
    
    width = instance.file.width
    height = instance.file.height

    filename = instance.file.path

    max_size = max(width, height)

    if max_size > MAX_THUMBNAIL_SIZE:
        image = Image.open(filename)
        image = image.resize(
            (round(width / max_size * MAX_THUMBNAIL_SIZE),
            round(width / max_size * MAX_THUMBNAIL_SIZE)),
            Image.ANTIALIAS
        )
        image.save(filename)


